from flask import Flask, render_template, request, redirect, url_for, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'home/nvidia/appli/src/'
UPLOAD_FOLDER_M = 'home/nvidia/appli/src2/piwall/videos/raw/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_M'] = UPLOAD_FOLDER_M

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_0/', methods=['GET', 'POST'])
def upload_0():
    with open(UPLOAD_FOLDER+'files_0.txt', 'r') as f:
        with open(UPLOAD_FOLDER+'files_0.txt', 'r+') as f:
            lines = f.readlines()
            if len(lines) == 0:
                existing_files = []
            else:
                existing_files = lines[0].split(' ')[:-1]

    if os.path.exists('files_to_delete_0.txt'):
        with open('files_to_delete_0.txt', 'r') as f:
            files_to_delete = f.read().splitlines()

        with open(UPLOAD_FOLDER+'files_0.txt', 'r+') as f:
            if f.readline() == '':
                files = []
            else:
                f.seek(0)
                files = f.readlines()[0].split(' ')[:-1]

            for filename in files_to_delete:
                if filename in files:
                    files.remove(filename)

            f.truncate(0)
            f.seek(0)
            for filename in files:
                f.write(filename + ' ')
        
        existing_files = [filename for filename in existing_files if filename not in files_to_delete]
    
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_0'))
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('upload_0.html', files=files, existing_files=existing_files)

@app.route('/televerser_0/', methods=['POST'])
def televerser_0():
    data = request.get_json()
    filenames = data['filenames']
    existing_files = data['existing_files']

    with open(UPLOAD_FOLDER+'files_0.txt', 'r') as f:
        existing_files = f.readline().split(' ')[:-1]

    with open(UPLOAD_FOLDER+'files_0.txt', 'w') as f:
        for filename in existing_files:
            f.write(filename + ' ')
        for filename in filenames:
            f.write(filename + ' ')

    return render_template('upload_0.html')

@app.route('/config_file_0/', methods=['POST'])
def config_file_0():
    with open(UPLOAD_FOLDER+'files_0.txt', 'r+') as f:
        lines = f.readlines()
        if len(lines) == 0:
            files = []
        else:
            files = lines[0].split(' ')[:-1]

    with open(UPLOAD_FOLDER+'config.txt', 'r+') as f:
        print("LES FILES :", files)
        lines = f.readlines()
        
        if len(lines) == 0:
            lines.append('E 0 ')  # Ajoute 'E 0 ' à la liste si elle est vide
        else:
            lines[0] = 'E 0 '  # Modifie la première ligne avec la valeur 'E 0 '

        for filename in files:
            if filename[-4:] == '.ogg' or filename[-4:] == '.ogv' or filename[-5:] == '.webm':
                lines[0] += 'V ' + "src/" + filename + ' '
                print("LIGNE 0 :", lines[0])
            elif filename[-4:] == '.jpg' or filename[-4:] == '.png':
                lines[0] += 'I ' + "src/" + filename + ' 60 '
                print("LIGNE 0 :", lines[0])
            else:
                print('error')
        
        print("LES LIGNES :", lines)
        f.seek(0)
        f.truncate(0)
        lines.insert(1, '\n')
        f.writelines(lines)

    return render_template('message.html')

@app.route('/generate_config_0/', methods=['POST'])
def generate_config_0():
    config_file_0()
    # Supprimer le fichier files_to_delete.txt
    if os.path.exists('files_to_delete.txt'):
        os.remove('files_to_delete.txt')
    return render_template('message.html')


@app.route('/delete_existing_file_0/', methods=['POST'])
def delete_existing_file_0():
    filename = request.get_json()['filename']

    with open('files_to_delete_0.txt', 'a') as f:
        f.write(filename.rstrip()+'\n')

    return 'Fichier ajouté à la liste des fichiers à supprimer'

@app.route('/clear_cache_0/', methods=['POST'])
def clear_cache():
    with open('files_to_delete_0.txt', 'w') as f:
        f.write('')
    return 'Cache vidé'

