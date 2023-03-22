from flask import Flask ,request,render_template
import re

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        string = request.form ['string']
        regex = request.form['regex']
        matches = re.findall(regex,string)
        counts=len(matches)
        return render_template('index.html',matches=matches,count=counts)
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
    