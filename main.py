import tkinter as tk
import requests

def get_weather():
    city = city_entry.get().strip()
    url =#enter a url
    headers = {
        "X-RapidAPI-Key": "#enter a key",
        "X-RapidAPI-Host": "#enter a host"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        weatherdata = response.json()
        location = weatherdata["location"]["name"]
        weather_desc = weatherdata["current"]["condition"]["text"]
        temperature = weatherdata["current"]["temp_c"]
        humidity = weatherdata["current"]["humidity"]
        result_label.config(text=f"City: {location}\nWeather: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%")
    except requests.exceptions.RequestException as e:
        result_label.config(text="Error: There was a problem sending the request!")
    except KeyError:
        result_label.config(text="No city found or weather data retrieved!")

#window
window = tk.Tk()
window.title("Weather App")
window.minsize(width=650, height=700)

#photolabel
weather_photo = tk.PhotoImage(file="wa.png")
photo_label = tk.Label(image=weather_photo)
photo_label.pack()

#label
city_label = tk.Label(window, text="City:", font=("Times", 30), fg="#FF6A6A")
city_label.pack(pady=5)

#entry
city_entry = tk.Entry(bg="#FFFAF0", font=10)
city_entry.pack(pady=5)
city_entry.focus()

#button
query_button = tk.Button(window, font=7, text="Search", command=get_weather, fg="#8B3A3A")
query_button.pack(pady=5)

#label
result_label = tk.Label(window, text="", font=('Helvetica', 20, 'bold'), fg="light blue")
result_label.pack(pady=10)

window.mainloop()