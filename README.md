# Evaluación Final - Aplicación Web con Flask (`evalucionWeb`)

Desarrollé esta aplicación web en Python utilizando el framework **Flask** como parte de mi examen final para la carrera de Técnico Analista Programador en IPLACEX. El proyecto organiza el código mediante rutas, funciones, plantillas HTML (`templates/`) y hojas de estilo externas (`static/`).

## Estructura del Proyecto

```text
evalucionWeb/
├── main.py
├── requirements.txt
├── README.md
├── static/
│   └── styles.css
└── templates/
    ├── index.html
    ├── ejercicio1.html
    ├── ejercicio2.html
    └── resultado.html
```

## Funcionalidades Implementadas

1. **Menú Principal (`/`)**: Diseñé una interfaz inicial con dos botones principales (`Ejercicio 1` y `Ejercicio 2`) estilizados mediante CSS en `static/styles.css`.
2. **Ejercicio 1 - Cálculo de Compras (`/ejercicio1`)**: Implementé un formulario que recibe el nombre del cliente, su edad y la cantidad de tarros de pintura ($9.000 por unidad), aplicando las siguientes reglas de descuento:
   - Menores de 18 años: sin descuento (0%).
   - Entre 18 y 30 años (inclusive): 15% de descuento.
   - Mayores de 30 años: 25% de descuento.
3. **Ejercicio 2 - Inicio de Sesión (`/ejercicio2`)**: Construí un formulario de autenticación que valida credenciales contra los usuarios registrados (`juan` / `admin` y `pepe` / `user`), mostrando el mensaje de bienvenida según el rol o el aviso de error correspondiente.

## Instrucciones de Instalación y Ejecución

1. Clono mi repositorio o descomprimo la carpeta `evalucionWeb`:
   ```bash
   git clone https://github.com/programadorbox/angeloGarridoEvaluacion.git
   cd evalucionWeb
   ```
2. Creo y activo un entorno virtual en Python (opcional, recomendado):
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # En Windows Git Bash
   ```
3. Instalo las dependencias del proyecto desde `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuto la aplicación Flask:
   ```bash
   python main.py
   ```
5. Abro mi navegador web en `http://127.0.0.1:5000/`.
