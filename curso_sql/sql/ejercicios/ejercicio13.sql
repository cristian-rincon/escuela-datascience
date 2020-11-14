-- Ejercicio 13 - Generando rangos POSTGRESQL

SELECT *
-- FROM generate_series(1,10)
-- FROM generate_series(15,1, -2)
-- FROM generate_series(3,4)
FROM generate_series(4,4)



SELECT current_date + s.a AS dates
FROM generate_series(0,14,7) AS s(a)


SELECT *
FROM generate_series('2020-09-01 00:00:00'::timestamp, '2020-09-04 12:00:00', '10 hours')


SELECT a.id,
		a.nombre,
		a.apellido,
		a.carrera_id,
		s.a
FROM platzi.alumnos AS a
	INNER JOIN generate_series(0,10) AS s(a)
	ON s.a = a.carrera_id
ORDER BY a.carrera_id


-- Reto: generar un triángulo a partir de un rango usando generate_series y l o r pad

-- Solucion:

SELECT lpad('\', id, '/') 
FROM generate_series(0,50) as id