from flask import Flask, render_template, request, redirect, url_for, jsonify, app
import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))


# Connect to the database



# TODO IMPLEMENT DATABASE URL
username = os.environ.get('POSTGRES_USERNAME')
# PASSWORD = os.getenv('POSTGRES_PASSWORD')
# PASSWORD = os.getenv('POSTGRES_PASSWORD')
password = os.environ.get('POSTGRES_PASSWORD')
localhost = os.environ.get('POSTGRES_HOST')
port = os.environ.get('POSTGRES_PORT')
# SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{password}@{localhost}:{port}/todoapp'
SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{password}@{localhost}:{port}/todos'
# alter user postgres password 'pass';
