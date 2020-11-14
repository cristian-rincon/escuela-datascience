-- Ejercicio 9 	| Egoísta (selfish) | self joins

-- Opción 1 -- 

SELECT a.nombre,
	   a.apellido,
	   t.nombre,
	   t.apellido
FROM	platzi.alumnos AS a
	INNER JOIN platzi.alumnos AS t 
	ON a.tutor_id = t.id

-- Opción 2

SELECT CONCAT(a.nombre,' ',a.apellido) AS alumno,
	   CONCAT(t.nombre,' ',t.apellido) AS tutor
FROM	platzi.alumnos AS a
	INNER JOIN platzi.alumnos AS t 
	ON a.tutor_id = t.id


-- Opción 3 | Cual tutor tiene mas alumnos | TOP 10

SELECT CONCAT(t.nombre,' ',t.apellido) AS tutor,
		COUNT(*) AS alumnos_por_tutor
FROM	platzi.alumnos AS a
	INNER JOIN platzi.alumnos AS t 
	ON a.tutor_id = t.id
GROUP BY tutor
ORDER BY alumnos_por_tutor DESC
LIMIT 10

-- Reto: Promedio de alumnos por tutor

-- Solución: 

SELECT SUM(alumnos_por_tutor) / COUNT(tutor) FROM (
SELECT CONCAT(t.nombre,' ',t.apellido) AS tutor,
			COUNT(*) AS alumnos_por_tutor
	FROM platzi.alumnos AS a
		INNER JOIN platzi.alumnos AS t 
		ON a.tutor_id = t.id
	GROUP BY tutor
) AS alumnos_por_tutor_tabla

	


