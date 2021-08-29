from flask import Flask
app = Flask(__name__) 


@app.route("/")
@app.route("/home")             # both / and /home point to home()
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':      # this is needed only if the program is run directly i.e. python flaskblog.py
    app.run(debug=True)         # __name__ == 'module_name' if ran indirectly

'''
    to run this without if __name__ use: 
        export FLASK_APP=flaskblog.py
        export FLASK_DEBUG=1
        flask run 
'''
