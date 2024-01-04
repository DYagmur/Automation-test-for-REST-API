const axios = require('axios');
const assert = require('assert');

async function testGetData() {
    // API endpoint
    const apiUrl = 'https://example.com/getData.json'; 

    // Test Case 1: 
    const symbol1 = 'AAPL';
    const date1 = '2022-01-01';
    const response1 = await makeApiCall(apiUrl, symbol1, date1);
    assertValidResponse(response1, symbol1, date1);

    // Test Case 2: 
    const symbol2 = 'GOOGL';
    const response2 = await makeApiCall(apiUrl, symbol2);
    assertValidResponse(response2, symbol2, getCurrentDate());

    // Test Case 3: 
    const response3 = await makeApiCall(apiUrl);
    assertInvalidResponse(response3);
}

async function makeApiCall(apiUrl, symbol, date = null) {
    const params = { symbol: symbol };
    if (date) {
        params.date = date;
    }

    try {
        const response = await axios.get(apiUrl, { params });
        return response.data;
    } catch (error) {
        return { error: error.message };
    }
}

function assertValidResponse(response, symbol, expectedDate) {
    assert.strictEqual(response.symbol, symbol);
    assert.strictEqual(response.date, expectedDate);
    assert.ok('name' in response);
    assert.ok('lastPrice' in response);
    assert.ok('change' in response);

    if ('bid' in response) {
        assert.ok(response.bid >= 0);
    }

    if ('ask' in response) {
        assert.ok(response.ask >= 0);
    }
}

function assertInvalidResponse(response) {
    assert.ok('error' in response);
}

function getCurrentDate() {
    const now = new Date();
    const formattedDate = `${now.getFullYear()}-${(now.getMonth() + 1).toString().padStart(2, '0')}-${now.getDate().toString().padStart(2, '0')}`;
    return formattedDate;
}

testGetData();
