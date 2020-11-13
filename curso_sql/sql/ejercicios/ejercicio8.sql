-- Ejercicio 7 	| Selectores de rango

-- Opción 1

SELECT *
FROM platzi.alumnos 
WHERE tutor_id IN (1,2,3,4,5)

-- Opción 2

SELECT *
FROM platzi.alumnos 
WHERE tutor_id BETWEEN 1 AND 10

-- Opción 3 - SOLO POSTGRESQL -- Funciones para manejo de rangos

SELECT int4range(10,20) @> 3

SELECT numrange(11.1,22.2) &&  numrange(20.0,30.0)

SELECT UPPER(int8range(15,25))
SELECT LOWER(int8range(15,25))

SELECT int4range(10,20) * int4range(15,25)

SELECT ISEMPTY (numrange(1,5))


--

SELECT *
FROM platzi.alumnos
WHERE int4range(10,20) @> tutor_id

-- Reto: Consultar las intersecciones de la tabla alumnos en el campo tutores

-- Solución:
SELECT 
	numrange(
		(SELECT MIN(tutor_id) FROM platzi.alumnos),
		(SELECT MAX(tutor_id) FROM platzi.alumnos)
	) * numrange(
		(SELECT MIN(carrera_id) FROM platzi.alumnos),
		(SELECT MAX(carrera_id) FROM platzi.alumnos)
	)
	


