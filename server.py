from flask import Flask, request


app = Flask(__name__, static_url_path = '')

@app.route('/')
def homepage():
    return app.send_static_file('index.html')


@app.route('/login')
def loginpage():
    return app.send_static_file('login.html')


@app.route('/aboutus')
def aboutus():
    return app.send_static_file('Aboutus.html')


@app.route('/category')
def category():
    return app.send_static_file('category.html')


@app.route('/howitworks')
def howitworks():
    return app.send_static_file('HowitWorks.html')

    
@app.route('/howitworksb')
def howitworksb():
    return app.send_static_file('howitworksb.html')


@app.route('/signup')
def signup():
    return app.send_static_file('signup.html')


@app.route('/profile')
def profile():
    return app.send_static_file('profile.html')

@app.route('/faqs')
def faq():
    return app.send_static_file('faqs.html')


@app.route('/getintouch')
def getintouch():
    return app.send_static_file('getintouch.html')

@app.route('/searchresults')
def searchresults():
    return app.send_static_file('Search-result.html');



if __name__ == '__main__':
    app.run(debug=True)