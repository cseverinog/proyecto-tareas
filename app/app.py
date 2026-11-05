from flask import Flask, jsonify, request
from psycopg import OperationalError

from app.database import complete_task, create_task, list_tasks


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify({
            "nombre": "API de tareas",
            "estado": "en desarrollo",
            "version": "0.1.0",
        })

    @app.get("/health")
    def health():
        return jsonify({"estado": "ok"})

    @app.post("/tareas")
    def add_task():
        payload = request.get_json(silent=True) or {}
        title = str(payload.get("titulo", "")).strip()
        if not title:
            return jsonify({"error": "El campo 'titulo' es obligatorio"}), 400

        try:
            task = create_task(title)
            return jsonify(task), 201
        except OperationalError:
            return jsonify({"error": "No fue posible conectar con la base de datos"}), 503

    @app.get("/tareas")
    def get_tasks():
        try:
            return jsonify(list_tasks())
        except OperationalError:
            return jsonify({"error": "No fue posible conectar con la base de datos"}), 503

    @app.patch("/tareas/<int:task_id>/completar")
    def finish_task(task_id):
        try:
            task = complete_task(task_id)
            if task is None:
                return jsonify({"error": "Tarea no encontrada"}), 404
            return jsonify(task)
        except OperationalError:
            return jsonify({"error": "No fue posible conectar con la base de datos"}), 503

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
