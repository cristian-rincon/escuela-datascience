var stopTraining;

const url_data =
  "https://gist.githubusercontent.com/cristian-rincon/05010fd97a3c39e5b0b9f90f6ce17a98/raw/1734e7af030777bb4b66473e4c3e6447401863c1/data.json";

async function getData() {
  const datosCasasR = await fetch(url_data);
  const datosCasas = await datosCasasR.json();
  const datosLimpios = datosCasas
    .map((casa) => ({
      precio: casa.Precio,
      cuartos: casa.NumeroDeCuartosPromedio,
    }))
    .filter((casa) => casa.precio != null && casa.cuartos != null);

  return datosLimpios;
}

//mostrar curva de inferencia()
async function verCurvaInferencia() {
  var data = await getData();
  var tensorData = await convertirDatosATensores(data);

  const { entradasMax, entradasMin, etiquetasMin, etiquetasMax } = tensorData;

  const [xs, preds] = tf.tidy(() => {
    const xs = tf.linspace(0, 1, 100);
    const preds = modelo.predict(xs.reshape([100, 1]));

    const desnormX = xs.mul(entradasMax.sub(entradasMin)).add(entradasMin);

    const desnormY = preds
      .mul(etiquetasMax.sub(etiquetasMin))
      .add(etiquetasMin);

    return [desnormX.dataSync(), desnormY.dataSync()];
  });

  const puntosPrediccion = Array.from(xs).map((val, i) => {
    return { x: val, y: preds[i] };
  });

  const puntosOriginales = data.map((d) => ({
    x: d.cuartos,
    y: d.precio,
  }));

  tfvis.render.scatterplot(
    { name: "Prediccion vs Originales" },
    {
      values: [puntosOriginales, puntosPrediccion],
      series: ["originales", "predicciones"],
    },
    {
      xLabel: "Cuartos",
      yLabel: "Precio",
      height: 300,
    }
  );
}

async function cargarModelo() {
  const uploadJSONInput = document.getElementById("upload-json");
  const uploadWeightsInput = document.getElementById("upload-weights");

  modelo = await tf.loadLayersModel(
    tf.io.browserFiles([uploadJSONInput.files[0], uploadWeightsInput.files[0]])
  );
  console.log("Modelo Cargado");
}

function visualizarDatos(data) {
  const valores = data.map((d) => ({
    x: d.cuartos,
    y: d.precio,
  }));

  tfvis.render.scatterplot(
    { name: "Cuartos vs Precio" },
    { values: valores },
    {
      xLabel: "Cuartos",
      yLabel: "Precio",
      height: 300,
    }
  );
}

function crearModelo() {
  const modelo = tf.sequential();

  // agregar capa oculta que va a recibir 1 dato
  modelo.add(tf.layers.dense({ inputShape: [1], units: 1, useBias: true }));

  // agregar una capa de salida que va a tener 1 sola unidad
  modelo.add(tf.layers.dense({ units: 1, useBias: true }));

  return modelo;
}

const optimizador = tf.train.adam();
const funcion_perdida = tf.losses.meanSquaredError;
const metricas = ["mse"];

async function entrenarModelo(model, inputs, labels) {
  // Prepare the model for training.
  model.compile({
    optimizer: optimizador,
    loss: funcion_perdida,
    metrics: metricas,
  });

  const surface = { name: "show.history live", tab: "Training" };
  const tamanioBatch = 28;
  const epochs = 50;
  const history = [];

  return await model.fit(inputs, labels, {
    tamanioBatch,
    epochs,
    shuffle: true,
    callbacks: {
      onEpochEnd: (epoch, log) => {
        history.push(log);
        tfvis.show.history(surface, history, ["loss", "mse"]);

        if (stopTraining) {
          modelo.stopTraining = true;
        }
      },
    },
  });
}

async function guardarModelo() {
  const saveResult = await modelo.save("downloads://modelo-regresion");
}

function convertirDatosATensores(data) {
  return tf.tidy(() => {
    tf.util.shuffle(data);

    const entradas = data.map((d) => d.cuartos);
    const etiquetas = data.map((d) => d.precio);

    const tensorEntradas = tf.tensor2d(entradas, [entradas.length, 1]);
    const tensorEtiquetas = tf.tensor2d(etiquetas, [etiquetas.length, 1]);

    const entradasMax = tensorEntradas.max();
    const entradasMin = tensorEntradas.min();
    const etiquetasMax = tensorEtiquetas.max();
    const etiquetasMin = tensorEtiquetas.min();

    // (dato -min) / (max-min)
    const entradasNormalizadas = tensorEntradas
      .sub(entradasMin)
      .div(entradasMax.sub(entradasMin));
    const etiquetasNormalizadas = tensorEtiquetas
      .sub(etiquetasMin)
      .div(etiquetasMax.sub(etiquetasMin));

    return {
      entradas: entradasNormalizadas,
      etiquetas: etiquetasNormalizadas,
      // Return the min/max bounds so we can use them later.
      entradasMax,
      entradasMin,
      etiquetasMax,
      etiquetasMin,
    };
  });
}

var modelo;
async function run() {
  const data = await getData();

  visualizarDatos(data);

  modelo = crearModelo();

  const tensorData = convertirDatosATensores(data);
  const { entradas, etiquetas } = tensorData;

  await entrenarModelo(modelo, entradas, etiquetas);
}

run();


