import os, signal
from subprocess import call, Popen
from bottle import Bottle, run, template, request

app = Bottle()

@app.route('/')
def index():
    """Home Page"""
    [command, path, files] = get_files_list()

    info = {'title':'Play Videos with '+command+' !',
            'names': files,
            'path': path,
            }

    return template('index.tpl', info)

@app.route('/play/<play_id>')
def play(play_id=None):
    """Play page to maintain context and PID"""
    if play_id is None:
       redirect('/')

    [command, path, files] = get_files_list()
    play_index = int(play_id)
    full_file_path = path +'/'+files[play_index]
    print("Calling "+full_file_path)
    proc = Popen([command, '-o', 'local', full_file_path])

    info = {'name': files[play_index],
            'pid': proc.pid
           }

    return template('play.tpl', info)

@app.route('/stop/<pid>')
def stop(pid=None):
    if pid is not None:
       """TODO""" 

    redirect('/')



def get_files_list():
    COMMAND = 'omxplayer'
    PATH = '/home/pi/Videos'
    files = os.listdir(PATH)
    return [COMMAND, PATH, files]


run(app, host='0.0.0.0', port=8080, debug=True)
