from flask import request
import math

import requests



def validate_url_params(param_dict:dict):    
        # checks for invalid types
        for data in param_dict:
            if param_dict[data] == None:
                return {'valid':False,
                        'data': data}           

        #  if url parameter checks passed
        return {'valid':True, 
                'data': None}  
        


def get_location_params():
    if request.method == "GET":
        # get query paramers for url (longitude & latitude) 
        # "type=int" for type checking [returns None for wrong type or if missing]
        is_valid = False

        longitude1 = request.args.get('longitude1', type=int)
        longitude2 = request.args.get('longitude2', type=int)
        latitude1 = request.args.get('latitude1', type=int)
        latitude2 = request.args.get('latitude2', type=int)

        location_params = {
            'latitude1': latitude1,
            'longitude1': longitude1,
            'latitude2': latitude2,
            'longitude2': longitude2
        }
        # validate parameters
        validate = validate_url_params(location_params)

        if validate['valid']==False:
            invalid_parameter = request.args.get(validate['data'])
            print("param", invalid_parameter)

            # if parameter is missing in query           
            if invalid_parameter==None:
                return {'is_valid': validate['valid'],
                        "data": validate['data'] + " is required "
                        }
            # for empty values
            elif len(str(invalid_parameter))<1:
                return {'is_valid': validate['valid'],
                        "data": "Empty value for '/" +validate['data'] + "'/ "
                        }
            # wrong types
            else:
                return {'is_valid': validate['valid'],
                        "data": validate['data'] + ": Wrong datatype (accepts integer value) "
                        }

        else:
            
            return {"is_valid": validate['valid'],
                    "data":[
                            location_params['latitude1'], 
                            location_params['latitude2'],
                            location_params['longitude1'],
                            location_params['longitude2'] 
                            ]}


def calculate_distance(latitude1, latitude2, longitude1, longitude2):
    '''
    Calculate and return the great-circle distance between two users given their latitudes
    and longitudes in decimal degrees(+/-DDD.DDDDD)

        distance = 2 ⋅ R ⋅ arcsin√(sin²(Δφ/2) + cos φ1 ⋅cosφ2 ⋅sin²(Δλ/2))
    
    -where φ is latitude, λ is longitude,
    -R is earth’s radius (mean radius = 6,371km);
    -Δ is delta. i.e the difference between 2 values.
    
    Note that angles need to be in radians to pass trigfunctions in the formula. PI = 3.142
    '''
    R = 6371
    lat1, lat2, long1, long2 = latitude1, latitude2, longitude1, longitude2
    
    latitude_diff = lat1-lat2
    longitude_diff = long1-long2

    distance = 2*R* math.asin( 
                        math.sqrt( 
                            math.sin(latitude_diff)**2 + 
                            (math.cos(lat1) * math.cos(lat2) * math.sin(longitude_diff)**2)
                                )
                            )

    return distance









 