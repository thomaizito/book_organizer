from flask import request, render_template
from app import app, db
from book.book import OrgLiv
from book.horario.ler import Horario

@app.route('/sla/', methods=['GET', "POST"])
def homepage():
    livros = OrgLiv()
    context = None
    horario = Horario()
    weekday = True
    
    if request.method == "POST":

        fisica = [request.form['f1'].split(' '), request.form["f2"].split(' ')]
        quimica = [request.form['q1'].split(' '), request.form['q2'].split(' ')]
        biologia = [request.form['b1'].split(' '), request.form['b2'].split(' ')]

        sociologia = [request.form['s1'].split(' '), request.form["s2"].split(' ')]
        geografia = [request.form['g1'].split(' '), request.form['g2'].split(' ')]
        filosofia = [request.form['fi1'].split(' '), request.form['fi2'].split(' ')]
        historia = [request.form['h1'].split(' '), request.form['h2'].split(' ')]

        matematica = [request.form['m1'].split(' '), request.form['m2'].split(' ')]

        portugues = [request.form['p1'].split(' '), request.form['p2'].split(' ')]
        ed = [request.form['ed1'].split(' '), request.form['ed2'].split(' ')]
        ingles = [request.form['i1'].split(' '), request.form['i2'].split(' ')]
        literatura = [request.form['li1'].split(' '), request.form['li2'].split(' ')]
        artes = [request.form['a1'].split(' '), request.form['a2'].split(' ')]
        
        items:dict = {
            'fisica': fisica,
            'quimica': quimica,
            'biologia': biologia,
            'sociologia': sociologia,

            'geografia': geografia,
            'filosofia': filosofia,
            'historia': historia,

            'matematica': matematica,
            
            'lingua portuguesa': portugues,
            'educacao fisica': ed,
            'ingles': ingles,
            'artes': artes,
            'literatura': literatura
        }
        
        turma = request.form['turma']


                
        livros.up_books_db(items, turma)
        

        context = livros.display()
    
    if request.method == "GET":
    
        turm = request.args.get('turma')
    
        items:dict = [
        'fisica',
        'quimica',
        'biologia',
        'sociologia',

        'geografia',
        'filosofia',
        'historia',

        'matematica',
        
        'portugues',
        'ed',
        'ingles',
        'artes',
        'literatura'
    ]
        if not horario:
            weekday = False
        
        try:
            dia = request.args.get('dayweek')
        except ValueError:
            weekday = False
            dia = None

        livros_all:dict = livros.down_books_db(turm)

        horario.esc(turm)
        horario = horario.today_day(dia)
        

        livros_do_dia = {}

        for i in horario:
            if i.lower() in items:
                livros_do_dia.update({i.lower(): livros_all[i.lower()]})

        livros.apd(livros_do_dia)
        context = livros.display()
        

            

    return render_template('index.html', context=context, horario=horario, weekday=weekday)
