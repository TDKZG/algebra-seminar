import json

# pokusaj 1.
tekst_json = ""
try:
    with open(
        "m3_03_tekstualne_datoteke/02_datoteke_json/user_p01.json", "r"
    ) as file_reader:
        tekst_json = file_reader.read()
except Exception as e:
    print(f"Dogodila se pogreska {e}")

dict_json = json.loads(tekst_json)
print(dict_json)


# pokusaj 2.
dict_json = {}
try:
    with open(
        "m3_03_tekstualne_datoteke/02_datoteke_json/user_p01.json", "r"
    ) as file_reader:
        dict_json = json.load(file_reader)
except Exception as ex:
    print(f"Dogodila se pogreska {ex}")

print(dict_json)
