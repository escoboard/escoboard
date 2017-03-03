from flask import Flask, render_template, send_from_directory
from utils import get_executions, get_games, get_game_detail

SUMMARY_PATH = '/Users/nowke/Desktop/summary'

app = Flask(__name__)

@app.route('/static/<path>')
def send_static_files(path):
    return send_from_directory('templates/static', path)

@app.route('/summary/<path:path>')
def send_summary_files(path):
    print(path)
    return send_from_directory(SUMMARY_PATH, path)

@app.route('/graph')
def graph():
    return render_template('temp.html')

@app.route('/<exec>/<game>')
@app.route('/<exec>/')
def execution_page(exec, game=None):
    if not game:
        games = get_games(summary_path=SUMMARY_PATH, execution=exec)
        return render_template('execution.html', games=games, exec=exec)
    else:
        game_detail = get_game_detail(
            summary_path=SUMMARY_PATH,
            execution=exec,
            game_path=game
        )
        return render_template('game.html', game=game_detail)

@app.route('/')
def home():
    executions = get_executions(SUMMARY_PATH)
    return render_template('home.html', executions=executions)
