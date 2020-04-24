from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)

def format_input(input_str):
    if input_str == "":
        return {}
    dict_input = {}
    input_str = input_str.split(";")
    for i in input_str:
        x = i.replace(" ", "").split(":")
        dict_input[x[0]] = float(x[1])
    return dict_input

def project(path, query):
    f = open(path, 'r')
    str = f.read()
    lines = ''
    lines = str
    lines.upper()
    lines = [str.replace(' ', '') for str in lines]
    number_of_characters = len(lines)

    # <><><><><><><><><><><><><><><><><><><<><><><><><><<><><><><><><<><><><><><><<><><><><><><

    freq = {}
    freqOfEach = {}

    for keys in lines:
        freq[keys] = freq.get(keys, 0) + 1
    freqOfEach = freq
    for i in freqOfEach:
        freqOfEach[i] = freqOfEach[i] / number_of_characters

    # <><><><><><><><><><><><><><><><><><><<><><><><><><<><><><><><><<><><><><><><<><><><><><><

    path = path.replace(".txt", "")
    while '\\' in path:
        path = path.replace(path[0:path.rindex('\\') + 1], "")

    # <><><><><><><><><><><><><><><><><><><<><><><><><><<><><><><><><<><><><><><><<><><><><><><

    score = 0
    for j in query:
        if j in freq:
            score += query[j] * freqOfEach[j]
    l = []
    l.append(score)
    l.append(path)
    return l
    f.close()

def main(query_in={}, ):
    list_of_scores = []
    list_of_scores.append(project('D:\IR\project@\project Ir\project.txt', query=query_in))
    list_of_scores.append(project('D:\IR\project@\project Ir\project1.txt', query=query_in))
    list_of_scores.append(project('D:\IR\project@\project Ir\project2.txt', query=query_in))
    list_of_scores.sort(reverse=True)
 
    dict_out = {}
    for i in range(0, 3):
        dict_out[list_of_scores[i][1]] = list_of_scores[i][0]
    print('the list of ranked scores', list_of_scores)
    return dict_out

@app.route('/')

def home():
    return render_template('home.html', show=False)

@app.route('/', methods=['GET', 'POST'])

def my_form_post():
    if request.method == 'POST':
        text = str(request.form['text']).replace(" ", "")
        if text == "":
            return render_template('home.html', list=None, show=False)
        return render_template('home.html', list=main(format_input(text)), show=True)
    return render_template('home.html', show=False)

if __name__ == '__main__':
    app.debug = True
    app.run()