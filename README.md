# Proyecto Tareas

Aplicación base para gestionar tareas. Este repositorio se construirá progresivamente para cumplir la entrega de Docker con dos contenedores:

- `app`: API desarrollada con Python y Flask.
- `db`: base de datos PostgreSQL.

## Estado del proyecto

La aplicación base ya expone endpoints para consultar su estado, crear tareas y listar tareas. La persistencia se realiza en PostgreSQL mediante la variable `DATABASE_URL`.

## Próximos componentes

1. API HTTP para crear y consultar tareas. ✅
2. Persistencia en PostgreSQL mediante una conexión interna al servicio `db`. ✅
3. Dockerfile de la aplicación. ✅
4. Docker Compose. ✅
4. Pruebas de comunicación y pipeline de GitHub Actions.

## Ejecutar las pruebas

```bash
python -m pytest
```

## Endpoints iniciales

- `GET /`: información de la API.
- `GET /health`: estado básico de la aplicación.
- `POST /tareas`: crea una tarea con `{"titulo":"..."}`.
- `GET /tareas`: lista las tareas guardadas.
- `PATCH /tareas/<id>/completar`: marca una tarea como completada.

## Ejecutar con Docker

```bash
cp .env.example .env
docker compose build
docker compose up -d
docker compose ps
```

La aplicación quedará disponible en `http://localhost:5000`. La aplicación se conecta a PostgreSQL usando el nombre interno del servicio `db`.
