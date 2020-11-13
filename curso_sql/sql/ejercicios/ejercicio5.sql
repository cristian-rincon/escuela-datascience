-- Ejercicio 5 - Seleccionar por año | Trabajando con fechas 2

-- QUERY Base
SELECT *
FROM platzi.alumnos

-- Opción 1 | EXTRACT

SELECT *
FROM platzi.alumnos
WHERE (EXTRACT(YEAR FROM fecha_incorporacion)) = 2018

-- Opción 2 | DATE_PART

SELECT *
FROM platzi.alumnos
WHERE (DATE_PART('YEAR', fecha_incorporacion)) = 2018

-- Opción 3 | DATE_PART

SELECT *
FROM (
	SELECT * ,
		DATE_PART('YEAR', fecha_incorporacion) AS anio_incorporacion
	FROM platzi.alumnos
) AS alumnos_con_anio
WHERE anio_incorporacion = 2020

-- Reto: Traer las incorporaciones de mayo de 2018

-- Solución 1: 

SELECT *
FROM platzi.alumnos
WHERE (DATE_PART('YEAR', fecha_incorporacion)) = 2018 
AND (DATE_PART('MONTH', fecha_incorporacion)) = 05


-- Solución 2: 

SELECT *
FROM platzi.alumnos
WHERE (EXTRACT(YEAR FROM fecha_incorporacion)) = 2018 
AND (EXTRACT(MONTH FROM fecha_incorporacion)) = 05
