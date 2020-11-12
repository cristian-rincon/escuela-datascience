-- Ejercicio 1 - El primero | Obtener el primer registro de una tabla.

-- Opción 1
/*
SELECT * FROM platzi.alumnos
FETCH FIRST 1 ROWS ONLY;
*/
-- Opción 2
/*
SELECT * FROM platzi.alumnos
LIMIT 1;
*/

-- Opción 3 - Window Function
/*
SELECT *
FROM (
    -- El OVER() vacío significa toda la tabla
	SELECT ROW_NUMBER() OVER() AS row_id, *
	FROM platzi.alumnos
) AS alumnos_with_row_num
WHERE row_id = 1
*/


-- Reto: Traer las primeras 5 filas usando el metodo
-- Método 1
/*
SELECT * FROM platzi.alumnos
FETCH FIRST 5 ROWS ONLY;
*/
-- Método 2 
/*
SELECT * FROM platzi.alumnos
LIMIT 5;
*/

-- Método 3 - Window Function
/*
SELECT *
FROM (
	SELECT ROW_NUMBER() OVER() AS row_id, *
	FROM platzi.alumnos
) AS alumnos_with_row_num
WHERE row_id BETWEEN 1 AND 5
*/
