from flask import request, render_template
from app import app, db
from book.book import OrgLiv
from book.horario.ler import Horario

@app.route('/', methods=['GET', "POST"])
def homepage():
    livros = OrgLiv()
    context = None
    horario_func = Horario()
    ot_livros = {'interioridade': False, 'itinerario': False}

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
        educacao = [request.form['ed1'].split(' '), request.form['ed2'].split(' ')]
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
            
            'portugues': portugues,
            'ed': educacao,
            'ingles': ingles,
            'artes': artes,
            'literatura': literatura
        }
            
        turma = request.form['turma']


                
        livros.up_books_db(items, turma)
        

        context = livros.display()
    

    if request.method == "GET":
        turma = request.args.get('turma')
        if not turma:
            turma = "B"
    
        items = [
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
        'literatura',
        'interioridade'
    ]   
        dia = request.args.get('dayweek')

        livros_all = livros.down_books_db(turma)
        horario = horario_func.Dia_Horario(dia, turma)
        

        livros_do_dia = {}

        try:
            for i in horario:
                if i.lower() in items:
                    if i.lower() == 'interioridade':
                        ot_livros['interioridade'] = True
                        continue

                    if i.lower() == 'itinerario':
                        ot_livros['itinerario formativo'] = True
                        print(ot_livros)
                        continue
                    
                    livros_do_dia.update({i.lower(): livros_all[i.lower()]})
        
        except Exception as e:
            horario = None

        livros.verification_ordering(livros_do_dia)
        context = livros.display()
        
        if not isinstance(horario, list):
            horario = None
        
            

    return render_template('index.html', context=context, horario_func=horario_func, horario=horario, turma=turma, livros=livros.livros, ot_livros=ot_livros)
