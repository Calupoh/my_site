from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('inicio', __name__)

@bp.route('/')
def index():
    return render_template('inicio/index.html')

