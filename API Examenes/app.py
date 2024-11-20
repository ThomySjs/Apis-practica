from flask import Flask
from rutas.rutas_alumnos import alumnos_bp
from rutas.rutas_temas import temas_bp
from rutas.rutas_TA import ta_bp

app = Flask(__name__)
app.register_blueprint(alumnos_bp)
app.register_blueprint(temas_bp)
app.register_blueprint(ta_bp)


if __name__ == "__main__":
    app.run(debug=True)