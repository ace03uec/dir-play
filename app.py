import os
from subprocess import call
from bottle import Bottle, run, template, request

app = Bottle()

@app.route('/')
def index():
    """Home Page"""
    COMMAND = 'playlocal'
    PATH = '~/Videos'
    files = os.listdir(PATH)
    info = {'title':'Play Videos with '+COMMAND+' !',
            'names': files,
            'path': PATH,
            }
    
    if request.query.play:
        play_index = int(request.query.play)
        full_file_path = path +'/'+files[play_index]
        print("Calling "+full_file_path)
        call([COMMAND, full_file_path])

    return template('simple.tpl', info)
            
run(app, host='localhost', port=8080)
