from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_TARRO = 9000

USUARIOS_REGISTRADOS = {
    "juan": {"password": "admin", "rol": "Administrador"},
    "pepe": {"password": "user", "rol": "Usuario"},
}


def calcular_compra(nombre: str, edad: int, cantidad: int) -> dict:
    total_sin_descuento = cantidad * PRECIO_TARRO

    if edad < 18:
        porcentaje_descuento = 0.0
    elif 18 <= edad <= 30:
        porcentaje_descuento = 0.15
    else:
        porcentaje_descuento = 0.25

    descuento = float(total_sin_descuento * porcentaje_descuento)
    total_a_pagar = float(total_sin_descuento - descuento)

    return {
        "nombre": nombre,
        "edad": edad,
        "cantidad": cantidad,
        "total_sin_descuento": total_sin_descuento,
        "descuento": descuento,
        "total_a_pagar": total_a_pagar,
    }


def verificar_credenciales(usuario: str, contrasena: str) -> str:
    registro = USUARIOS_REGISTRADOS.get(usuario)
    if registro and registro["password"] == contrasena:
        return f"Bienvenido {registro['rol']} {usuario}"
    return "Usuario o contraseña incorrectos"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    error = None

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        try:
            edad = int(request.form.get("edad", ""))
            cantidad = int(request.form.get("cantidad", ""))
            if edad < 0 or cantidad < 0:
                error = "La edad y la cantidad deben ser valores positivos."
            else:
                resultado = calcular_compra(nombre, edad, cantidad)
        except ValueError:
            error = "Ingrese valores numéricos válidos en edad y cantidad."

    return render_template("ejercicio1.html", resultado=resultado, error=error)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        contrasena = request.form.get("contrasena", "")
        mensaje = verificar_credenciales(nombre, contrasena)

    return render_template("ejercicio2.html", mensaje=mensaje)


@app.route("/resultado")
def resultado():
    return render_template("resultado.html")


if __name__ == "__main__":
    app.run(debug=True)
