from flask.ext.wtf import Form
from wtforms import TextAreaField
from wtforms.validators import Required

class RstForm(Form):
    input_text = TextAreaField('input_text', validators = [Required()])
