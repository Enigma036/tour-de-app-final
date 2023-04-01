from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from datetime import datetime
from . import db
from sqlalchemy import desc
from .models import Note
import json
import requests



api = Blueprint("api", __name__) 

@api.route('/')
def home():

    return render_template("stat.html")

@api.route('/user')
def user():
    # zde se provádí aktualizace dat z vzdáleného API s ověřovacím kódem
    headers = {'x-access-token': '9affb11f76fe692941ea8ae870f77b62'}
    response = requests.get('https://tda.knapa.cz/user/', headers=headers)
    data = response.json()

    print("AHOJ")
    # vrácení aktualizovaných dat jako JSON pomocí Flask
    return jsonify(data)

@api.route('/sysinfo/')
def sys():
    # zde se provádí aktualizace dat z vzdáleného API s ověřovacím kódem
    headers = {'x-access-token': '9affb11f76fe692941ea8ae870f77b62'}
    response = requests.get('https://tda.knapa.cz/sysinfo/', headers=headers)
    data = response.json()
    
    print("OK")
    # vrácení aktualizovaných dat jako JSON pomocí Flask
    return jsonify(data)

@api.route('/commit/')
def commit():
    # zde se provádí aktualizace dat z vzdáleného API s ověřovacím kódem
    headers = {'x-access-token': '9affb11f76fe692941ea8ae870f77b62'}
    response = requests.get('https://tda.knapa.cz/commit/', headers=headers)
    data = response.json()

    print("LOL")
    # vrácení aktualizovaných dat jako JSON pomocí Flask
    return jsonify(data)

