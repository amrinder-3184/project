from tkinter import *
import requests
import time
 

def getWeather(city):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f64b72ac48adaf52228e071836e232ec"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise
    label1.config(text = final_info)
    label2.config(text = final_data)

# Take a variable and use it to make the tkinter window
city = Tk()
city.geometry("600x500")
city.config(background = "cyan")
city.title("Weather App")
f = ("Helvetica", 20, "bold")
t = ("Helvetica", 35, "bold")

textField = Entry(city, text="Search Weather", justify='center', width = 15, font = t)
textField.pack()
textField.focus()
textField.bind('<Return>', getWeather)
Search_btn = Button(city, text="Search Weather", width=15, bg="blue",fg="white", font=f, command= getWeather)
Search_btn.pack()   #(pack is function which will allow us to put all this (^) thing in tkinter window)

label1 = Label(city, font=t,bg="cyan", fg="Purple")
label1.pack()
label2 = Label(city, bg="cyan" , font=f)
label2.pack()
city.mainloop()