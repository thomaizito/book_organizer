from flask import request, render_template
from app import app
from book import OrgLiv

@app.route('/', methods=['GET', "POST"])
def homepage():
    livros = OrgLiv()
    context = None
    if request.method == "POST":
        ch = [request.form['ch1'].split(' '), request.form['ch2'].split(' ')]
        cn = [request.form['cn1'].split(' '), request.form['cn2'].split(' ')]
        l =[request.form['l1'].split(' '), request.form['l2'].split(' ')]
        m = [request.form['m1'].split(' '), request.form['m2'].split(' ')]
        

        livros.apd(ch, cn, l, m)
        context = livros.display()


    return render_template('index.html', context=context)
