from bokeh.plotting import figure, output_file, show


if __name__ == "__main__":
    output_file('graficado_simple.html')
    fig = figure()

    total_values = int(input('¿Cuántos valores quieres graficar? \n'))
    x_values = list(range(total_values))
    y_values = []

    for x in x_values:
        new_value = int(input(f'Valor y para {x} \n'))
        y_values.append(new_value)

    fig.line(x_values, y_values, line_width=2)
    show(fig