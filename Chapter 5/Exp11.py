#Conversion Program

def celsius_to_fahrenheit (celsius_float):
    """Convert Celsius to Fahrenheit."""
    return celsius_float * 1.8+32
    
#main part of the program
print("Convert Celsius to Farenheit.")
celsius_float = float (input ("Enter a Celsius Temp:"))
#call the conversion function 
fahrenheit_float = celsius_to_fahrenheit (celsius_float)
#print the return value
print(celsius_float, "Convert to",fahrenheit_float,"Fahrenheit")

