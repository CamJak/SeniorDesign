function addData(chart, label, newData) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(newData);
    });
    chart.update();
}

function removeOldestData(chart) {
    chart.data.labels.shift();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
    });
    chart.update();
}

// Update chart with new random value
function updateChartCD(chart) {
    addData(chart, 'May 10', ~~(Math.random()*51));
    removeOldestData(chart);
    setTimeout(function(){updateChartCD(chart)},10000);
}

function createChartCD() {
    // Grab html element to place chart inside
    const cdChart = document.getElementById('connectedDevices');

    // Generate random data
    let randData = [...Array(10)].map(e=>~~(Math.random()*51));
    // Generate dummy labels
    let labels = [...Array(10).keys()].map(i=>'May '+(i+1));

    // Create data object for chart
    let data = {
        labels: labels,
        datasets: [{
            label: 'Connected Devices',
            data: randData
        }]
    };

    // Set config for chart
    let config = {
        type: 'line',
        data: data,
        options: {},
    };

    // Generate chart within html element
    let chartObj = new Chart(cdChart, config);

    // Update chart continually
    updateChartCD(chartObj);
}

function createChartNT() {
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
}

createChartCD();
createChartNT();