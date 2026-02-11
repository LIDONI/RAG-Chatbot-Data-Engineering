import pandas as pd
from datetime import datetime, timedelta

DATA_PATH = "data/events.csv"

def test_events_recent():
    df = pd.read_csv(DATA_PATH)

    # Convertir en datetime et supprimer le fuseau horaire
    df["firstdate_begin"] = pd.to_datetime(df["firstdate_begin"], errors="coerce").dt.tz_localize(None)

    one_year_ago = datetime.now() - timedelta(days=365)

    assert df["firstdate_begin"].notna().all(), "Dates invalides détectées"
    assert (df["firstdate_begin"] >= one_year_ago).all(), "Événements trop anciens"

def test_events_region():
    df = pd.read_csv(DATA_PATH)
    assert (df["location_region"] == "Île-de-France").all(), "Événement hors Île-de-France détecté"

if __name__ == "__main__":
    test_events_recent()
    test_events_region()
    print("✅ Tous les tests passent.")
