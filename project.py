import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt 
from math import log
from pylab import plot, title, xlabel, ylabel, savefig, legend, array
from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)


def generate(path, query):
    
    import random
    f = open(path, 'w')
    items = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5]
    x = random.choices(items, k=10)
    lists = ''.join(map(str, x))
    f.write(lists)
    f.close

    f = open(path, 'r')
    str1 = f.read()
    lines = ''
    lines = str1
    lines = ''.join([i for i in str1 if not i.isdigit()])
    lines = [lines.replace(' ', '') for lines in lines]
    number_of_characters = len(lines)

    freq = {}
    freqOfEach = {}
    for keys in lines:
        freq[keys] = freq.get(keys, 0) + 1
    freqOfEach = freq
    for i in freqOfEach:
        freqOfEach[i] = freqOfEach[i]/number_of_characters

    queryOUT = {}
    query = query.split(";")
    for i in query:
        x = i.replace(" ", "").split(":")
        queryOUT[x[0]] = float(x[1])

    path = path.replace(".txt", "")
    while '\\' in path:
        path = path.replace(path[0:path.rindex('\\') + 1], "")

    result = []
    result = ''.join([i for i in str1 if i.isdigit()])
    result = list(dict.fromkeys(result))

    n = int(path)

    solut ={}
    solut.update( {path : result} )

    for i,j in solut.items():
        if i in j :
            j.remove(i)

    print(solut)
    score = 0
    for j in queryOUT:
        if j in freq:
            score += queryOUT[j]*freqOfEach[j]

    l = []
    l.append(score)
    l.append(path)
    print(l)
    return solut
    f.close

def typein(path, query):
    from itertools import chain
    f = open(path, 'r')
    str = f.read()
    lines = ''
    lines = str
    str1 = ''
    str1 = str
    lines = [str.replace(' ', '') for str in lines]
    lines = ''.join([i for i in str if not i.isdigit()])

    number_of_characters = len(lines)

    freq = {}
    freqOfEach = {}
    for keys in lines:
        freq[keys] = freq.get(keys, 0) + 1
    freqOfEach = freq
    for i in freqOfEach:
        freqOfEach[i] = freqOfEach[i]/number_of_characters

    queryOUT = {}
    query = query.split(";")
    for i in query:
        x = i.replace(" ", "").split(":")
        queryOUT[x[0]] = float(x[1])

    path = path.replace(".txt", "")
    while '\\' in path:
        path = path.replace(path[0:path.rindex('\\') + 1], "")

    result = ''.join([i for i in str1 if i.isdigit()])
    result = list(dict.fromkeys(result))

    n = int(path)

    solut = {}
    solut.update({path: result})

    for i, j in solut.items():
        if i in j:
            j.remove(i)

    score = 0
    for j in queryOUT:
        if (j in freq):
            score += queryOUT[j]*freqOfEach[j]
    lista = []
    lista.append(score)
    lista.append(path)

    return solut

def main(queryIN={}, ):
    import pygal
    # list_of_scores = []
    # list_of_scores.append(project('D:\IR\project@\project Ir\project.txt', query=query_in))
    # list_of_scores.append(project('D:\IR\project@\project Ir\project1.txt', query=query_in))
    # list_of_scores.append(project('D:\IR\project@\project Ir\project2.txt', query=query_in))
    # list_of_scores.sort(reverse=True)
 
    l={}
    l1=generate('D:\\IR\\project final\\1.txt',query=queryIN)
    l2=generate('D:\\IR\\project final\\2.txt',query=queryIN)
    l3=generate('D:\\IR\\project final\\3.txt',query=queryIN)
    l4=generate('D:\\IR\\project final\\4.txt',query=queryIN)
    l5=generate('D:\\IR\\project final\\5.txt',query=queryIN)

    l.update(l1)
    l.update(l2)
    l.update(l3)
    l.update(l4)
    l.update(l5)

    g1 = nx.DiGraph()
    g1.add_nodes_from(l.keys())

    for k, v in l.items():
        g1.add_edges_from(([(k, t) for t in v]))

    plt.figure(figsize =(5, 5)) 
    nx.draw_networkx(g1, with_labels = True) 

    hubs, authorities = nx.hits(g1, max_iter = 400, normalized = True) 

    print("Hub Scores: ", hubs) 
    print("Authority Scores: ", authorities) 

    line_chart = pygal.Bar()
    line_chart.title = 'Autherity and hub'
    line_chart.x_labels = map(str, range(0, 5))
    for i in 1:
        line_chart.add(l1,l1[i])
    for i in l2:
        line_chart.add(l2,l2[i])
    for i in l3:
        line_chart.add(l3,l3[i])
    for i in l4:
        line_chart.add(l4,l4[i])
    for i in l5:
        line_chart.add(l5,l5[i])

    line_chart.render()
    
    s={}
    s1=typein('D:\\IR\\project final\\1.txt',query=queryIN)
    s2=typein('D:\\IR\\project final\\2.txt',query=queryIN)
    s3=typein('D:\\IR\\project final\\3.txt',query=queryIN)
    s4=typein('D:\\IR\\project final\\4.txt',query=queryIN)
    s5=typein('D:\\IR\\project final\\5.txt',query=queryIN)

    s.update(s1)
    s.update(s2)
    s.update(s3)
    s.update(s4)
    s.update(s5)

    g = nx.DiGraph()
    g.add_nodes_from(s.keys())

    for k, v in s.items():
        g.add_edges_from(([(k, t) for t in v]))

    plt.figure(figsize =(5, 5)) 
    nx.draw_networkx(g, with_labels = True) 

    hubsz, authoritiesz = nx.hits(g, max_iter = 400, normalized = True) 

    print("Hub Scores: ", hubsz) 
    print("Authority Scores: ", authoritiesz) 
        
    line_chart = pygal.Bar()
    line_chart.title = 'Autherity and hub'
    line_chart.x_labels = map(str, range(0, 5))
    for i in s1:
        line_chart.add(s1,s1[i])
    for i in s2:
        line_chart.add(s2,s2[i])
    for i in s3:
        line_chart.add(s3,s3[i])
    for i in s4:
        line_chart.add(s4,s4[i])
    for i in s5:
        line_chart.add(s5,s5[i])

    line_chart.render()

    dict_out = {}
    
    for i in range(0, 5):
        dict_out[s[i][1]] = s[i][0]

    print('the list of ranked hubs', hubs)
    print("the list of ranked Authority",authorities)
    
    for i in range(0, 5):
        dict_out[l[i][1]] = l[i][0]

    print('the list of ranked hubs', hubsz)
    print("the list of ranked Authority",authoritiesz)

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
        return render_template('home.html', list=main(generate(text),list=typein(text)), show=True)
    return render_template('home.html', show=False)

if __name__ == '__main__':
    app.debug = True
    app.run()