Chatbot Nutricional – Proyecto Integrador
👥 Integrantes
Victoria (rama: victoria-dev)
Dana (rama: dana-dev)
Guadalupe (rama: guadalupe-dev)
Sebastian (rama: sebastian-dev)

📌 Descripción
Este proyecto consiste en un chatbot desarrollado en Python con respuestas predefinidas relacionadas a nutrición. Incluye:

Estructura modular.

Pruebas unitarias.

Integración continua (CI) con GitHub Actions.

Simulación de errores reales.

🚀 Instalación
1.Cloná el repositorio:

git clone https://github.com/VictoriaEFernandez/chatbot-nutricion
cd chatbot-nutricion

2.Activá el entorno visual
python -m venv venv
venv\Scripts\activate  # En Windows

3. Instala las dependencias
pip install -r requirements.txt

4.Ejecutá el chatbot 
python chatbot.py

Para correr los test unitarios
pytest

🔧 Integración Continua (CI)
Se configuró GitHub Actions para ejecutar automáticamente:

Instalación de dependencias.

Pruebas unitarias.

Linter (flake8).

📄 Archivo del workflow: .github/workflows/main.yml
🔗 Ver workflow: GitHub Actions

Simulación de errores
Test fallido tras fusión:
Se modificó una respuesta en chatbot.py, lo que hizo fallar un test unitario.

Conflicto de dependencias:
Se agregó una versión incompatible de Flask en requirements.txt, fallando en la instalación.

📘 Lecciones aprendidas
Aprendimos a trabajar en equipo usando ramas.

Simulamos errores comunes en proyectos reales.

Implementamos CI para mejorar la calidad del código.

Usamos pytest y flake8 para pruebas y estilo.
