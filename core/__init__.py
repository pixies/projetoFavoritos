from flask import Flask

app = Flask(__name__)

from core.controllers import default
