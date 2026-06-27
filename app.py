from flask import Flask, make_response

app = Flask(__name__)

@app.after_request
def agregar_cabeceras_seguridad(response):
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    response.headers["Cache-Control"] = "no-store"
    return response

@app.route("/")
def home():
    html = """
    <html>
        <head>
            <title>Evaluacion 3</title>
        </head>
        <body>
            <h1>Hola Mundo con Flask</h1>
            <p>Aplicacion web para pruebas automatizadas de seguridad con OWASP ZAP.</p>
        </body>
    </html>
    """
    response = make_response(html)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
