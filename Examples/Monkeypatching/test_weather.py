import pytest
from weather import get_weather

# Fake API response
fake_response = {"city": "Gotham", "temp": 20}

def fake_get(url):
    class FakeResponse:
        def json(self):
            return fake_response
    return FakeResponse()

def test_get_weather(monkeypatch):
    import requests
    monkeypatch.setattr(requests, "get", fake_get)  # Replaces requests.get
    result = get_weather("Gotham")
    assert result["temp"] == 20