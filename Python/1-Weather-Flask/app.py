from flask import Flask,render_template,request
from local_settings import SECRET_KEY, MAPS_KEY
import requests
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map



app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = MAPS_KEY
GoogleMaps(app)



@app.route("/index",methods=["GET","POST"])
def index():
    if request.method == 'POST':      
        city = request.form["city"]
        url_path = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid='+SECRET_KEY
        r=requests.get(url_path)
        data=r.json()
        return render_template('index.html',city=city,data=data)
    else:
        return render_template("index.html")

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)  