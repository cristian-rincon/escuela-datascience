-- Ejercicio 2 - El segundo más alto | Segunda mayor colegiatura

-- Opción 1
/*
SELECT DISTINCT colegiatura
FROM platzi.alumnos AS a1
WHERE 2 = (
	SELECT COUNT ( DISTINCT colegiatura)
	FROM platzi.alumnos AS a2
	WHERE a1.colegiatura <= a2.colegiatura
)
*/
-- Opción 2
/*
SELECT DISTINCT colegiatura, tutor_id
FROM platzi.alumnos
WHERE tutor_id = 20
ORDER BY colegiatura DESC
LIMIT 1 OFFSET 1
*/


-- Opción 3
/*
SELECT *
FROM platzi.alumnos AS datos_alumnos
INNER JOIN (
	SELECT DISTINCT colegiatura
	FROM platzi.alumnos
	WHERE tutor_id = 20
	ORDER BY colegiatura DESC
	LIMIT 1 OFFSET 1
) AS segunda_mayor_colegiatura
ON datos_alumnos.colegiatura = segunda_mayor_colegiatura.colegiatura 
*/

-- Opción 4
/*
SELECT *
FROM platzi.alumnos AS datos_alumnos
WHERE colegiatura = (
	SELECT DISTINCT colegiatura
	FROM platzi.alumnos
	WHERE tutor_id = 20
	ORDER BY colegiatura DESC
	LIMIT 1 OFFSET 1
)
*/
------------------------------------------------------------------------
-- Reto: 
-- Traer la tabla platzi alumnos, solamente la segunda mitad de la tabla
------------------------------------------------------------------------
-- Opción de solución 1
/*
SELECT *
FROM platzi.alumnos
LIMIT 500
OFFSET 500
*/
-- Opción de solución 2
/*
SELECT * FROM platzi.alumnos AS datos_alumnos
WHERE id >= (
	SELECT COUNT(*)/2
	FROM platzi.alumnos
)
*/
-- Opción de solución 3
/*
SELECT * FROM platzi.alumnos
OFFSET 500 ROWS
FETCH FIRST 500 ROWS ONLY
*/

-- Propuesta del profesor

SELECT ROW_NUMBER() OVER() AS row_id, *
FROM platzi.alumnos
OFFSET(
	SELECT COUNT(*)/2
	FROM platzi.alumnos
)

