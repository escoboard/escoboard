import os
import datetime
import random


def get_executions(path):
    exec_dirs = next(os.walk(path))[1]
    exec_count = len(exec_dirs)
    executions = []
    for i, exec_dir in enumerate(exec_dirs):
        full_path = "{}/{}".format(path, exec_dir)
        games_dirs = next(os.walk(full_path))[1]
        execution_time = datetime.datetime.fromtimestamp(float(exec_dir[5:]))
        gif_path = get_random_gif(exec_dir, games_dirs)
        execution = {
            'serial': exec_count - i,
            'games': len(games_dirs),
            'path': exec_dir,
            'time': execution_time.strftime("%I:%M %p, %b %d, %Y"),
            'thumbnail': gif_path
        }
        executions.append(execution)
    return executions

def get_games(summary_path, execution):
    exec_path = "{}/{}".format(summary_path, execution)
    games_dirs = next(os.walk(exec_path))[1]
    game_count = len(games_dirs)
    games = []
    for i, game_dir in enumerate(games_dirs):
        execution_time = datetime.datetime.fromtimestamp(float(game_dir[5:]))
        game = {
            'serial': game_count - i,
            'path': game_dir,
            'time': execution_time.strftime("%I:%M %p, %b %d, %Y"),
        }
        games.append(game)
    return games

def get_game_detail(summary_path, execution, game_path):
    full_path = "{}/{}/{}".format(summary_path, execution, game_path)
    game = {
        'gif': "{}/{}/game.gif".format(execution, game_path),
        'data': "{}/{}/data.csv".format(execution, game_path)
    }
    return game

def get_random_gif(exec_dir, games_dirs):
    game_dir = random.choice(games_dirs)
    return "{}/{}/game.gif".format(exec_dir, game_dir)
