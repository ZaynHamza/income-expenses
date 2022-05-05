const searchField = document.querySelector("#searchField");
const appTable = document.querySelector(".app-table");

const tableOutput = document.querySelector(".table-output");
tableOutput.style.display = "none";

const paginationContainer = document.querySelector(".pagination-container");
const noResults = document.querySelector(".no-results");
const tbody = document.querySelector(".table-body")

searchField.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;

    if (searchValue.trim().length > 0) {
        paginationContainer.style.display = "none";
        tbody.innerHTML = "";
        fetch("/income/search-income", {
            body: JSON.stringify({ searchText: searchValue }),
            method: "POST",
          })
            .then((res) => res.json())
            .then((data) => {
              console.log("data", data);
              appTable.style.display = "none";
              tableOutput.style.display = "block";

              if (data.length === 0) {
                noResults.style.display = "block";
                tableOutput.style.display = "none";
              } else { 
                noResults.style.display = "none";
                data.forEach((item) => {
                  tbody.innerHTML += `
                    <tr>
                      <td>${ item.amount }</td>
                      <td>${ item.source }</td>
                      <td>${ item.description }</td>
                      <td>${ item.date }</td>
                    </tr>`;
                });
              }
            });
    } else {
        tableOutput.style.display = "none";
        paginationContainer.style.display = "block";
        appTable.style.display = "block";
    }
}); 