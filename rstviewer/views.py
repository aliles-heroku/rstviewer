from flask import render_template, request

import docutils.core

from rstviewer import app
from rstviewer.forms import RstForm

@app.route('/')
def index():
    form = RstForm()
    return render_template("index.html", form=form,
            short_title="rST Viewer",
            long_title="reStructuredText Viewer",
            placeholder="Create reStructuredText document here ...")

@app.route('/render', methods=['POST'])
def render():
    html = docutils.core.publish_parts(request.form['input_text'],
            writer_name='html')
    return html['whole']
