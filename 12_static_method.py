class TemperatureConverter():

    @staticmethod
    def celsius_to_farenheight(c):
        return (c * 9/5) + 32
    
if __name__ == "__main__":
        print("Farenheight:", TemperatureConverter.celsius_to_farenheight(0))
        print("Farenheight:", TemperatureConverter.celsius_to_farenheight(100))
        print("Farenheight:", TemperatureConverter.celsius_to_farenheight(120))
    

