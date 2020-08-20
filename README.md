 _    _            _   _                 _____                                
| |  | |          | | | |               /  ___|                               <br />
| |  | | ___  __ _| |_| |__   ___ _ __  \ `--.  ___ _ __ __ _ _ __   ___ _ __ <br />
| |/\| |/ _ \/ _` | __| '_ \ / _ | '__|  `--. \/ __| '__/ _` | '_ \ / _ | '__|<br />
\  /\  |  __| (_| | |_| | | |  __| |    /\__/ | (__| | | (_| | |_) |  __| |   <br />
 \/  \/ \___|\__,_|\__|_| |_|\___|_|    \____/ \___|_|  \__,_| .__/ \___|_|   <br />
                                                             | |              <br />
                                                             |_|              <br />

# WeatherScraper
Get monthly weather forecast via terminal.

![Screenshot](https://raw.githubusercontent.com/BerkinAKKAYA/WeatherScraper/master/Screenshot.png)

## HOW TO USE
* Download the `Weather.py`
* Run it via terminal: `python3 Weather.py`
* **IMPORTANT:** You need to have **Selenium** and **Chrome Driver** installed on your computer.
* For installation, please see `https://selenium-python.readthedocs.io/installation.html`

## CONFIGURATION
* Initially *WeatherScraper* is set to show the weather of *Istanbul / Turkey*.
* Open the `Weather.py` with your code editor
* Update the **Country** and **City** variables based on your location
* Open `https://accuweather.com`
* Search for your city
* Note the URL `EXAMPLE: https://www.accuweather.com/en/us/new-york/10007/weather-forecast/349727`
* Code1 variable in the Weather.py is the number after your city in the accuweather URL `EXAMPLE: .../new-york/10007/`
* Code2 variable in the Weather.py is the last number in the URL `EAXMPLE: .../weather-forecast/349727`
* Now you are ready to use **WeatherScraper!**
* If you have a slow network connection, you can increase the WaitFor variable's value.

Created By [Berkin AKKAYA](https://berkinakkaya.github.io)
