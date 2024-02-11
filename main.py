import math
import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route('/predict')
def get_bike_share_count():
    if request.method == 'GET':
        season = request.args.get("season")
        yr = request.args.get("yr")
        holiday = request.args.get('holiday')
        atemp = request.args.get('atemp')
        casual = request.args.get("casual")
        registered = request.args.get("registered")
        loaded_model = pickle.load(open('bike_sharing_model.sav', 'rb'))
        result = loaded_model.predict([[season, yr, holiday, atemp, casual, registered]])[0]
        return {'bike_share': math.floor(result)}

    else:
        return {'error': True, 'message': "Invalid Request"}


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
