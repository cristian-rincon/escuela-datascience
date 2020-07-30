import { visualizarDatos } from "./visualizarDatos.js";
import { crearModelo } from "./crearModelo.js";
import { convertirDatosATensores } from "./convertirDatosATensores.js";
import { entrenarModelo } from "./entrenarModelo.js";

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

export const optimizador = tf.train.adam();
export const function_perdida = tf.losses.meanSquaredError;
export const metricas = ["mse"];

async function run() {
  const data = await getData();
  //console.log(data);
  visualizarDatos(data);
  modelo = crearModelo();
  const tensorData = convertirDatosATensores(data);
  const { entradas, etiquetas } = tensorData;
  entrenarModelo(modelo, entradas, etiquetas);
}

run();
