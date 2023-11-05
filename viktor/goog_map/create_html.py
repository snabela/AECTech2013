def create_html(lon, lat):

    html_text = """<!DOCTYPE html>
    <head>
      <meta charset="utf-8">
      <title>CesiumJS 3D Tiles Simple Demo</title>
      <script src="https://ajax.googleapis.com/ajax/libs/cesiumjs/1.105/Build/Cesium/Cesium.js"></script>
      <link href="https://ajax.googleapis.com/ajax/libs/cesiumjs/1.105/Build/Cesium/Widgets/widgets.css" rel="stylesheet">
    </head>
    <body>
      <div id="cesiumContainer"></div>
      <script>
    
        // Enable simultaneous requests.
        Cesium.RequestScheduler.requestsByServer["tile.googleapis.com:443"] = 18;
    
        // Create the viewer.
        const viewer = new Cesium.Viewer('cesiumContainer', {
          imageryProvider: new Cesium.UrlTemplateImageryProvider({
          url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
          }),
          terrainProvider: new Cesium.ArcGISTiledElevationTerrainProvider({
            url:
              "https://elevation3d.arcgis.com/arcgis/rest/services/WorldElevation3D/Terrain3D/ImageServer",
          }),
          baseLayerPicker: false,
          // https://cesium.com/blog/2018/01/24/cesium-scene-rendering-performance/#enabling-request-render-mode
          requestRenderMode: true,
        });
    
        // Add 3D Tiles tileset
        const tileset = new Cesium.Cesium3DTileset({
          url: "https://tile.googleapis.com/v1/3dtiles/root.json?key=AIzaSyC5aJ5Z0Popy3TXC9qJBp2Au6jNVCcRAiA"
        });
    
        viewer.scene.primitives.add(tileset);
    
        // Point the camera at a specific location
        viewer.scene.camera.setView({
          destination: Cesium.Cartesian3.fromDegrees(""" + str(lon) + "," + str(lat) + """, 250),
          orientation: {
            heading: Cesium.Math.toRadians(45),
            pitch: 0,
            roll: 0
          }
        });
        
      </script>
    </body>
    """

    return html_text