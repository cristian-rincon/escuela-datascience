-- Ejercicio 12 - Triangulando


-- Left padding - acolchonamiento a la izquierda
				
---SELECT lpad(
-- 'sql', String inicial
-- 15, Cantidad de caracteres que debe tener todo el string
-- 'hola' String de relleno
-- )

SELECT lpad('*', id, '*')
FROM platzi.alumnos
WHERE id < 10
ORDER BY carrera_id
-- Ejercicio: LPAD VS RPAD
SELECT 
lpad(' *|* ', CAST(row_id AS int), 'Soy un relleno que va a la izquierda'), 
rpad(' *|* ', CAST(row_id AS int), 'Soy un relleno que va a la derecha')
FROM (
	SELECT ROW_NUMBER() OVER() AS row_id, *
	FROM platzi.alumnos
) AS alumnos_with_row_id
WHERE row_id <= 50