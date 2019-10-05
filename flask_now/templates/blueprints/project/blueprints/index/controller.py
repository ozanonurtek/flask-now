from flask import Blueprint, render_template

bp_index = Blueprint('app_index', __name__, url_prefix='/')


@bp_index.route("/", methods=['GET'])
def index():
    title = 'Welcome'
    return render_template('index.html', title=title)

