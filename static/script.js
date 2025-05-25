// document.addEventListener("DOMContentLoaded", () => {
//     document.getElementById("searchForm").addEventListener("submit", async function (event) {
//         event.preventDefault();

//         const keyword = document.getElementById("keyword").value;
//         const skills = document.getElementById("skills").value;
//         const startDate = document.getElementById("startDate").value;

//         const query = `${keyword} internship ${skills} ${startDate}`;
//         const response = await fetch(`/search?query=${encodeURIComponent(query)}`);
//         const data = await response.json();

//         let resultsDiv = document.getElementById("results");
//         resultsDiv.innerHTML = "<h2>Internship Results</h2>";
//         if (data.length === 0) {
//             resultsDiv.innerHTML += "<p>No internships found.</p>";
//         } else {
//             data.forEach((internship) => {
//                 resultsDiv.innerHTML += `<p><a href="${internship.link}" target="_blank">${internship.title}</a></p>`;
//             });
//         }
//     });
// });


//document.addEventListener("DOMContentLoaded", () => {
//    document.getElementById("searchForm").addEventListener("submit", async function (event) {
//        event.preventDefault();
//
//        const keyword = document.getElementById("keyword").value;
//        const response = await fetch(`/search?query=${encodeURIComponent(keyword)}`);
//        const data = await response.json();
//
//        let resultsDiv = document.getElementById("results");
//        resultsDiv.innerHTML = "<h2>Internship Results By Your Choice </h2>";
//        if (data.length === 0) {
//            resultsDiv.innerHTML += "<p>No internships found.</p>";
//        } else {
//            data.forEach((internship) => {
//                resultsDiv.innerHTML += `<div>
//                    <h3><a href="${internship.link}" target="_blank">${internship.title}</a></h3>
//                    <p>${internship.description}</p>
//                </div>`;
//            });
//        }
//    });
//});
