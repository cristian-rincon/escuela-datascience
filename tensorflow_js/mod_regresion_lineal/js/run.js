import visualizarDatos from "./visualizarDatos.js";
import { getData } from "./main";
export async function run() {
    const data = await getData();
    //console.log(data);
    visualizarDatos(data);
}
