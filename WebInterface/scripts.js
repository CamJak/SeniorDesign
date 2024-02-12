// Grab html element to place chart inside
const ctx = document.getElementById('myChart');

// Generate random data
let randData = [...Array(10)].map(e=>Math.floor(Math.random()*51));
// Generate dummy labels
labels = [...Array(10).keys()].map(i=>'May '+(i+1));

// Create data object for chart
const data = {
    labels: labels,
    datasets: [{
        label: 'Connected Devices',
        data: randData
    }]
};

// Set config for chart
const config = {
    type: 'line',
    data: data,
    options: {},
};

// Generate chart within html element
new Chart(ctx, config);