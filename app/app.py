from flask import Flask, jsonify


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

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
