# File: weather_selector.py
# Assignment Number: 12.1
# Description: A program that allows the user to input a location (city, country or zip code), gathers data from
#              openweathermap.org and prints weather information in a readable format for said location

import requests
import json
import time

print('Welcome Real Time Weather Update! Look up your Weather Information in Real Time\n'
      "\n Would you like to look up Weather Data? \n"
      "Feel Free to look up by Weather Data by US City or Zip-Code!\n"
      'Please, Enter (1) for US city or (2) For Zip-Code \n')


def main():
    """Main function allows the User to type a Zip-Code or City to receive latest Weather forecast"""
    url = 'https://api.openweathermap.org/data/2.5/weather'
    url_ext = 'https://api.openweathermap.org/data/2.5/forecast'
    location = input('Please Enter desired Zip-Code, or City: ')
    while True:
        try:
            weather_current(location, url)
            weather_extended(location, url_ext)
            print('')
            more_weather()
            break
        except LookupError:
            print('')
            more_weather()
            break


def weather_current(location, url):
    """GET request used to connect the URL for latest weather, ensures connection is ON, parses and displays the data"""
    if location.isdigit() is True:
        query_params = {'zip': location, 'APPID': 'c4499d49b337035afe4b833807989803'}
    else:
        query_params = {'q': location, 'APPID': 'c4499d49b337035afe4b833807989803'}
    response = requests.get(url, params=query_params, timeout=(5, 14))
    try_web(response, location)
    if response.status_code == 200:
        print('Connected....Location Found')
    current_parsed = json.loads(response.text)
    current_formatted(current_parsed)


def weather_extended(location, url_ext):
    """GET request to find extended forecast, parses and displays Weather Data"""
    if location.isdigit() is True:
        query_params = {'zip': location, 'cnt': 16, 'APPID': 'c4499d49b337035afe4b833807989803'}
    else:
        query_params = {'q': location, 'cnt': 16, 'APPID': 'c4499d49b337035afe4b833807989803'}
    response = requests.get(url_ext, params=query_params, timeout=(5, 14))
    try_web(response, location)
    ext_parsed = json.loads(response.text)
    ext_formatted(ext_parsed)


def convert_temp(temp):
    """Converts Kelvin temperatures to Fahrenheit and Celsius format"""
    f_degree = round((((temp - 273.15)*9)/5)+32)
    c_degree = round(temp - 273.15)
    return f'{f_degree}{chr(176)}F / {c_degree}{chr(176)}C'

""" work from here down:  """
def try_web(response, location):
    """Try Except block to test the request was successful, additionally checking if the city or
    zip code entered is valid by using 404 status code"""
    try:
        response.raise_for_status()
    except requests.HTTPError as error0:
        if response.status_code == 404:
            if location.isdigit() is True:
                print(f"The zip code entered '{location}' was not found or is not valid.")
            else:
                if location.__contains__(','):
                    print(f"The city entered '{location[0:-2].title() + location[-2:].upper()}' was not found.")
                else:
                    print(f"The city entered '{location.title()}' was not found.")
        else:
            print('Even we do not have access to single digit zip codes.')
            print(f'{error0}')
    except requests.ConnectionError as error1:
        print('Error Connecting')
        print(error1)
    except requests.Timeout as error2:
        print('Timeout Error')
        print(error2)
    except requests.RequestException as error3:
        print('Something Else Went Wrong')
        print(error3)


def current_formatted(parsed):
    """Decodes the JSON data, formats the time variables to match proper time zones, then formats the printable
    output of the current weather"""
    city = str(json.dumps(parsed['name'])).replace('"', '')
    country = str(json.dumps(parsed['sys']['country'])).replace('"', '')
    timezone = int(json.dumps(parsed['timezone']))
    epoch_time = int(json.dumps(parsed['dt']))
    true_time = epoch_time + timezone
    current_time = time.strftime("%A, %b %d, %Y %I:%M %p (local time)", time.gmtime(true_time))
    temp = float(json.dumps(parsed['main']['temp']))
    conditions = str(json.dumps(parsed['weather'][0]['description'])).replace('"', '').title()
    print(f'Weather Report for {city}, {country} on {current_time}:\n'
          f'Current Temperature {convert_temp(temp)}\n'
          f'Current Conditions: {conditions}\n')


def ext_formatted(parsed):
    """Decodes the JSON data, formats the time variables to match time to the time zones, then formats the printable
    output of the extended forecast"""
    print(f"{'36 Hour Forecast':30}{'Temperature':22}{'Conditions'}")
    # For loop to pull the data for every six (6) hours, approximate 36 hour forecast data return
    for i in range(1, 15, 2):
        epoch_time = int(json.dumps(parsed['list'][i]['dt']))
        timezone = int(json.dumps(parsed['city']['timezone']))
        true_time = epoch_time + timezone
        future_time = time.strftime("%a, %b %d %I:%M %p", time.gmtime(true_time))
        temp = float(json.dumps(parsed['list'][i]['main']['temp']))
        conditions = str(json.dumps(parsed['list'][i]['weather'][0]['description'])).replace('"', '').title()
        print(f'{future_time:30}{convert_temp(temp):22}{conditions}')


def more_weather():
    """Allows the user to look up another location or exit the program"""
    option = str(input('Would you like to enter another location, Yes or No? ')).lower().strip()
    # while loop for a yes selection or to exit the program (and to catch input errors)
    while not (option == 'yes' or option == 'no'):
        option = str(input('You did not enter a valid selection.\n'
                           'Please enter Yes to search another location or No to exit: ')).lower().strip()
    if option == 'yes':
        print('')
        main()
    if option == 'no':
        print('Thank you for using our service. Goodbye')


main()