@app.route('/upload_1/', methods=['GET', 'POST'])
def upload_1():
    with open(UPLOAD_FOLDER+'files_1.txt', 'r') as f:
        with open(UPLOAD_FOLDER+'files_1.txt', 'r+') as f:
            lines = f.readlines()
            if len(lines) == 0:
                existing_files = []
            else:
                existing_files = lines[0].split(' ')[:-1]

    if os.path.exists('files_to_delete_1.txt'):
        with open('files_to_delete_1.txt', 'r') as f:
            files_to_delete = f.read().splitlines()

        with open(UPLOAD_FOLDER+'files_1.txt', 'r+') as f:
            if f.readline() == '':
                files = []
            else:
                f.seek(0)
                files = f.readlines()[0].split(' ')[:-1]

            for filename in files_to_delete:
                if filename in files:
                    files.remove(filename)

            f.truncate(0)
            f.seek(0)
            for filename in files:
                f.write(filename + ' ')
        
        existing_files = [filename for filename in existing_files if filename not in files_to_delete]
    
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_1'))
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('upload_1.html', files=files, existing_files=existing_files)

@app.route('/televerser_1/', methods=['GET', 'POST'])
def televerser_1():
    data = request.get_json()
    filenames = data['filenames']
    existing_files = data['existing_files']

    with open(UPLOAD_FOLDER+'files_1.txt', 'r') as f:
        existing_files = f.readline().split(' ')[:-1]

    with open(UPLOAD_FOLDER+'files_1.txt', 'w') as f:
        for filename in existing_files:
            f.write(filename + ' ')
        for filename in filenames:
            f.write(filename + ' ')

    return render_template('upload_1.html')

@app.route('/config_file_1/', methods=['POST'])
def config_file_1():
    #creation of a config file that will be used by the python script
    #it reads the file files.txt and creates a payload.txt who has this format: E [screen number (0 for this example)] [V for video or I for image] [file name]
    #the payload.txt file is then read by the python script and the video/image is displayed on the screen
    with open(UPLOAD_FOLDER+'files_1.txt', 'r+') as f:
        lines_f = f.readlines()
        if len(lines_f) == 0:
            files = []
        else:
            files = lines_f[0].split(' ')[:-1]

    with open(UPLOAD_FOLDER+'config.txt', 'r+') as f:
        print("LES FILES :", files)
        lines = f.readlines()
        if len(lines) == 0:
            lines.append('\n')  # Ajoute une ligne vide si la liste est vide ou ne contient qu'une seule ligne
            lines.append('\n')  # Ajoute une autre ligne vide pour atteindre la deuxième ligne
            lines[1] = 'E 1 '  # Modifie la deuxième ligne avec la valeur 'E 1' suivie d'un saut de ligne
            print("cas 1")

        elif len(lines) == 1:
            lines.append('\n')  # Ajoute une ligne vide si la liste ne contient qu'une seule ligne
            lines[1] = 'E 1 '  # Modifie la deuxième ligne avec la valeur 'E 1'
            print("cas 2")
        
        elif len(lines) == 2:
            lines[1] = 'E 1 '
            print("cas 3")

        else:
            print("Erreur : le fichier config.txt contient plus de 2 lignes")

        for filename in files:
            if filename[-4:] == '.ogg' or filename[-4:] == '.ogv' or filename[-5:] == '.webm':
                lines[1] += 'V ' + "src/" + filename + ' '
            elif filename[-4:] == '.jpg' or filename[-4:] == '.png':
                lines[1] += 'I ' + "src/" + filename + ' 60 '
            else:
                print('error')

        print("LES LIGNES :", lines)
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)
    return render_template('message.html')

@app.route('/generate_config_1/', methods=['POST'])
def generate_config_1():
    config_file_1()
    # Supprimer le fichier files_to_delete.txt
    if os.path.exists('files_to_delete_1.txt'):
        os.remove('files_to_delete_1.txt')
    return render_template('message.html')


@app.route('/delete_existing_file_1/', methods=['POST'])
def delete_existing_file_1():
    filename = request.get_json()['filename']

    with open('files_to_delete_1.txt', 'a') as f:
        f.write(filename.rstrip()+'\n')

    return 'Fichier ajouté à la liste des fichiers à supprimer'

