export function visualizarDatos(data) {
  const valores = data.map((d) => ({
    x: d.cuartos,
    y: d.precio,
  }));
  tfvis.render.scatterplot(
    { name: "Cuartos VS Precio" },
    { values: valores },
    {
      xLabel: "Cuartos",
      yLabel: "Precio",
      height: 300,
    }
  );
}
