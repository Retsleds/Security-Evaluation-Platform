from flask import Flask, render_template, request, Response
import settings
from apps import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=8080)
