from flask import Flask, request, jsonify
import helper_scripts

app = Flask(__name__)

@app.route('/great_circle_distance/')
def great_circle_distance():
    """
    Implements GET Request Method

    Parameters:
    
    Returns:
    data (json): returns serialized response of calculated distance  
    """
    if request.method == "GET":
         # validate url params from helper_scripts
        url_location_params = helper_scripts.get_location_params()
        if url_location_params['is_valid']==True:
            latitude1, latitude2, longitude1, longitude2  = url_location_params["data"]

            # calculate distance from helper
            distance = helper_scripts.calculate_distance(latitude1, latitude2, longitude1, longitude2)

            # round to 2dp
            response = str(round(distance,2))+ " KM"
            return jsonify(response), 200
        else:
            # return error from helper
            error_message = url_location_params["data"]
            return {'error': error_message}, 400

    
  
# uncomment this to run locally
# if __name__ == "__main__":
#     app.run(debug=True)
    

       
 