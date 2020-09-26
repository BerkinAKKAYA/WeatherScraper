from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from sys import argv
from tqdm import tqdm

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
print("FETCHING WEATHER for %s..." % month.upper())

print("Opening the Chrome Web Driver...")
driver = webdriver.Chrome()

print("Opening the URL...")
driver.get(URL)

try:
    print("Reading data...")
    
    # Get Temperatures and dates
    dates = WebDriverWait(driver, WaitFor).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.date')))
    temps = WebDriverWait(driver, WaitFor).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.high')))

    # All temperatures will be collected here
    dateTempPairs = []

    # Iterate all the dates
    for index in tqdm(range(len(dates))):
        # If date is a number, not something like "7/11" (past or next month's data)
        if len(dates[index].text) <= 2:
            date = int(dates[index].text)
            temp = int(temps[index].text[:-1])
            dateTempPairs.append((date, temp))

    for pair in dateTempPairs:
        print("%s %2d: %d°" % (month, pair[0], pair[1]))

    # Print the average temperature
    allTemperatures = [pair[1] for pair in dateTempPairs]
    print("AVERAGE: %d°" % (sum(allTemperatures) // len(allTemperatures)))
except TimeoutException:
    print("Page took too long to load!")

# Close the browser & end the session
driver.quit()
