import { visualizarDatos } from "./visualizarDatos.js";
import { crearModelo } from "./crearModelo.js";
import { convertirDatosATensores } from "./convertirDatosATensores.js";

var modelo;

const url_data =
  "https://gist.githubusercontent.com/cristian-rincon/05010fd97a3c39e5b0b9f90f6ce17a98/raw/1734e7af030777bb4b66473e4c3e6447401863c1/data.json";

async function getData() {
  const datosCasasR = await fetch(url_data);
  const datosCasas = await datosCasasR.json();
  var datosLimpios = datosCasas.map((casa) => ({
    precio: casa.Precio,
    cuartos: casa.NumeroDeCuartosPromedio,
  }));
  datosLimpios = datosLimpios.filter(
    (casa) => casa.precio != null && casa.cuartos != null
  );
  return datosLimpios;
}

const optimizador = tf.train.adam();
const function_perdida = tf.losses.meanSquaredError;
const metricas = ["mse"];

async function entrenarModelo(model, inputs, labels) {
  model.compile({
    optimizer: optimizador,
    loss: function_perdida,
    metrics: metricas,
  });

  const surface = { name: "show.history live", tab: "Training" };
  const tamanoBatch = 28;
  const epochs = 50;
  const history = [];

  return await model.fit(inputs, labels, {
    tamanoBatch,
    epochs,
    shuffle: true,
    callbacks: tfvis.show.fitCallbacks(
      { name: "Training Performance" },
      ["loss", "mse"],
      { height: 200, callbacks: ["onEpochEnd"] }
    ),
  });
}

async function run() {
  const data = await getData();
  //console.log(data);
  visualizarDatos(data);
  const modelo = crearModelo();
  const tensorData = convertirDatosATensores(data);
  const { entradas, etiquetas } = tensorData;
  entrenarModelo(modelo, entradas, etiquetas);
}

run();
