// window.onload = function() {
//   cartodb.createVis('map', 'https://joshaddington.cartodb.com/api/v2/viz/ace876d2-c1dd-11e4-a3cf-0e9d821ea90d/viz.json',{
//    center_lat: 40.71953837,
//    center_lon: -73.98426726,
//    });
// };

      function main() {
           cartodb.createVis('map', 'https://joshaddington.cartodb.com/api/v2/viz/ace876d2-c1dd-11e4-a3cf-0e9d821ea90d/viz.json', {
                shareable: true,
                search: true,
                // tiles_loader: true,
                center_lat: 40.71953837,
                center_lon: -73.98426726,
                zoom: 13
           })
          .done(function(vis, layers) {
          // layer 0 is the base layer, layer 1 is cartodb layer
          // setInteraction is disabled by default
          layers[1].setInteraction(true);
          layers[1].on('featureOver', function(e, latlng, pos, data) {
                cartodb.log.log(e, latlng, pos, data);
          });
          // you can get the native map to work with it
          var map = vis.getNativeMap();
          // now, perform any operations you need
          // map.setZoom(12);
          // map.panTo([-73.98426726, 40.71953837]);
        })
        .error(function(err) {
          console.log(err);
        });
      }
      window.onload = main;
