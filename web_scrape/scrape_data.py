import requests
import selectorlib
import time
from datetime import datetime
import os

URL = "https://programmer100.pythonanywhere.com/"
filename = "data.txt"

def get_time():
    current_time = datetime.now()
    current_date = current_time.strftime('%d-%m-%Y=%H:%M:%S')
    return current_date

def scrape(url):
    """Scrape the page-source from the URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value

def store(ext_data):
    current_date = get_time()
    
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("date,temperature\n")
            print(f"{filename} successfully created!")

    with open(filename, 'a') as file:
        file.write(f"{current_date},{ext_data}\n")


if __name__ == "__main__":
    while True:
        generature_data = input("Would you like more sample data? (y/n)")
        if generature_data.strip().lower() == "y":
            for i in range(1,4):
                scraped_data = scrape(URL)
                extracted_data = extract(scraped_data)
                store(extracted_data)

                time.sleep(2)

