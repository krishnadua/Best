<!DOCTYPE html>
<html>
<head>
    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_33106abd0bf713f3313a1e20bd48e280 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            </style>
        
</head>
<body>
    
    
            <div class="folium-map" id="map_33106abd0bf713f3313a1e20bd48e280" ></div>
        
</body>
<script>
    
    
            var map_33106abd0bf713f3313a1e20bd48e280 = L.map(
                "map_33106abd0bf713f3313a1e20bd48e280",
                {
                    center: [22.3511148, 78.6677428],
                    crs: L.CRS.EPSG3857,
                    zoom: 9,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_6fc75d1aa8455c337cb390b39db02d19 = L.tileLayer(
                "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors", "detectRetina": false, "maxNativeZoom": 19, "maxZoom": 19, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            );
        
    
            tile_layer_6fc75d1aa8455c337cb390b39db02d19.addTo(map_33106abd0bf713f3313a1e20bd48e280);
        
    
            var marker_9f598f5d5c998e4f9fbf4ff865422b4c = L.marker(
                [22.3511148, 78.6677428],
                {}
            ).addTo(map_33106abd0bf713f3313a1e20bd48e280);
        
    
        var popup_a8a9711ff5ca7e16b295d2ff9224db4c = L.popup({"maxWidth": "100%"});

        
            
                var html_7740d1a4d1c5d4a08792d35ac9087e98 = $(`<div id="html_7740d1a4d1c5d4a08792d35ac9087e98" style="width: 100.0%; height: 100.0%;">India</div>`)[0];
                popup_a8a9711ff5ca7e16b295d2ff9224db4c.setContent(html_7740d1a4d1c5d4a08792d35ac9087e98);
            
        

        marker_9f598f5d5c998e4f9fbf4ff865422b4c.bindPopup(popup_a8a9711ff5ca7e16b295d2ff9224db4c)
        ;

        
    
</script>
</html>