from flask import Flask, jsonify
from rutas.rutas_libros import libros_bp

app = Flask(__name__)

app.register_blueprint(libros_bp)


if __name__ == "__main__":
    app.run(debug=True)