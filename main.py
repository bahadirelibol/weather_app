import customtkinter as ctk

import tkinter as tk

import requests


def get_weather():
    city = city_entry.get().strip()
    url = "#enter a url"
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
        result_label.configure(
            text=f"City: {location}\nWeather: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%")
    except requests.exceptions.RequestException as e:
        result_label.configure(text="Error: There was a problem sending the request!")
    except KeyError:
        result_label.configure(text="No city found or weather data retrieved!")


def close_app():
    app.destroy()


ctk.set_appearance_mode("light")  # light mode
ctk.set_default_color_theme("blue")  # Blue theme

app = ctk.CTk()
app.geometry("650x550")
app.title("Weather App")
app.config(background="#f2f4f4")

#photolabel
weather_photo = tk.PhotoImage(file="wa.png")
photo_label = tk.Label(image=weather_photo, background="#f2f4f4")
photo_label.pack()

#label
city_label = ctk.CTkLabel(app, text="City:", font=("Lucida Handwriting", 30), fg_color="#f2f4f4")
city_label.pack(pady=5)

#entry
city_entry = ctk.CTkEntry(app, width=200, font=("Helvetica", 15))
city_entry.pack(pady=5)
city_entry.focus()

#button
query_button = ctk.CTkButton(app, text="Search", command=get_weather, font=("Helvetica", 12), fg_color="#5dade2",
                             hover_color="#85c1e9")
query_button.pack(pady=5)

#label
result_label = ctk.CTkLabel(app, text="", font=('Helvetica', 20, 'bold'), fg_color="#f2f4f4")
result_label.pack(pady=10)

#exitbutton
exit_btn = ctk.CTkButton(app, text="Exit", command=close_app, font=("Helvetica", 12), fg_color="#d5d8dc",
                         hover_color="#c0392b")
exit_btn.pack(padx=10, pady=10, side='right', anchor='s')

app.mainloop()
