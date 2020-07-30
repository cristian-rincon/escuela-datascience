export function crearModelo() {
    const modelo = tf.sequential();

    modelo.add(
        tf.layers.dense({
            inputShape: [1],
            units: 1,
            useBias: true,
        })
    );
    modelo.add(
        tf.layers.dense({
            units: 1,
            useBias: true,
        })
    );
    return modelo;
}
