import xml.etree.ElementTree as ET
import requests
import random

URL = "https://vrijeme.hr/hrvatska_n.xml"


response = requests.get(URL)
tree = ET.fromstring(response.content)


def extract_dhmz_data(city="Zagreb-Maksimir"):
    data_dict = {}
    for element in tree.findall("Grad"):
        if element.find("GradIme").text == city:
            sensor_data = element.find("Podatci")
            data_dict["temp"] = float(sensor_data.find("Temp").text)
            data_dict["humidity"] = float(sensor_data.find("Vlaga").text)
            data_dict["pressure"] = float(sensor_data.find("Tlak").text)
    print(data_dict)
    return data_dict


def simulate_outside_temp(start=-10, end=40):
    return round(random.uniform(start, end), 1)


def random_variation(value, start=-0.2, end=0.2):
    return round(value + random.uniform(start, end), 1)


def random_gauss_variation(value, sigma=1):
    return round(value + random.gauss(0, sigma), 1)


def simulate_inside_temp(mean=23, sigma=1):
    return round(random.gauss(mean, sigma), 1)


if __name__ == "__main__":
    dhmz_temp = extract_dhmz_data()["temp"]
    outside_temp = random_variation(dhmz_temp)
    inside_temp = simulate_inside_temp()
    print(f"City temp: {dhmz_temp}")
    print(f"Sensor outside temp: {outside_temp}")
    print(f"Sensor inside temp: {inside_temp}")
