import requests
import sys
import json
from Ninja_key import NINJA_API_KEY


def get_food_info(food):
    URL = "http://127.0.0.1:8000/dishes"
    item =  {"name": food}
    response = requests.post(url=URL, headers={"Content-Type": "application/json"}, data=json.dumps(item))
    ID = requests.json()
    response2 = requests.get(f'{URL}/{ID}', headers={"Content-Type": "application/json"})
    val = response2.json()
    calories = val.get("calories")
    sodium = val.get("sodium_mg")
    sugar = val.get("sugar_g")
    return calories, sodium, sugar

if __name__ == '__main__':
    fh_query = open("query.txt", 'r')
    lines = fh_query.readlines()
    fh_query.close()
    fh_resp = open("/tmp/response.txt",'w')
    for line in lines:
        food = line.strip()
        cal, sod, sug = get_food_info(food)
        s = food + " contains " + '{:1f}'.format(cal) + " calories, " + '{:1f}'.format(sod) + " mgs of sodium, and " + \
            '{:1f}'.format(sug) + " grams of sugar\n"
        fh_resp.write(s)
    fh_resp.close()
