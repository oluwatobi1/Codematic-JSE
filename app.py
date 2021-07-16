from flask import Flask, request, jsonify
import helper_scripts

app = Flask(__name__)

@app.route('/great_circle_distance/')
def great_circle_distance():
    # validate url params from helper_scripts
    url_location_params = helper_scripts.get_location_params()
    if url_location_params['is_valid']==True:
        latitude1, latitude2, longitude1, longitude2  = url_location_params["data"]
        distance = helper_scripts.calculate_distance(latitude1, latitude2, longitude1, longitude2)
        
        return jsonify(distance), 200
    else:
        error_message = url_location_params["data"]
        return {'error': error_message}, 400

    



    

       
    

if __name__ == "__main__":
    app.run(debug=True)
