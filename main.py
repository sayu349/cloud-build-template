from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'cloudbuildが動作しているか確認します。'