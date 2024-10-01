from flask import Blueprint, render_template
from app.forms import ContactForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template('contact.html', form=form, success=True)
    return render_template('contact.html', form=form)