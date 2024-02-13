// Grab html element to place chart inside
const cdChart = document.getElementById('connectedDevices');

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
new Chart(cdChart, config);



// Grab html element to place chart inside
const ntChart = document.getElementById('networkTraffic');

// Generate random data
let randData2 = [...Array(10)].map(e=>(Math.floor(Math.random()*51))+45);
// Generate dummy labels
let labels2 = [...Array(10).keys()].map(i=>'May '+(i+1));

// Create data object for chart
const data2 = {
    labels: labels2,
    datasets: [{
        label: 'Network Traffic (GB)',
        data: randData2
    }]
};

// Set config for chart
const config2 = {
    type: 'bar',
    data: data2,
    options: {
        backgroundColor: 'rgba(231, 32, 37, 0.83)' //red
    },
};

// Generate chart within html element
new Chart(ntChart, config2);