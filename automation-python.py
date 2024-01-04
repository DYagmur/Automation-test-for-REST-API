import requests
from datetime import datetime

def test_get_data():
    # API endpoint
    api_url = "https://example.com/getData.json"  

    # Test Case 1: 
    symbol = "AAPL"
    date = "2022-01-01"
    response = make_api_call(api_url, symbol, date)
    assert_valid_response(response, symbol, date)

    # Test Case 2: 
    symbol = "GOOGL"
    response = make_api_call(api_url, symbol)
    assert_valid_response(response, symbol, datetime.now().strftime("%Y-%m-%d"))

    # Test Case 3: 
    response = make_api_call(api_url)
    assert_invalid_response(response)

def make_api_call(api_url, symbol, date=None):
    params = {"symbol": symbol}
    if date:
        params["date"] = date

    response = requests.get(api_url, params=params)
    return response.json()

def assert_valid_response(response, symbol, expected_date):
    assert response["symbol"] == symbol
    assert response["date"] == expected_date
    assert "name" in response
    assert "lastPrice" in response
    assert "change" in response

    if "bid" in response:
        assert response["bid"] >= 0

    if "ask" in response:
        assert response["ask"] >= 0

def assert_invalid_response(response):
    assert "error" in response

if __name__ == "__main__":
    test_get_data()
