from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
	return "Hi i am from python file and done in lab test"
if __name__=="__main__":
	app.run(host='0.0.0.0',port=5000)

