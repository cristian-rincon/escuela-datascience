-- Ejercicio 8 	| Eres lo máximo | Mínimos y Máximos

-- Opción 1 -- Fecha máxima

SELECT fecha_incorporacion
FROM platzi.alumnos
ORDER BY fecha_incorporacion DESC
LIMIT 1

-- Opción 2 -- Fecha máxima

SELECT carrera_id, 
	MAX(fecha_incorporacion)
FROM platzi.alumnos
GROUP BY carrera_id
ORDER BY carrera_id

-- Reto: mínimo nombre alfabético y el mínimo por tutor

-- Solución: 
-- Mínimo nombre alfabético

SELECT nombre
FROM platzi.alumnos
ORDER BY nombre ASC
LIMIT 1

-- Mínimo por tutor

SELECT tutor_id,
	MIN(nombre)
FROM platzi.alumnos
GROUP BY tutor_id
ORDER BY tutor_id