// function buildMetadata(sample) {

//   // @TODO: Complete the following function that builds the metadata panel

//   // Use `d3.json` to fetch the metadata for a sample
//     // Use d3 to select the panel with id of `#sample-metadata`

//     // Use `.html("") to clear any existing metadata

//     // Use `Object.entries` to add each key and value pair to the panel
//     // Hint: Inside the loop, you will need to use d3 to append new
//     // tags for each key-value in the metadata.

//     // BONUS: Build the Gauge Chart
//     // buildGauge(data.WFREQ);
// }

function buildSalesChart() {

  var url = "/album_sales";
  d3.json(url).then(function(response) {
    console.log(response);
    var data = [response];
    var layout = {
      title: "Sales",
      xaxis: {
        title: "Album"
      },
      yaxis: {
        title: "Sales"
      }
    };
    Plotly.newPlot("plot", data, layout);
  });
}  

function buildDebutArtistChart() {

  var url = "/debut_artists";
  d3.json(url).then(function(response) {
    console.log(response);
    var data = [response];
    var layout = {
      title: "Sales",
      xaxis: {
        title: "Album"
      },
      yaxis: {
        title: "Sales"
      }
    };
    Plotly.newPlot("plot_artists", data, layout);
  });
}  
//function init() {
  // Grab a reference to the dropdown select element
  // var selector = d3.select("#selDataset");

  // // Use the list of sample names to populate the select options
  // d3.json("/album_sales").then((sampleNames) => {
  //   sampleNames.forEach((sample) => {
  //     selector
  //       .append("option")
  //       .text(sample)
  //       .property("value", sample);
  //   });

    // Use the first sample from the list to build the initial plots
    // const firstSample = sampleNames[0];
  buildSalesChart();
  buildDebutArtistChart();