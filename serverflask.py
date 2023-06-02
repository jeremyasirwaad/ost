from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def calculator():
    if(request.method == 'POST'):
        num1 = request.form['num1']
        num2 = request.form['num2']
        # calculator = request.form['calculator']
        print(num1,num2)
        return render_template('calculator.html', result=10)
    return render_template('calculator.html')


if(__name__ == '__main__'):
    app.run(debug=True)