from flask import Flask, render_template

app = Flask(__name__)

# Ana sayfa için rota
@app.route('/')
def home():
    return render_template('index.html')

# Asya sayfası için rota
@app.route('/asya')
def asya():
    return render_template('asya.html')

# Hakkımızda sayfası için rota
@app.route('/hakkimizda')
def hakkimizda():
    return render_template('about_us.html')

# Kıtalar sayfası için rota
@app.route('/kitalar')
def kitalar():
    return render_template('kitalar.html')

# Blog sayfası için rota
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Blog sayfası için rota
@app.route('/dolmabahce')
def dolmabahce():
    return render_template('blog_page/dolmabahce.html')

# Blog sayfası için rota
@app.route('/angkor-wat')
def angkor_wat():
    return render_template('blog_page/angkor-wat.html')

# Blog sayfası için rota
@app.route('/iletisim')
def iletisim():
    return render_template('contact_us.html')

if __name__ == '__main__':
    app.run(debug=True)