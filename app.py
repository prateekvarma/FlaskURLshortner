from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        #read the json file(if exists)
        if os.path.exists('urls.json'):
            with open('urls.json') as url_file2:
                #read contents of the json file
                urls = json.load(url_file2)
        #check if the url-code already exists. The keys() will check all key references        
        if request.form['code'] in urls.keys():
            #url-code alredy exists, so don't save, display flash
            flash('Short code already used :( choose another ')
            return redirect(url_for('home'))

        #write url and  url-code into the json file
        urls[request.form['code']] = { 'url':  request.form['url']}
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)

        return render_template('your_url.html', code=request.form['code'])
    else:
        #you have reached the GET request
        #redirect looks for the URL instead of the template, so "/" needed
        return redirect(url_for('home'))
