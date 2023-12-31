from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'

@app.route('/cron/job')
def cron_job():
    return 'Hello cron'


@app.route('/apis/data')
def api():
    with open('files/data.json', mode='r') as my_file:
        text = my_file.read()
        return text
    
    my_file.close()