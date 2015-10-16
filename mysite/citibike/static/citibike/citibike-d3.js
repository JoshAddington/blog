var path = d3.geo.path();
var currentSlide = 0;
var w = 800, h = 900;
var stations, availableBikes, timestamps;

svg = d3.select("#mapbox")
            .append("svg")
            .attr("width", w)
            .attr("height", h)
            .style("z-index", 200);

var projection = d3.geo.mercator().center([-73.999, 40.733])
                       .translate([w/2, h/2])
                       .scale([330000]);

var path = d3.geo.path()
                 .projection(projection);

var g = svg.append("g").style("z-index", 200);

function addCommas(nStr){
  nStr += '';
  x = nStr.split('.');
  x1 = x[0];
  x2 = x.length > 1 ? '.' + x[1] : '';
  var rgx = /(\d+)(\d{3})/;
  while (rgx.test(x1)) {
      x1 = x1.replace(rgx, '$1' + ',' + '$2');
  }
  return x1 + x2;
}

d3.json("/static/citibike/api.json", function(error, data){
  stations = data.stations;
  timestamps = data.updates;

  function lat (d) { return projection([d.longitude, d.latitude])[0]; }
  function lon (d) { return projection([d.longitude, d.latitude])[1]; }
  var rScale = d3.scale.sqrt()
                 .domain([1, 60])
                 .range([2, 34]);

  //apending a circle for each station, initial radius set to the radius at first time in timestamps array
  g.selectAll(".ab")
    .data(stations)
    .enter()
    .append("circle")
    .attr("class", "ab")
    .attr("cx", lat)
    .attr("cy", lon)
    .attr("r", function(d){
      if ( d.bikes[0] > 0) { return rScale(d.bikes[0]); }
      else {return 0;}
    })
    .style("opacity", ".35")
    .style("fill", "#30765f")
    .style("z-index", 200);

    g.selectAll(".station")
      .data(stations)
      .enter()
      .append("circle")
      .attr("class", "station")
      .attr("cx", lat)
      .attr("cy", lon)
      .attr("r", 1)
      .attr("opacity", ".7")

      .style("fill", "#041616"); //navy
  //initialize jquery slider, and call move function on slide, pass value to move()
  $( "#slider" ).slider({
    value: 0,
    min: 0,
    max: timestamps.length,
    step: 1,
    slide: function( event, ui ){
      setSlide(ui.value);
    }
  });


  //gets called on every slide, updates size of circle and text element
  function setSlide(i) {
    //updated all of the circles radiussss
    g.selectAll(".ab")
      .data(stations)
      .attr("r", function(d){
        if ( d.bikes[currentSlide] > 0) { return rScale(d.bikes[currentSlide]); }
        else {return 0;}
    });
    //update position of the slider
    $( "#slider" ).slider( "value", i );
    currentSlide = i;

    var currentTime = timestamps[i];

    // Format currentTime with moment
    var time = moment(currentTime).format("dddd, MMMM Do, h:mm [<span>]a[</span>]");

    //updates current time
    d3.select("#current_time")
      .html(time);
  }

  var playInterval;
  var autoRewind = true;

  function getSpeed(){
    var speed = $("input:radio[name=speed]:checked").val();
    if (speed == "fast"){ return 50; }
    else if (speed == "slow") { return 150; }
  }

  // Thank you to the guy who created this - http://jsfiddle.net/amcharts/ZPqhP/
  $('#play').click(
    function(){
      if (playInterval !== undefined){
          clearInterval(playInterval);
          playInterval = undefined;
          $(this).html("Play");
          return;
        }
      $(this).html("Pause");
      playInterval = setInterval(function(){
        currentSlide++;
        if (currentSlide > timestamps.length){
          if (autoRewind){
            currentSlide = 0;
          }
          else {
            clearInterval(playInterval);
            return;
          }
        }
        setSlide(currentSlide);
      }, getSpeed() );
  });

  //hover state for each station
  d3.selectAll(".ab")
    .on("mouseover", function(d) {
          d3.select("#tooltip")
            .style("opacity", 1);
          d3.select(this)
            .style("opacity", ".9")
            .style("stroke", "white")
            .style("stroke-width", "2");
          d3.select("#tooltip")
            .style("left", (d3.event.pageX) - 180 + "px")
            .style("top", (d3.event.pageY) - 175 + "px");
          d3.select('#station-name')
            .text(d.name);
          d3.select('#bikes')
            .text(d.bikes[currentSlide]);
    })
    .on("mouseout", function() {
      //Hide the tooltip
      d3.select("#tooltip")
        .style("opacity", 0);
      d3.select(this)
        // .transition()
        .style("opacity", ".35")
        .style("stroke-width", "0");
  });
});
