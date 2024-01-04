import unittest
import requests
from datetime import date

class TestGetDataAPI(unittest.TestCase):
    BASE_URL = "https://example.com/getData.json"

    def test_valid_data(self):
        symbol = "DUYGU"
        date_param = "2024-01-03"

        response = self._make_api_call(symbol, date_param)

        
        self.assertIn("symbol", response, "Missing 'symbol' in the response")
        self.assertIn("name", response, "Missing 'name' in the response")
        self.assertIn("date", response, "Missing 'date' in the response")
        self.assertIn("lastPrice", response, "Missing 'lastPrice' in the response")
        self.assertIn("change", response, "Missing 'change' in the response")


        if response.get("bid", 0) > 0:
            self.assertIn("bid", response, "Missing 'bid' in the response")
        if response.get("ask", 0) > 0:
            self.assertIn("ask", response, "Missing 'ask' in the response")

        
        expected_date = date_param if date_param else str(date.today())
        self.assertEqual(response["date"], expected_date, "Mismatch in 'date' field")

    def test_missing_symbol(self):
        with self.assertRaises(requests.exceptions.HTTPError, msg="Expected HTTPError for missing symbol"):
            self._make_api_call(None, "2024-01-04")

    def test_invalid_date(self):
        symbol = "DUYGU"
        invalid_date = "invalid_date"
        with self.assertRaises(requests.exceptions.HTTPError, msg="Expected HTTPError for invalid date"):
            self._make_api_call(symbol, invalid_date)

    def _make_api_call(self, symbol, date_param):
        url = self.BASE_URL
        params = {"symbol": symbol, "date": date_param}
        response = requests.get(url, params=params)
        
      
        response.raise_for_status()
        
        return response.json()

if __name__ == '__main__':
    unittest.main()
