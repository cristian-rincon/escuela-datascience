-- Ejercicio 3 - Seleccionar de un set de opciones
-- Opción 1
/*
SELECT * 
FROM (
	SELECT ROW_NUMBER() OVER() AS row_id, *
	FROM platzi.alumnos
) AS alumnos_with_row_num
WHERE row_id IN (1,5,10,12,15,20)
*/

-- Opción 2
/*
SELECT *
FROM platzi.alumnos
WHERE id IN (
	SELECT id
	FROM platzi.alumnos
	WHERE tutor_id = 30
)
*/
-- Reto: traer los datos que no se encuentren en la query que se retornó en la opción 2
-- Solución 
SELECT *
FROM platzi.alumnos
WHERE id NOT IN (
	SELECT id
	FROM platzi.alumnos
	WHERE tutor_id = 30
)