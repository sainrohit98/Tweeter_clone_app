from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from datetime import datetime
import requests
from geopy.geocoders import Nominatim
from flask_paginate import Pagination

"""from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from posts import models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db = SQLAlchemy(app)

from posts import route"""