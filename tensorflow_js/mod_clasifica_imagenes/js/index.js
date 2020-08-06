let model;

const webcamElement = document.getElementById("webcam");
const classifier = knnClassifier.create();

const imgEl = document.getElementById("img");
const descEl = document.getElementById("descripcion_imagen");
var count = 0;
var net;
var webcam;
async function app() {
  console.log("Cargando modelo de identificacion de imagenes");
  net = await mobilenet.load();
  console.log("Carga terminada");
  //clasificamos la imagen de carga
  const result = await net.classify(imgEl);
  console.log(result);
  descEl.innerHTML = JSON.stringify(result);

  //obtenemos datos del webcam
  webcam = await tf.data.webcam(webcamElement);
  //y los vamos procesando
  while (true) {
    const img = await webcam.capture();

    const result = await net.classify(img);

    const activation = net.infer(img, "conv_preds");
    var result2;
    try {
      result2 = await classifier.predictClass(activation);
    } catch (error) {
      result2 = {};
    }

    document.getElementById("descripcion_video").innerText = `
      prediction: ${result[0].className}\n
      probability: ${result[0].probability}
    `;

    // Dispose the tensor to release the memory.
    img.dispose();

    // Give some breathing room by waiting for the next animation frame to
    // fire.
    await tf.nextFrame();
  }
}

img.onload = async function () {
  try {
    result = await net.classify(img);
    descEl.innerHTML = JSON.stringify(result);
  } catch (error) {}
};

async function cambiarImagen() {
  count = count + 1;
  imgEl.src = "https://picsum.photos/200/300?random=" + count;
  descEl.innerHTML = "";
}

app();
