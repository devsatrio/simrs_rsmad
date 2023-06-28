$(function () {


var barChartCanvas = $('#barChart').get(0).getContext('2d')
var barChartData = $.extend(true, {}, areaChartData)
var temp0 = areaChartData.datasets[0]
barChartData.datasets[0] = temp0

var barChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    datasetFill: false
}

new Chart(barChartCanvas, {
    type: 'bar',
    data: barChartData,
    options: barChartOptions
})

//-------------
//- PIE CHART -
//-------------
// Get context with jQuery - using jQuery's .get() method.
var pieChartCanvas = $('#pieChart').get(0).getContext('2d')
var pieData = donutData;
var pieOptions = {
    maintainAspectRatio: false,
    responsive: true,
}
//Create pie or douhnut chart
// You can switch between pie and douhnut using the method below.
new Chart(pieChartCanvas, {
    type: 'pie',
    data: pieData,
    options: pieOptions
})
})

function ConvertStringToHex(str) {
    var arr = [];
    for (var i = 0; i < str.length; i++) {
        arr[i] = ("00" + str.charCodeAt(i).toString(16)).slice(-4);
    }
    return "\\u" + arr.join("\\u");
}