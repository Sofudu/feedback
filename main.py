from flask import Flask, render_template, redirect
from forms.user import FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'i always say him that i like chocolate'


@app.route('/', methods=['GET', 'POST'])
def register():
    form = FeedbackForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        mess = form.mess.data
        print(name, email, mess)
        return redirect("/thank")
    return render_template('register.html', title='Обратная связь', form=form)


@app.route("/thank")
def thank():
    return render_template("thank_you.html")


if __name__ == '__main__':
    app.run()