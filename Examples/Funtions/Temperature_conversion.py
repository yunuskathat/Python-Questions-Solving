def temperature_conversion(temp, unit):
    if unit == 'C':
        return temp*9/5 + 32  #celcius to farhenite
    elif unit == 'F':
        return (temp - 32)*5/9
    else:
        return None
    
temperature_conversion(29, 'C')
