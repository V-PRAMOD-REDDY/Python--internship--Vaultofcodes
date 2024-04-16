def convert_temperature(temperature, unit):
    if unit == 'F':
        converted_temperature = (temperature - 32) * 5/9
    elif unit == 'C':
        converted_temperature = (temperature * 9/5) + 32
    else:
        return "Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius."
    
    return round(converted_temperature, 2)


print(convert_temperature(32, 'F'))  
print(convert_temperature(100, 'C')) 
