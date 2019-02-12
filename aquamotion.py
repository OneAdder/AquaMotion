from flask import Flask, render_template, request, url_for, redirect, send_file

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/project")
def project():
    return render_template("project.html")


@app.route("/languages")
def languages():
    return render_template("languages.html")

#language groups
@app.route("/germanic")
def germanic():
    return render_template("germanic.html")

@app.route("/romance")
def romance():
    return render_template("romance.html")

@app.route("/average2")
def average2():
    return render_template("average2.html")

@app.route("/slavbalt")
def slavbalt():
    return render_template("slavbalt.html")

@app.route("/caucasian")
def caucasian():
    return render_template("caucasian.html")

@app.route("/uralic")
def uralic():
    return render_template("uralic.html")

@app.route("/turcic")
def turcic():
    return render_template("turcic.html")

@app.route("/semitic")
def semitic():
    return render_template("semitic.html")

@app.route("/indoaryan")
def indoaryan():
    return render_template("indoaryan.html")

@app.route("/average1")
def average1():
    return render_template("average1.html")

@app.route("/fareast")
def fareast():
    return render_template("fareast.html")
#хватит языков

@app.route("/volume")
def volume():
    return render_template("volume.html")


@app.route("/domains")
def domains():
    return render_template("domains.html")


@app.route("/systems")
def systems():
    return render_template("systems.html")


@app.route("/methodology")
def methodology():
    return render_template("methodology.html")


@app.route("/publications")
def publications():
    return render_template("publications.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/authors")
def authors():
    return render_template("authors.html")

@app.route("/gb")
def gd():
    return redirect(url_for('main_page'))

@app.route("/indexl")
def indexl():
    return redirect(url_for('eng_page'))

@app.route('/index-engl')
def eng_page():
    return render_template("index-eng.html")

@app.route('/contacts-eng')
def eng_con():
    return render_template("contacts-eng.html")

@app.route('/publications-eng')
def eng_pub():
    return render_template("publications-eng.html")

@app.route('/summary')
def summary():
    return render_template("summary.html")


@app.route('/0/<other>')
def other_html(other):
    try:
        render_template(other)
    except:
        return('No such html')
    return render_template(other)


@app.route('/<file>')
def show_file(file):
    try:
        return send_file('static/' + file, attachment_filename = file)
    except:
        return ''

@app.route('/<other>')
def other_url(other):
    return redirect('/')

    
if __name__ == '__main__':
    app.run(threaded = True)


