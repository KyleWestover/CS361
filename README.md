# CS361

## Using this microservice
To use this microservice you must follow these instructions:

1.) Create a file named 'location.txt'

2.) Create a Python dictionary with the following two key:value pairs:

    - 'latitude': *latitude_val*
    
    - 'longitude': *longitude_val*
    
3.) Write dictionary contents to 'location.txt' using json.dump()

4.) Read the response file named 'weather.txt', which will contain a dictionary with the following keys (and their associated values)

    - 'city'
    
    - 'state'
    
    - 'temp'
    
    - 'weather'
    
    - 'wind_speed'
    
    - 'wind_direction'

Example 'location.txt' request:

    {"latitude": 40.2428029, "longitude": -80.222142}

Example 'weather.txt' response:

    {"city": "Houston", "state": "PA", "temp": 59, "weather": "Broken clouds", "wind_speed": 1.54, "wind_direction": "S"}
  
