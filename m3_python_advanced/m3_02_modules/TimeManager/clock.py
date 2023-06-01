import os
from datetime import datetime
import locale
import time


def pokreni_sat():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        sadasnji_trenutak = datetime.now()
        locale.setlocale(locale.LC_TIME, "de_DE")
        de_datum = f"{sadasnji_trenutak.strftime('%A')}\t{sadasnji_trenutak.strftime('%d/%m/%Y %H:%M:%S')}."
        print(de_datum)
        print()
        locale.setlocale(locale.LC_TIME, "hr_HR")
        hr_datum = f"{sadasnji_trenutak.strftime('%A')}\t{sadasnji_trenutak.strftime('%d/%m/%Y %H:%M:%S')}."
        print(hr_datum)
        time.sleep(1)