@app.route('/clear_cache_1/', methods=['POST'])
def clear_cache_1():
    with open('files_to_delete_1.txt', 'w') as f:
        f.write('')
    return 'Cache vidé'


@app.route('/upload_m/', methods=['GET', 'POST'])
def upload_m():
    with open(UPLOAD_FOLDER_M+'files_m.txt', 'r') as f:
        with open(UPLOAD_FOLDER_M+'files_m.txt', 'r+') as f:
            lines = f.readlines()
            if len(lines) == 0:
                existing_files = []
            else:
                existing_files = lines[0].split(' ')[:-1]

    if os.path.exists('files_to_delete_m.txt'):
        with open('files_to_delete_m.txt', 'r') as f:
            files_to_delete = f.read().splitlines()

        with open(UPLOAD_FOLDER_M+'files_m.txt', 'r+') as f:
            if f.readline() == '':
                files = []
            else:
                f.seek(0)
                files = f.readlines()[0].split(' ')[:-1]

            for filename in files_to_delete:
                if filename in files:
                    files.remove(filename)

            f.truncate(0)
            f.seek(0)
            for filename in files:
                f.write(filename + ' ')
        
        existing_files = [filename for filename in existing_files if filename not in files_to_delete]
    
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER_M'], filename))
            return redirect(url_for('upload_m'))
    files = os.listdir(app.config['UPLOAD_FOLDER_M'])
    return render_template('upload_m.html', files=files, existing_files=existing_files)

@app.route('/televerser_m/', methods=['GET', 'POST'])
def televerser_m():
    data = request.get_json()
    filenames = data['filenames']
    existing_files = data['existing_files']

    with open(UPLOAD_FOLDER_M+'files_m.txt', 'r') as f:
        existing_files = f.readline().split(' ')[:-1]

    with open(UPLOAD_FOLDER_M+'files_m.txt', 'w') as f:
        for filename in existing_files:
            f.write(filename + ' ')
        for filename in filenames:
            f.write(filename + ' ')

    return render_template('upload_m.html')

@app.route('/config_file_m/', methods=['POST'])
def config_file_m():
    #creation of a config file that will be used by the python script
    #it reads the file files.txt and creates a payload.txt who has this format: E [screen number (0 for this example)] [V for video or I for image] [file name]
    #the payload.txt file is then read by the python script and the video/image is displayed on the screen
    with open(UPLOAD_FOLDER_M+'files_m.txt', 'r+') as f:
        lines_f = f.readlines()
        if len(lines_f) == 0:
            files = []
        else:
            files = lines_f[0].split(' ')[:-1]

    with open(UPLOAD_FOLDER_M+'config.txt', 'w') as f:
        print("LES FILES :", files)
        f.seek(0)
        f.truncate(0)
        f.write('M ')

        for filename in files:
            if filename[-4:] == '.ogg' or filename[-4:] == '.ogv' or filename[-5:] == '.webm':
                f.write('V ' + "src/" + filename + ' ')
            elif filename[-4:] == '.jpg' or filename[-4:] == '.png':
                f.write('I ' + "src/" + filename + ' 60 ')
            else:
                print('error')

    return render_template('message.html')

@app.route('/generate_config_m/', methods=['POST'])
def generate_config_m():
    config_file_m()
    # Supprimer le fichier files_to_delete.txt
    if os.path.exists('files_to_delete_m.txt'):
        os.remove('files_to_delete_m.txt')
    redirect(url_for('message'))


@app.route('/delete_existing_file_m/', methods=['POST'])
def delete_existing_file_m():
    filename = request.get_json()['filename']

    with open('files_to_delete_m.txt', 'a') as f:
        f.write(filename.rstrip()+'\n')

    return 'Fichier ajouté à la liste des fichiers à supprimer'

@app.route('/clear_cache_m/', methods=['POST'])
def clear_cache_m():
    with open('files_to_delete_m.txt', 'w') as f:
        f.write('')
    return 'Cache vidé'

@app.route('/message/')
@app.route('/message.html')
def message():
    return render_template('message.html')

if __name__ == "__main__":
    app.run()