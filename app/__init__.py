from flask import Flask
from book.book import OrgLiv

app = Flask(__name__)
livro = OrgLiv()

from app.views.request_items import apd