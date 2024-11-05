from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Заміна 'YOUR_API_KEY' на ваш API ключ
    response = requests.get("https://api.currencyapi.com/v3/latest?apikey=cur_live_zIXdHha2jXRLV8nn55YPDGEdG4afVYC1B5MVufle")
    data = response.json()
    rates = data.get("data", {})
    return render_template("index.html", rates=rates)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
