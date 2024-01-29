def report_weather(temperature, function):
    return function(temperature)
    
def as_sun_lover(temperature):
    if temperature >= 25:
        return "Great"
    else:
        return "Not great"
    
def as_snow_lover(temperature):
    if temperature <= 0:
        return "Great"
    else:
        return "Not great"


report_weather(26, as_sun_lover)
#this in repl will return 'Great'
report_weather(26, as_snow_lover)
#this will return 'Not great'
report_weather(-1, as_sun_lover)
report_weather(-1, as_snow_lover)