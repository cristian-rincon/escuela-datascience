let net;

const imgElement = document.getElementById("img");
const descElement = document.getElementById("descripcion_imagen");
const webcamElement = document.getElementById("webcam");
const descElementVideo = document.getElementById("descripcion_video");

function utils(number) {
  return Math.floor(number);
}

async function app() {
  net = await mobilenet.load();
  //const result = await net.classify(imgElement);
  //console.log(result);
  displayImagePrediction();

  const webcam = await tf.data.webcam(webcamElement);
  while (true) {
    const img = await webcam.capture();
    const result = await net.classify(img);
    descElementVideo.innerHTML = ` Predicción: ${
      result[0].className
    }<br> Probabilidad: ${utils(result[0].probability * 100)} %`;
  }
}

imgElement.onload = async () => {
  displayImagePrediction();
};

async function displayImagePrediction() {
  try {
    const result = await net.classify(imgElement);
    descElement.innerHTML = ` Predicción: ${
      result[0].className
    }<br> Probabilidad: ${utils(result[0].probability * 100)} %`;
  } catch (error) {
    console.error(error);
  }
}
var count = 0;
async function cambiarImagen() {
  count = count + 1;
  imgElement.src = `https://picsum.photos/200/300?random=${count}`;
}

app();
