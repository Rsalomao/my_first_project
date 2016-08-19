"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import my_first_project.views
