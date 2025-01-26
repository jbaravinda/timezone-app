from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/timezone', methods=['GET'])
def get_timezone():
    location = request.args.get('location')
    
    if not location:
        return jsonify({"error": "Location parameter is required"}), 400

    geolocator = Nominatim(user_agent="timezone-app")
    location_data = geolocator.geocode(location)

    if not location_data:
        return jsonify({"error": "Invalid location"}), 404

    lat, lon = location_data.latitude, location_data.longitude
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lng=lon, lat=lat)

    if not timezone_str:
        return jsonify({"error": "Timezone not found"}), 404

    now = datetime.now(pytz.timezone(timezone_str))

    return jsonify({
        "location": location,
        "latitude": lat,
        "longitude": lon,
        "timezone": timezone_str,
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S %Z")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
