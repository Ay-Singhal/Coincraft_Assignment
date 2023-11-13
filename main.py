import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/profit")
def calculate_profit(scheme_code, start_date, end_date, capital=1000000.0):
    
    def get_nav(scheme_code, date):
        api_url = f"https://api.mfapi.in/mf/{scheme_code}"
        response = requests.get(api_url, params={"date": date})
        data = response.json()["data"]
    
        for entry in data:
            if entry["date"] == date:
                return float(entry["nav"])

    nav_purchase = get_nav(scheme_code, start_date)
    nav_redemption = get_nav(scheme_code, end_date)

    units_allotted = capital / nav_purchase
    value_redemption = units_allotted * nav_redemption
    
    net_profit = value_redemption - capital
    return net_profit
