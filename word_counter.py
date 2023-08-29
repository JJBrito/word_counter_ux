#Imports
from flask import Flask, render_template, request
import string

#App
app = Flask(__name__)

#Route
@app.route('/', methods=['GET', 'POST'])

#Function
def index():
    result = None
    error = None
    if request.method == 'POST':
        test_string = request.form['text']

        if not test_string:
            error = "Required field!"
        else:
            res = sum([i.strip(string.punctuation).isalpha() for i in test_string.split()])
            result = "Word count: " + str(res)

        return render_template('index.html', result=result, error=error)

    return render_template('index.html', result=result)

 #Main
if __name__ == '__main__':
    app.run(debug=True)
