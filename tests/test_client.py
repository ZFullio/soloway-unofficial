from src.soloway_unofficial import Client

client = Client("YOUR_LOGIN", "YOUR_PASSWORD")
date_start = "2022-08-16"
date_stop = "2022-10-15"


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
    assert data
