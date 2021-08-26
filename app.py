from flask import Flask , render_template , request, escape

app = Flask(__name__)


def search4letters(phrase, letters ='aeioru'):
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


"""
log.write('\n')
        log.write(str(req.form) + '\n')
        log.write(str(req.remote_addr)+ '\n')
        log.write(str(req.user_agent)+'\n')
        log.write(str(res)+'\n')
"""
@app.route("/about")
def about():
    return render_template("index.html" , username  ='Rowida' ,the_title='Welcome to search4letters on the web!')

def log_request(res : str,  req :'flask_request'):
    with open('search4letters.log' , 'w+') as log :
        print(req.form , file =log ,end = '|')
        print(req.remote_addr, file= log ,end = '|')
        print(req.user_agent,file = log ,end = '|')
        print(res ,file = log ,end = '|')

@app.route('/entry') 
def entry_page():
    return render_template('entry.html',title='Welcome to search4letters on the web!' , username = 'Rowida')

@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = search4letters(phrase ,letters)
    log_request(results , request)
    return render_template('result.html', the_phrase = phrase , the_letters = letters ,the_title='search4letters on the web!' ,
            the_results=results)


@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/viewlog')
def view_the_req_history():
    """ 
    with open('search4letters.log') as log:
                    contents = log.readlines()
                return escape(''.join(contents))
    """
    contents = []
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')

    with open('search4letters.log') as log:
        for line in log :
            contents.append([escape(item) for item in line.split('|') ])
        return render_template('viewlog.html',the_title='View Log',row_titles=titles,the_data=contents,)

if __name__ == '__main__':
    app.run(debug = True)