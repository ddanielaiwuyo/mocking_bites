from lib.main import ActivitySuggester
from pytest import raises, mark, fixture
from unittest.mock import Mock, patch

mock_data = {
        "activity":"gain 300 pounds and cut to 180 before summer 2026"
}

class TestAcitivitySuggester:
    @mark.it("Checks that the api function is actually called")
    @patch("lib.main.ActivitySuggester._make_request_to_api")
    def test__make_request_to_api_is_called(self, api_req):
        api_req.return_value = mock_data
        ac = ActivitySuggester()
        ac.suggest()

        api_req.assert_called_once()

    
    @mark.it("Mocking the requests module")
    @patch("lib.main.requests.get")
    def test_request_is_successful(self,  mock_get_req):
        # this is basicallly js in python
        mock_response = Mock()
        mock_response.status_code = 200
        # since the src_code has reponse.json() -> dict
        mock_response.json.return_value = mock_data

        mock_get_req.return_value = mock_response
        
        ac = ActivitySuggester()
        ac.suggest()

        mock_get_req.assert_called_once()
