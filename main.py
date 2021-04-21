from flask import Flask, render_template, redirect
from forms.user import FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'i always say him that i like chocolate'


@app.route("/")
@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = FeedbackForm()
    if form.validate_on_submit():
        # Эти три переменные на отправку на почту
        name = form.name.data
        email = form.email.data
        mess = form.mess.data
    return render_template('register.html', title='Обратная связь', form=form)


if __name__ == '__main__':
    app.run()