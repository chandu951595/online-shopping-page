from flask import Flask, request, render_template
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template("login.html")
database={'chandu':'viswa','lokesh':'bobby','dhanush':'relangimawa'}
@app.route('/form_login',methods=['Post','Get'])
def login():
    name1=request.form['USERNAME']
    pwd=request.form['PASSWORD']



    if name1 not in database:
        return render_template('login.html', info='invalid name')
    else:
        if database[name1] != pwd:
            return render_template('login.html', info='invalid PASSWORD')
        else:
            return render_template('home.html', name=name1,)



if __name__ == '__main__':
    app.run(debug=True)