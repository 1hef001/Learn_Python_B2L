from flask import Flask, render_template, request, redirect, url_for
import analyzerFns as a
import test_spell as b
from db_functions import add_todo_item, mark_complete, get_complete, get_incomplete

app = Flask(__name__)

# main
@app.route('/')
def n():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

# @app.route('/todo')
# def todo():

#   TO DO LIST

@app.route('/todo')
def initTodo():
    incomplete = get_incomplete()
    complete = get_complete()
    #print(complete[0])
    return render_template('todo.html', incomplete=incomplete, complete=complete)


@app.route('/todo/add', methods=['POST'])
def add():
    add_todo_item(text=request.form['todoitem'])
    return redirect(url_for('initTodo'))


@app.route('/todo/complete/<id>')
def complete(id):
    mark_complete(id)
    return redirect(url_for('initTodo'))


#   WEB PAGE ANALYZER... DON'T MOD UNLESS NEEDED
sentence, words, uniqueWords, lst, res, text, err, sugg = 0, 0, 0, [], {}, '', [], []
@app.route("/WebPageAnalyzer")
def initWebpage():
    return render_template("webpageAnalyser.html", txt=text,sen=sentence, words=words, uniqueWords=uniqueWords, lst=lst, err=err,sugg=sugg)

@app.route("/WebPageAnalyzer/url", methods=["POST"])
def finWebpage():
    url = request.form["url"]
    global sentence, words, uniqueWords, lst, res, text, err, sugg
    # url.replace("%2F", "/")
    # url.replace("%3A", ":")
    text = a.url(url)
    sentence = a.sentences(text)
    res = a.dictionary(text)
    words = str(sum(res.values()))
    uniqueWords = str(len(res))
    lst = a.sortDictionary(res, 5)
    print(lst)
    _,err,sugg = b.spellCheck(text)
    return redirect(url_for('initWebpage'))
    # return text = "asdasd"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
