from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from sys import argv

### EDIT THESE VARIABLES
Country = "tr"
City = "istanbul"
Code1 = "318251"
Code2 = "318251"
WaitFor = 60 # in seconds
### Checkout README.md at [GitHub] BerkinAKKAYA/WeatherScraper for more details

# GET MONTH
currentMonth = datetime.now().strftime("%B")
month = None
if len(argv) <= 1:  month = currentMonth
else:               month = argv[1]

# Generate the URL to fetch
BASE_URL = "https://www.accuweather.com/en/"
PARAMS = Country + "/" + City + "/" + Code1 + "/" + month + "-weather/" + Code2
URL = BASE_URL + PARAMS
# Print the URL to fetch
print(URL)

# Open the browser
driver = webdriver.Chrome()
driver.get(URL)

print("WEATHER for %s" % month.upper())

try:
    # Get Temperatures and dates
    dates = WebDriverWait(driver, WaitFor).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.date')))
    temps = WebDriverWait(driver, WaitFor).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.high')))
    # All temperatures will be collected here
    monthlyTemps = []

    # Iterate all the dates
    for index in range(len(dates)):
        # If date is a number, not something like "7/11" (past or next month's data)
        if len(dates[index].text) <= 2:
            date = int(dates[index].text)
            temp = int(temps[index].text[:-1])
            monthlyTemps.append(temp)
            print(month, end=" ")
            print("%2d: %d°" % (date, temp))
    
    # Print the average temperature
    print("AVERAGE: %d°" % (sum(monthlyTemps) // len(monthlyTemps)))
except TimeoutException:
    print("Page took too long to load!")

# Close the browser & end the session
driver.quit()
