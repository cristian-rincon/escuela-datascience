import { optimizador, function_perdida, metricas } from "./main.js";
export async function entrenarModelo(model, inputs, labels) {
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
