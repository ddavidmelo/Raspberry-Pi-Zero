<html>

<div id="curve_chart"></div>

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

<script type="text/javascript">
  // library
  // https://developers.google.com/chart/interactive/docs/gallery/areachart
  // Load google charts
  google.charts.load('current', {'packages':['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  // Draw the chart and set the chart values
  function drawChart() {
    var data = google.visualization.arrayToDataTable([
        <?php echo file_get_contents("esp8266.private"); ?>
    ]);

    // Optional; add a title and set the width and height of the chart
    var options = {
    title:'Battery Voltage',
    width:750,
    height:400,
    backgroundColor: 'transparent',
    legendTextStyle: {color:'#FFFFFF'},
    hAxis: {textStyle:{color: '#FFFFFF'}},
    vAxis: {textStyle:{color: '#FFFFFF'},baselineColor:'#59f442',gridlines:{color: '#59f442'}}
    };

    // Display the chart inside the <div> element with id="piechart"
    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
    chart.draw(data, options);
  }
</script>

</html>


<style>
body {
    color: white;
    background-color: black;
}

h1 {
    color: green;
}

html {
    overflow: scroll;
    overflow-x: hidden;
}
::-webkit-scrollbar {
    width: 0px;  /* remove scrollbar space */
    background: transparent;  /* optional: just make scrollbar invisible */
}

#curve_chart {
    margin: auto;
    max-width: 750px;
}


</style>

<script>

</script>

