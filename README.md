# WeatherScraper
Get monthly weather forecast via terminal.

![Screenshot](https://raw.githubusercontent.com/BerkinAKKAYA/WeatherScraper/master/Screenshot.png)

## HOW TO USE
* Download the `Weather.py`
* Run it via terminal: `python3 Weather.py`
* **IMPORTANT:** You need to have [**Selenium**][selenium] and [**Chrome Driver**][chrome] installed on your computer.
* For installation, please see the [documentation](https://selenium-python.readthedocs.io/installation.html).

## CONFIGURATION
* Initially *WeatherScraper* is set to show the weather of *Istanbul / Turkey*.
* Open the `Weather.py` with your code editor.
* Update the **Country** and **City** variables based on your location.
* Open `https://accuweather.com`
* Search for your city.
* Note the URL `EXAMPLE: https://www.accuweather.com/en/us/new-york/10007/weather-forecast/349727`
* Code1 variable in the Weather.py is the number after your city in the accuweather URL `10007 in the url above`
* Code2 variable in the Weather.py is the last number in the URL `349727 in the url above`
* Now you are ready to use **WeatherScraper!**
* Depending on your network speed, you can edit the `WaitFor` variable's value.

Created By [Berkin AKKAYA](https://berkinakkaya.github.io)


[selenium]: https://raw.githubusercontent.com/BerkinAKKAYA/Pomolog/master/Screenshots/SS1.jpg "Image 1"
[chrome]: https://raw.githubusercontent.com/BerkinAKKAYA/Pomolog/master/Screenshots/SS2.jpg "Image 2"
