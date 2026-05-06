from flask import Flask, render_template, request
import os

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/produk')
def produk():
    return render_template('produk.html')

@app.route('/kontak', methods=['GET', 'POST'])
def kontak():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        return render_template('hasil.html', nama=nama, email=email)
    return render_template('kontak.html')

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
