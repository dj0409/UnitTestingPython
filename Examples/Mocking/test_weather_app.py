from weather_app import fetch_weather_data

def test_fetch_weather_data(mocker):
    # Create a mock API client
    mock_api_client = mocker.Mock()

    # Mock the response of the API client
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": "20C", "condition": "Sunny"}

    # Set the mock API client to return the mocked response
    mock_api_client.get.return_value = mock_response

    # Call the function with the mock API client
    result = fetch_weather_data(mock_api_client)

    # Assert that the correct data is returned
    assert result == {"temperature": "20C", "condition": "Sunny"}

    mock_api_client.get.assert_called_once_with("https://api.weather.com/data")