from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/')
def a():
    images = ["static/sun.png", "static/cloud.png", "static/ragr.png", "static/clsun.png", "static/rain.png", "static/snow.png"]
    weather_image = random.choice(images)
    s1 = {"static/sun.png": "Солнечно", "static/cloud.png": "Облачно", "static/ragr.png": "Гроза", "static/clsun.png": "Переменная облачность", "static/rain.png": "Дождь", "static/snow.png": "Снег"}
    return render_template('rt.html', text=s1[weather_image], weth = weather_image, t = random.randrange(-30, 40), vl = random.randrange(0, 100))

if __name__ == "__main__":
    app.run()