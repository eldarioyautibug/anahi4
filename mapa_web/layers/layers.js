var wms_layers = [];


        var lyr_OpenStreetMap_0 = new ol.layer.Tile({
            'title': 'OpenStreetMap',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
            attributions: ' ',
                url: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
            })
        });
var format_UbicacindelospozospetrolferosenBrasil_1 = new ol.format.GeoJSON();
var features_UbicacindelospozospetrolferosenBrasil_1 = format_UbicacindelospozospetrolferosenBrasil_1.readFeatures(json_UbicacindelospozospetrolferosenBrasil_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_UbicacindelospozospetrolferosenBrasil_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_UbicacindelospozospetrolferosenBrasil_1.addFeatures(features_UbicacindelospozospetrolferosenBrasil_1);
cluster_UbicacindelospozospetrolferosenBrasil_1 = new ol.source.Cluster({
  distance: 30,
  source: jsonSource_UbicacindelospozospetrolferosenBrasil_1
});
var lyr_UbicacindelospozospetrolferosenBrasil_1 = new ol.layer.Vector({
                declutter: false,
                source:cluster_UbicacindelospozospetrolferosenBrasil_1, 
                style: style_UbicacindelospozospetrolferosenBrasil_1,
                popuplayertitle: 'Ubicación de los pozos petrolíferos en Brasil',
                interactive: true,
                title: '<img src="styles/legend/UbicacindelospozospetrolferosenBrasil_1.png" /> Ubicación de los pozos petrolíferos en Brasil'
            });

lyr_OpenStreetMap_0.setVisible(true);lyr_UbicacindelospozospetrolferosenBrasil_1.setVisible(true);
var layersList = [lyr_OpenStreetMap_0,lyr_UbicacindelospozospetrolferosenBrasil_1];
lyr_UbicacindelospozospetrolferosenBrasil_1.set('fieldAliases', {'fid': 'fid', 'LATITUDE_BASE_DD': 'LATITUDE_BASE_DD', 'LONGITUDE_BASE_DD': 'LONGITUDE_BASE_DD', });
lyr_UbicacindelospozospetrolferosenBrasil_1.set('fieldImages', {'fid': '', 'LATITUDE_BASE_DD': '', 'LONGITUDE_BASE_DD': '', });
lyr_UbicacindelospozospetrolferosenBrasil_1.set('fieldLabels', {'fid': 'no label', 'LATITUDE_BASE_DD': 'no label', 'LONGITUDE_BASE_DD': 'no label', });
lyr_UbicacindelospozospetrolferosenBrasil_1.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});