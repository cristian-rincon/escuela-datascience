export function convertirDatosATensores(data) {
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

        //(dato-min) / (max-min)
        const entradasNormalizadas = tensorEntradas
            .sub(entradasMin)
            .div(entradasMax.sub(entradasMin));
        const etiquetasNormalizadas = tensorEtiquetas
            .sub(etiquetasMin)
            .div(etiquetasMax.sub(etiquetasMin));

        return {
            entradas: entradasNormalizadas,
            etiquetas: etiquetasNormalizadas,
            entradasMax,
            entradasMin,
            etiquetasMax,
            etiquetasMin,
        };
    });
}
