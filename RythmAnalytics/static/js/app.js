function buildSalesChart() {
var url = "/album_sales";
d3.json(url).then(function(response) 
{
    console.log(response);
    var dataChart = [response];
    console.log(dataChart[0].x);
    // console.log(data[1]);
    var ctx = document.getElementById('plotSalesPanel').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: dataChart[0].x,
        datasets: [{
            label: 'Volume of Sales',
            data: dataChart[0].y,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
  
}
)}

function buildCriticChart() {
      var url = "/total_critic";
      d3.json(url).then(function(response) {
        console.log("critic"+response);
        var data_crtic = [response];
        var layout = {
          autosize: false,
          width:500,
          height:350,
          title: "Critic Rating Analysis",
          margin: {
            l: 50,
            r: 50,
            b: 100,
            t: 100,
            pad: 4
          },
          paper_bgcolor: '##87CEEB',
          plot_bgcolor: '#c7c7c7',
          xaxis: {
            title: "Album"
          },
          yaxis: {
            title: "Critic Rating"
          }
        };
        Plotly.newPlot("plotCriticsPanel", data_crtic, layout);
      });
    }
    function buildDebutArtistChart() {
          var url = "/debut_artists";
          d3.json(url).then(function(response) {
            console.log(response);
            var dataArtist = [response];
            var ctx = document.getElementById('plotArtistPanel');
            var myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: dataArtist[0].x,
                datasets: [{
                    label: 'Volume of Sales',
                    data: dataArtist[0].y,
                    backgroundColor: [
                        'rgba(255, 140, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ]
                    
                }]
            },
            options: {
                title: {
                  display: true,
                  text: 'Volume of Sales by Artist'
                }
              }
        });
    });
}
        //     var layout = {
        //     autosize: false,
        //     width:500,
        //     height:350,
        //     title: "Album Sales by Artist",
        //     margin: {
        //         l: 50,
        //         r: 50,
        //         b: 100,
        //         t: 100,
        //         pad: 4
        //       },
        //     paper_bgcolor: '##87CEEB',
        //     plot_bgcolor: '#c7c7c7',
        //     xaxis: {
        //         title: "Album"
        //       },
        //     yaxis: {
        //         title: "Sales"
        //       }
        //     };
        //     Plotly.newPlot("plotArtistPanel", dataArtist, layout);
        //   });
         
buildCriticChart();
buildSalesChart();
buildDebutArtistChart();
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
    // const firstSample = sampleNames[0]