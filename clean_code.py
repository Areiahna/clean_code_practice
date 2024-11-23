# Task 1: Identifying and Creating Classes

    # Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

    # Problem Statement: The existing script for the weather forecast application is written in a procedural style and lacks organization.

    # Code Example: Before Refactoring:

    # Weather Forecast Application Script

weather_data = {
    "New York" : {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
    "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
    "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
}

class WeatherDataFetcher():
    def __init__ (self,city,data = weather_data):
        self.city = city
        self.data = data

    def get_city_data(self,city):
        if self.city not in self.data:
            return f"Weather data not available for {city}"
        else:
            print(f"Fetching weather data for {city}...")
            return(self.data.get(city))


class DataParser(WeatherDataFetcher):
    def __init__ (self,city, data = weather_data):
        self.city = city
        self.data = data

    def detailed_forecast(self):
        if self.city not in self.data:
            print(f"Weather data not available for {self.city}")
        else:
            data = self.get_city_data(self.city)
            print(f"Fetching weather data for {self.city}...")
            temperature = data["temperature"]
            condition = data["condition"]
            humidity = data["humidity"]

            print(f"Weather in {self.city}: {temperature} degrees, {condition}, Humidity: {humidity}%")


def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ").title()
        if city.lower() == 'exit':
            break  
        data = WeatherDataFetcher(city) 
        parsed_data = DataParser(city)   
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = parsed_data.detailed_forecast()
        else:
            forecast =  data.get_city_data(city)
        print(forecast)

if __name__ == "__main__":
    main()