from flask import Flask
import configparser

Config = configparser.ConfigParser()
Config.read("./config.ini")

openWeatherAPIKey = Config.get('DEFAULT', 'openWeatherAPIKey')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':

    app.run()
