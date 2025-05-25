from flask import Flask, request, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
import mysql.connector


# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "internship"
}

app = Flask(__name__)


def scrape_google(query):
    """Scrapes Google search results for internship links."""
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)




    search_url = f"https://www.google.com/search?q={query}+internship"
    print(f"Opening URL: {search_url}")
    driver.get(search_url)
    time.sleep(3)

    internships = []
    results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")

    for i, result in enumerate(results[:10]):
        try:
            title_element = result.find_element(By.CSS_SELECTOR, "h3")
            link_element = result.find_element(By.TAG_NAME, "a")

            title = title_element.text.strip() if title_element.text.strip() else query + " internship"
            link = link_element.get_attribute("href") if link_element else "No Link Found"

            internships.append({"title": title, "link": link})
        except Exception as e:
            print(f"Error in result {i + 1}: {e}")

    driver.quit()
    return internships


@app.route('/')
def home():
    """Renders the home page."""
    print("Home page visited")
    return render_template("index.html")


def store_results_in_db(results, query):
    """Stores scraped internship results in MySQL database."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO internships (title, link, search_query)
        VALUES (%s, %s, %s)
        """
        data = [(result["title"], result["link"], query) for result in results]
        cursor.executemany(insert_query, data)

        conn.commit()
        print(f"{cursor.rowcount} records inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/search', methods=['GET'])
def search():
    """Handles search request and stores results in database."""
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "No query provided"}), 400

    internship_links = scrape_google(query)
    store_results_in_db(internship_links, query)
    return jsonify(internship_links)


def get_stored_results():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("SELECT title, link, search_query FROM internships ORDER BY id DESC LIMIT 10")
        results = cursor.fetchall()

        return results

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return []

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route("/previous_searches", methods=["GET"])
def load_results():
    results = get_stored_results()
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
