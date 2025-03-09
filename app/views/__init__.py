from flask import request, render_template, Blueprint
from book.book import OrgLiv

request_py = Blueprint('request', __name__)
book = Blueprint('book', __name__)

class Livro:
    def __init__(self):
        livros = OrgLiv
    
    def apd(self):
        pass
    
    def booky(self):
        pass

from . import request_items
