from datetime import date

from src.soloway_unofficial import Client

client = Client("YOUR_LOGIN", "YOUR_PASSWORD")
date_start = date(2022, 1, 1)
date_stop = date(2022, 12, 31)


def test_login():
    client.login()
    assert client.x_sid


def test_get_placements():
    client.get_placements()
    assert client.placements


def test_get_placements_stat_all():
    data = client.get_placements_stat_all(date_start, date_stop)
    assert data


def test_get_placements_stat_by_day():
    data = client.get_placements_stat_by_day(date_start, date_stop)
    result: list = []
    for row in data:
        result.extend(row['list'])
    assert data
