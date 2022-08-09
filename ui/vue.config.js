// Importamos webpack-bundle-tracker
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    // La ruta donde estará disponible el bundle de los archivos estáticos 
    // Directorio donde se creará el bundle de archivos estáticos
    outputDir: './dist/',
    // Estable que se compile en tiempo de ejecución.
  runtimeCompiler: true,

    // Los puntos de entrada de nuestra aplicación.
  pages: {
    main: {
        // entry for the page
        entry: 'src/main.js',
        },
      
  },

  chainWebpack: config => {
    config.optimization
    .splitChunks(false)

    config
        .plugin('BundleTracker')
        // El archivo que mapeará los estáticos del proyecto.
    .use(BundleTracker, [{filename: './webpack-stats.json'}])

    config.watchOptions({poll: 1000})

    config.resolve.alias
    .set('__STATIC__', 'static')
    config.output.filename("js/[name].js");
    config.devServer
    .host('0.0.0.0')
    .port(8080)
    .hot('only')
    .https(false)
    .headers({"Access-Control-Allow-Origin": ["\*"]})
  }
};