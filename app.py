from flask import Flask, render_template, request

app = Flask(__name__)

def get_lang():
    accept = request.headers.get('Accept-Language', '') or ''
    lang = accept.split(',')[0].lower()
    if lang.startswith('pt'): 
        return 'pt'
    return 'en'

@app.route('/')
def home():
    lang = get_lang()
    return render_template('index.html', lang=lang, APP_NAME="BRILHAH IA")

@app.route('/health')
def health():
    return {"ok": True, "app": "BRILHAH IA"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
