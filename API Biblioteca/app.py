from flask import Flask, jsonify, json
from rutas.rutas_libros import libros_bp
from rutas.rutas_socios import socios_bp
from rutas.rutas_prestamos import prestamo_bp

app = Flask(__name__)

app.register_blueprint(libros_bp)
app.register_blueprint(socios_bp)
app.register_blueprint(prestamo_bp)


if __name__ == "__main__":
    app.run(debug=True)