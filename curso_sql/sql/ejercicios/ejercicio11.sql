-- Ejercicio 11 - Todas las uniones

-- LEFT JOIN EXCLUSIVO
SELECT a.nombre,
	   a.apellido,
	   a.carrera_id,
	   c.id,
	   c.carrera
FROM platzi.alumnos AS a
	LEFT JOIN platzi.carreras AS c 
	ON a.carrera_id = c.id -- Elemento de unión entre las tablas
WHERE c.id IS NULL

-- LEFT JOIN NO EXCLUSIVO
SELECT a.nombre,
	   a.apellido,
	   a.carrera_id,
	   c.id,
	   c.carrera
FROM platzi.alumnos AS a
	LEFT JOIN platzi.carreras AS c 
	ON a.carrera_id = c.id -- Elemento de unión entre las tablas
ORDER BY c.id DESC

-- RIGHT JOIN EXCLUSIVO
SELECT a.nombre,
	   a.apellido,
	   a.carrera_id,
	   c.id,
	   c.carrera
FROM platzi.alumnos AS a
	RIGHT JOIN platzi.carreras AS c 
	ON a.carrera_id = c.id -- Elemento de unión entre las tablas
WHERE a.id IS NULL
ORDER BY c.id DESC

-- RIGHT JOIN
SELECT a.nombre,
	   a.apellido,
	   a.carrera_id,
	   c.id,
	   c.carrera
FROM platzi.alumnos AS a
	RIGHT JOIN platzi.carreras AS c 
	ON a.carrera_id = c.id -- Elemento de unión entre las tablas
ORDER BY c.id DESC

-- INNER JOIN -- Lo que ambas tablas tienen en común
SELECT a.nombre,
	   a.apellido,
	   a.carrera_id,
	   c.id,
	   c.carrera
FROM platzi.alumnos AS a
	INNER JOIN platzi.carreras AS c 
	ON a.carrera_id = c.id -- Elemento de unión entre las tablas
ORDER BY c.id DESC

-- FULL OUTER JOIN (EXCLUSIVO) - Diferencia simétrica, lo que está en A o B pero no en ambas

SELECT a.nombre,
	   a.apellido,
	   a.carrera_id,
	   c.id,
	   c.carrera
FROM platzi.alumnos AS a
	FULL OUTER JOIN platzi.carreras AS c 
	ON a.carrera_id = c.id -- Elemento de unión entre las tablas
WHERE a.id IS NULL
	OR c.id IS NULL
ORDER BY a.carrera_id DESC, c.id DESC