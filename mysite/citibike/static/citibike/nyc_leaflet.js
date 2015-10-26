var map = L.mapbox.map('mapbox', 'joshaddington.l8aja3lb', {
    accessToken: 'pk.eyJ1Ijoiam9zaGFkZGluZ3RvbiIsImEiOiI3YkZxMFJnIn0.iVv6sgsySboP3BaH8KqGbA',
    scrollWheelZoom: false,
    zoomControl: false
}).setView([40.733, -73.999], 13);

map.dragging.disable();
map.touchZoom.disable();
map.doubleClickZoom.disable();
map.scrollWheelZoom.disable();
map.keyboard.disable();


var svg = d3.select(map.getPanes().overlayPane).append("svg"),
    g = svg.append("g").attr("class", "leaflet-zoom-hide");

d3.json("/api/citibike/boroughs", function(collection){
    var transform = d3.geo.transform({point: projectPoint}),
        path = d3.geo.path().projection(transform);

    var feature = g.selectAll('path')
        .data(collection.features)
        .enter().append('path')
        .attr("class", "nyc_map");

    map.on('viewreset', reset);
    reset();

    function reset(){
        bounds = path.bounds(collection);

        var topLeft = bounds[0],
        bottomRight = bounds[1];

        svg.attr("width", bottomRight[0] - topLeft[0])
            .attr("height", bottomRight[1] - topLeft[1])
            .style("left", topLeft[0] + "px")
            .style("top", topLeft[1] + "px");

        g.attr("transform", "translate(" + -topLeft[0] +","
                                    + -topLeft[1] + ")");

        feature.attr("d", path)
            .attr("stroke", "grey")
            .attr("fill", "none");
    }

    function projectPoint(x, y){
        var point = map.latLngToLayerPoint(new L.LatLng(y, x));
        this.stream.point(point.x, point.y);
    }
});
