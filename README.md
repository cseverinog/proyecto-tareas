# Proyecto Tareas

Aplicación base para gestionar tareas. Este repositorio se construirá progresivamente para cumplir la entrega de Docker con dos contenedores:

- `app`: API desarrollada con Python y Flask.
- `db`: base de datos PostgreSQL.

## Estado del proyecto

Actualmente se está construyendo la aplicación base antes de agregar Docker Compose, persistencia y CI.

## Próximos componentes

1. API HTTP para crear y consultar tareas.
2. Persistencia en PostgreSQL mediante una conexión interna al servicio `db`.
3. Dockerfile y `docker-compose.yml`.
4. Pruebas de comunicación y pipeline de GitHub Actions.
