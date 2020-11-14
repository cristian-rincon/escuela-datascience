-- Ejercicio 10	| Resolviendo diferencias | Elementos que están en una tabla, pero no en la otra

SELECT * FROM platzi.carreras

-- Opción 1 -- 

SELECT carrera_id, COUNT(*) AS cuenta
FROM platzi.alumnos
GROUP BY carrera_id
ORDER BY cuenta DESC

/*
DELETE FROM platzi.carreras
WHERE id BETWEEN 30 AND 40
*/
-- Exclusive LEFT JOIN
SELECT a.nombre,
	   a.apellido,
	   a.carrera_id,
	   c.id,
	   c.carrera
FROM platzi.alumnos AS a
	LEFT JOIN platzi.carreras AS c
	ON a.carrera_id = c.id
WHERE c.id IS NULL
ORDER BY a.carrera_id

-- Reto:Hacer un LEFT JOIN que traiga todo lo que esté en alumnos

-- Solución: 
