import requests, pandas as pd
from datetime import datetime, timedelta

URL = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/evenements-publics-openagenda/records"

def fetch_events():
    one_year_ago = (datetime.now() - timedelta(days=365)).isoformat() # Prise en compte de la date un an par rapport à aujourdhui. 

    params = {
        "limit": 100, # Limit au 100 premiers elements. 
        "where": (
            "location_region='Île-de-France' AND "
            f"firstdate_begin >= '{one_year_ago}'"  
        )
    }

    r = requests.get(URL, params=params, verify=False)
    r.raise_for_status()

    df = pd.DataFrame(r.json()["results"])

    cols = [
        "title_fr", "description_fr",
        "location_name", "location_city",
        "location_region", "firstdate_begin"
    ]
    df = df[cols]
    df.columns = [c.replace("_fr", "") for c in df.columns]

    df.to_csv("data/events.csv", index=False)
    return df

if __name__ == "__main__":
    fetch_events()
