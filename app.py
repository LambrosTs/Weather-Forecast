from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your OpenWeatherMap API Key
API_KEY = '26adadde08b007e99a834241c21c22f7'

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        print(f"City entered: {city}")  # Debugging log
        if city:
            weather_data = get_weather(city)
            print(f"Weather data: {weather_data}")  # Debugging log
    return render_template("index.html", weather=weather_data)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    print(f"API URL: {url}")  # Debugging log
    print(f"API Response: {response.json()}")  # Debugging log
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == "__main__":
    app.run(debug=True)
