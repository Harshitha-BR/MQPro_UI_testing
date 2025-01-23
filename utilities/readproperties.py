import configparser
import csv
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import webdriver, options

config = configparser.RawConfigParser()
config.read('/home/harshitha/Desktop/MqPro/MQPro_Testing/configuration/config.ini')


class ReadConfig:

    @staticmethod
    def geturl():
        url = config.get('login', 'login_url')
        return url

    @staticmethod
    def get_password():
        password = config.get('login', 'login_passcode')
        return password

    @staticmethod
    def get_logs_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("utilities", "")
        logs_directory = os.path.join(current_directory, 'Logs')
        return logs_directory

    @staticmethod
    def read_credentials_from_csv():
        credentials = []
        details = []
        filename = "/home/harshitha/Desktop/MqPro/MQPro_Testing/credentials.csv"
        with open(filename, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                email = row['email']
                password = row['password']
                credentials.append({'email': email, 'password': password})
        credentials_data = credentials
        for data in credentials_data:
            details.append(data['email'])
            details.append(data['password'])
        return details

