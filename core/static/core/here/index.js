(function () {
'use strict';

var app_id = "DemoAppId01082013GAL";
var app_code = "AJKnXv84fjrb0KIHawS0Tg";

var queries = {"query":{"fileName":"./query.json","dataset":"561122bec90a46778e08c366ce201402","id":"ca679fb980d14dc7a97413836d96afa5"}};

const {query} = queries;

// Initialize communication with the platform, to access your own data, change the values below
// https://developer.here.com/documentation/geovisualization/topics/getting-credentials.html

// We recommend you use the CIT environment. Find more details on our platforms below
// https://developer.here.com/documentation/map-tile/common/request-cit-environment-rest.html

const platform = new H.service.Platform({
    app_id,
    app_code,
    useCIT: true,
    useHTTPS: true
});

// Initialize a map
const pixelRatio = devicePixelRatio > 1 ? 2 : 1;
const defaultLayers = platform.createDefaultLayers({tileSize: 256 * pixelRatio});
const map = new H.Map(
    document.getElementsByClassName('dl-map')[0],
    defaultLayers.normal.basenight,
    {pixelRatio}
);
window.addEventListener('resize', function() {
    map.getViewPort().resize();
});

// Make the map interactive
new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
let ui = H.ui.UI.createDefault(map, defaultLayers);
ui.removeControl('mapsettings');

// instantiate Geovisualization service
var service = platform.configure(new H.datalens.Service());
var filterValue = 1;

// get query stats for a reference zoom level
service.fetchQueryStats(query.id, {
    stats: [
        {
            column_stats: {
                count_sum: ['$min', '$max', '$average'],
                lat_avg: ['$min', '$max'],
                lon_avg: ['$min', '$max']
            },
            dynamic: {
                x: '$drop',
                y: '$drop',
                z: 15
            }
        }
    ]
}).then(({stats}) => {

    const columnStats = stats[0].column_stats;

    //set map bounds
    map.setViewBounds(new H.geo.Rect(
        columnStats.lat_avg.$max,
        columnStats.lon_avg.$min,
        columnStats.lat_avg.$min,
        columnStats.lon_avg.$max
    ), false);

    const colorScale = d3.scaleLinear().range([
        'rgba(30, 68, 165, 0.03)',
        'rgba(87, 164, 217, 0.8)',
        'rgba(202, 248, 191, 0.8)'
    ]).domain([0,.5,1]);


    const provider = new H.datalens.QueryTileProvider(
        service, {
            queryId: query.id,
            tileParamNames: {
                x: 'x',
                y: 'y',
                z: 'z'
            }
        }
    );

    const layer = new H.datalens.HeatmapLayer(
        provider, {
             dataToRows: function(data) {
                 return data.rows.filter(function(row) {
                     if (row[5] == filterValue) {
                          return row
                     }
                 });
             },
            rowToTilePoint: function(row) {
                return {
                    x: row[3],
                    y: row[4],
                    value: row[0],
                    count: 1
                };
            },

            // Interpolates between the values for the given
            // reference zoom levels
            bandwidth: [{
                    value: 2,
                    zoom: 4
                },
                {
                    value: 20,
                    zoom: 17
                }
            ],

            // Value per pixel per zoom level and it is
            // derived for other zoom levels
            valueRange: {
                value: columnStats.count_sum.$average,
                zoom: 4
            },
            colorScale
        }
    );

    map.addLayer(layer);

    function timestep() {
        return timestepCtl.getValue();
    }

    // Init legend panel
    const panel = new Panel('Density map');
    const colorLegend = new ColorLegend(colorScale);
    const timestepFilter = new Label();
    const timestepCtl = new Slider(1);
    ui.addControl('panel', panel);

    panel.addChild(timestepFilter);
    panel.addChild(timestepCtl);
    panel.addChild(colorLegend);
    timestepFilter.setHTML(`Time step ${timestepCtl.getValue()}`);

    // Connect ui with layer
    function updatePanel() {
        filterValue = timestepCtl.getValue();
        layer.redraw();
        timestepFilter.setHTML(`Time step: ${filterValue}`);
    }
    timestepCtl.addEventListener('change', updatePanel);

});

}());
