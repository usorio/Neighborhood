from flask import Flask

app = Flask(__name__)

#initialize views
from project import views
