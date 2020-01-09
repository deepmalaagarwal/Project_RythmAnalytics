function buildSalesChart(sample) {
var url = "/album_sales/"+sample;
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
            label: 'Top 5 Album Sales for '+sample,
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

function buildCriticChart(sample) {
      var url = "/total_critic/"+sample;
      d3.json(url).then(function(response) {
        console.log("critic"+response);
        var data_crtic = [response];
        var layout = {
          autosize: false,
          width:500,
          height:350,
          title: "Critic Rating Analysis for "+sample,
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
    function buildDebutArtistChart(sample) {
          var url = "/debut_artists/"+sample;
          d3.json(url).then(function(response) {
            console.log(response);
            var dataArtist = [response];
            var ctx = document.getElementById('plotArtistPanel');
            var myChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: dataArtist[0].x,
                datasets: [{
                    label: 'Top 5 Artist for '+sample,
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

    function buildLyricsWordChart(sample) {
        var url = "/Lyrics_word_count/"+sample;
        d3.json(url).then(function(response) 
        {
            console.log(response);
            var dataLyricsChart = [response];
            console.log(dataLyricsChart[0].x);
            // console.log(data[1]);
            var ctx = document.getElementById('plotLyricsPanel').getContext('2d');
            var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: dataLyricsChart[0].x,
                datasets: [{
                    label: 'Word Count in Lyrics of Popular songs of '+sample,
                    data: dataLyricsChart[0].y,
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
        }  );
        
        });
    }

function init() {
//   Grab a reference to the dropdown select element
  console.log("i am in init");
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then(function(response) {
    
    console.log(response)
    var lyear = [response]
    lyear[0].Year.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = lyear[0].Year[0];
    buildCriticChart(firstSample);
    buildSalesChart(firstSample);
    buildDebutArtistChart(firstSample);
    buildLyricsWordChart(firstSample);
    console.log(firstSample)
    
});
   
}
init();
function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    buildLyricsWordChart(newSample);
    buildDebutArtistChart(newSample);
    buildSalesChart(newSample);
    buildCriticChart(newSample);
  }
