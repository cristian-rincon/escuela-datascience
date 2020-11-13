-- Ejercicio 4 - En mis tiempos | Trabajando con fechas

SELECT *
FROM platzi.alumnos

-- Opción 1 | EXTRACT

SELECT EXTRACT(YEAR FROM fecha_incorporacion) AS anio_incorporacion
FROM platzi.alumnos

-- Opción 2 | DATE_PART

SELECT DATE_PART('YEAR', fecha_incorporacion) AS anio_incorporacion
FROM platzi.alumnos

-- Opción 3 | DATE_PART YEAR MONTH DAY

SELECT DATE_PART('YEAR', fecha_incorporacion) AS anio_incorporacion,
	   DATE_PART('MONTH', fecha_incorporacion) AS mes_incorporacion,
	   DATE_PART('DAY', fecha_incorporacion) AS dia_incorporacion
FROM platzi.alumnos

-- Reto | Extraer horas, minutos y segundos

-- Solución 1

SELECT DATE_PART('HOUR', fecha_incorporacion) AS hora_incorporacion,
	   DATE_PART('MINUTE', fecha_incorporacion) AS minutos_incorporacion,
	   DATE_PART('SECOND', fecha_incorporacion) AS segundos_incorporacion
FROM platzi.alumnos

-- Solución 2

SELECT EXTRACT(HOUR FROM fecha_incorporacion) hora_incorporacion,
	   EXTRACT(MINUTE FROM fecha_incorporacion) AS minutos_incorporacion,
	   EXTRACT(SECOND FROM fecha_incorporacion) AS segundos_incorporacion
FROM platzi.alumnos
