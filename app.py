from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/webhook", methods=['POST'])
def webhook():
    print(request.data)
    return render_template('index.html')
    
if __name__== "__main__":
    app.run(debug=True)