# Proyecto Tareas

Aplicación para gestionar tareas mediante una API desarrollada con Python y Flask, conectada a PostgreSQL. Docker Compose ejecuta ambos componentes como servicios independientes dentro de una red Docker propia.

## Servicios

- `app`: API Flask que recibe las solicitudes HTTP y administra las tareas.
- `db`: PostgreSQL 16.6, encargado de almacenar las tareas.

La aplicación se conecta a PostgreSQL mediante el nombre interno del servicio `db`, no mediante `localhost` ni una dirección IP fija.

## Estructura del repositorio

```text
proyecto-tareas/
├── app/
│   ├── Dockerfile
│   ├── app.py
│   └── database.py
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

PostgreSQL utiliza directamente la imagen oficial `postgres:16.6-alpine`, por lo que no necesita una carpeta propia dentro del repositorio.

## Requisitos

- Docker Desktop.
- Docker Compose v2.
- Git.

## Configuración

Crear el archivo local de variables de entorno:

```bash
cp .env.example .env
```

El archivo `.env` contiene la configuración local y no se sube al repositorio. El archivo `.env.example` documenta las variables necesarias sin incluir credenciales reales.

## Ejecutar con Docker

Construir las imágenes:

```bash
docker compose build
```

Levantar los servicios:

```bash
docker compose up -d
```

Consultar el estado:

```bash
docker compose ps
```

La aplicación estará disponible en `http://localhost:5000`. Si ese puerto está ocupado, cambia `APP_PORT` en `.env`, por ejemplo a `5001`.

## Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Información general de la API |
| GET | `/health` | Verifica que la aplicación esté activa |
| POST | `/tareas` | Crea una tarea |
| GET | `/tareas` | Lista las tareas guardadas |
| PATCH | `/tareas/<id>/completar` | Marca una tarea como completada |

## Prueba de comunicación entre contenedores

La aplicación Flask se conecta a PostgreSQL usando el nombre de servicio `db`, definido en `docker-compose.yml`. Docker resuelve ese nombre dentro de la red `tareas-net`.

Crear una tarea:

```bash
curl -X POST http://localhost:5000/tareas \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Prueba de comunicación"}'
```

Consultar las tareas:

```bash
curl http://localhost:5000/tareas
```

La primera operación guarda la tarea en PostgreSQL y la segunda la recupera desde la base de datos. Si se utiliza otro puerto externo, reemplaza `5000` por el valor configurado en `APP_PORT`.

## Red y persistencia

Los dos servicios pertenecen a la red Docker `tareas-net`:

```bash
docker network inspect tareas-net
```

PostgreSQL utiliza el volumen `tareas-data` para conservar la información:

```bash
docker volume ls
```

## Detener y limpiar los servicios

Detener y eliminar los contenedores, conservando los datos:

```bash
docker compose down
```

Detener los contenedores y eliminar también el volumen y los datos:

```bash
docker compose down -v
```

## Pruebas locales

```bash
python -m pytest
```

## Integración continua

GitHub Actions se ejecuta en cada `push` y `pull_request`. El pipeline:

1. Instala las dependencias.
2. Ejecuta las pruebas unitarias.
3. Construye las imágenes Docker.
4. Levanta Flask y PostgreSQL.
5. Ejecuta una prueba POST/GET.
6. Verifica que la tarea creada pueda recuperarse.
7. Detiene y limpia los servicios.

El workflow está definido en `.github/workflows/ci.yml`.

## Repositorio

https://github.com/cseverinog/proyecto-tareas
