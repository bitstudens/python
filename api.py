import requests
import json

latitude = 52.5
longitude = 13.41

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
  
    current_weather = data.get("current_weather", {})
    temperature = current_weather.get("temperature")
    windspeed = current_weather.get("windspeed")
    winddirection = current_weather.get("winddirection")
    weathercode = current_weather.get("weathercode")
    time = current_weather.get("time")

    # Print the current weather data
    print(f"Current Weather in New York City:")
    print(f"Temperature: {temperature}°C")
    print(f"Windspeed: {windspeed} km/h")
    print(f"Wind Direction: {winddirection}°")
    print(f"Weather Code: {weathercode}")
    print(f"Time: {time}")
else:
    print(f"Failed to retrieve weather data. Status code: {response.status_code}")






# # # Example of using the requests library to get a random dog image




# # response = requests.get("https://random.dog/woof.json")

# # if response.status_code == 200:
# #     todos = response.json()
# #     print(todos)
# # else:   
# #     print(f"Failed to retrieve todos. Status code: {response.status_code}")

# def get_joke():
#     response = requests.get("https://official-joke-api.appspot.com/random_joke")
#     if response.status_code == 200:
#         joke = response.json()
#         return joke
#     else:
#         print(f"Failed to retrieve joke. Status code: {response.status_code}")
#         return None
    
# joke1 = get_joke()
# joke2 = get_joke()


# print(f"Joke: {joke1['setup']}")
# print(f"Punchline: {joke1['punchline']} \n")



# print(f"Joke: {joke2['setup']}")
# print(f"Punchline: {joke2['punchline']}")



    
        

  