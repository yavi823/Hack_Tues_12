let data = {
    temp: 28,
    humidity: 45,
    soil: 20,
    pressure: 1008
};

document.getElementById("temp").innerText = data.temp + " °C";
document.getElementById("humidity").innerText = data.humidity + " %";
document.getElementById("soil").innerText = data.soil + " %";
document.getElementById("pressure").innerText = data.pressure + " hPa";

let statusText = "";

if (data.soil < 30) {
    statusText = "Растението има нужда от вода";
} else if (data.temp > 30) {
    statusText = "Прекалено горещо";
} else {
    statusText = "Растението е в добро състояние";
}

document.getElementById("status").innerText = statusText;

let history = [
    "Поливане - 09:00",
    "Ниска влажност - 11:30",
    "Температура висока - 14:00"
];

let list = document.getElementById("historyList");

history.forEach(function(item) {
    let li = document.createElement("li");
    li.innerText = item;
    list.appendChild(li);
});

let ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["10:00", "11:00", "12:00", "13:00"],
        datasets: [{
            label: 'Температура',
            data: [22, 24, 27, 28],
            borderWidth: 2
        }]
    }
});
