let chart;

async function loadData() {
    let res = await fetch("/data");
    let data = await res.json();

    document.getElementById("temp").innerText = data.temperature + " °C";
    document.getElementById("humidity").innerText = data.humidity + " %";
    document.getElementById("pressure").innerText = data.pressure + " hPa";
    document.getElementById("status").innerText = data.status;

    let img = document.getElementById("cameraImg");
    img.src = data.image + "?t=" + new Date().getTime();

    let historyList = document.getElementById("historyList");
    historyList.innerHTML = "";

    data.history.forEach(function(item) {
        let li = document.createElement("li");
        li.innerText = item.time + " — " + item.text;
        historyList.appendChild(li);
    });

    updateChart(data.chart_labels, data.chart_temps);
}

function updateChart(labels, temps) {
    let ctx = document.getElementById("tempChart").getContext("2d");

    if (chart) {
        chart.destroy();
    }

    chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Температура",
                    data: temps,
                    borderWidth: 2,
                    tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

loadData();
setInterval(loadData, 5000);