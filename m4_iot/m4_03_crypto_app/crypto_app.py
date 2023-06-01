from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import tkinter as tk


root = tk.Tk()
root.title("Algebra - Python programer")
root.geometry("600x400")


url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {"limit": 5}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "your-api-key",
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    list_data = data["data"]

    for coin in list_data:
        name = coin["name"]
        price = coin["quote"]["USD"]["price"]
        frame = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
        frame.pack()
        tk.Label(frame, text=f"{name} - {price}").pack()

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

root.mainloop()
