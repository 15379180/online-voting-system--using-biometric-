from flask import Flask, render_template,request,session,logging,url_for,redirect

app = Flask(__name__)

@app.route("/" , methods=['GET'])

#route = generate url

def  home():
	return render_template("LOGIN.html")

@app.route('/result', methods=['POST'])

def result():
	usr=request.form['Username']
	pswd=request.form['password']
	print(Username)
	print(password)
	return "success"

if __name__=="__main__":
	app.run(host='0.0.0.0' , debug = True)