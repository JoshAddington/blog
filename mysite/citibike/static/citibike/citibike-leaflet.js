var map = new L.Map("mapbox", {zoomControl: false, center: [40.733, -73.99100056], zoom: 13})
    .addLayer(new L.TileLayer("http://{s}.tiles.mapbox.com/v4/joshaddington.l8aja3lb/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoiam9zaGFkZGluZ3RvbiIsImEiOiI3YkZxMFJnIn0.iVv6sgsySboP3BaH8KqGbA", {
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
}));

map.keyboard.disable();
map.dragging.disable();
map.touchZoom.disable();
map.doubleClickZoom.disable();
map.scrollWheelZoom.disable();

var svg = d3.select(map.getPanes().overlayPane).append("svg"),
    g = svg.append("g").attr("class", "leaflet-zoom-hide");

var width = 800;
var height = 900;
d3.json("/api/citibike/boroughs", function(error, collection) {

    var transform = d3.geo.transform({point: projectPoint}),
      path = d3.geo.path().projection(transform);

    var feature = g.selectAll('path')
        .data(collection.features)
        .enter().append('path');

    map.on('viewreset', reset);
    reset();

    // fit the SVG element to leaflet's map layer
    function reset() {

        bounds = path.bounds(collection);

        var topLeft = bounds[0],
        bottomRight = bounds[1];

        svg.attr("width", bottomRight[0] - topLeft[0])
            .attr("height", bottomRight[1] - topLeft[1])
            .style("left", topLeft[0] + "px")
            .style("top", topLeft[1] + "px");

        g.attr("transform", "translate(" + -topLeft[0] + ","
                                     + -topLeft[1] + ")");

        // initialize the path data
        feature.attr("d", path)
            .attr('stroke', 'grey')
            .attr('fill','none');
  }

    // Use Leaflet to implement a D3 geometric transformation.
  function projectPoint(x, y) {
    var point = map.latLngToLayerPoint(new L.LatLng(y, x));
    this.stream.point(point.x, point.y);
  }
});
