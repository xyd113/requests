import unittest
from unittest.mock import patch, MagicMock
from requests import api as requests_api # To avoid conflict with the 'request' method

class TestApi(unittest.TestCase):

    @patch('requests.sessions.Session.request')
    def test_request(self, mock_session_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session_request.return_value = mock_response

        url = 'http://example.com'
        
        response = requests_api.request('get', url, timeout=5)

        mock_session_request.assert_called_once_with(
            method='get',
            url=url,
            timeout=5
        )
        self.assertEqual(response, mock_response)

    @patch('requests.sessions.Session.request')
    def test_get(self, mock_session_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session_request.return_value = mock_response

        url = 'http://example.com'
        params = {'key': 'value'}

        response = requests_api.get(url, params=params, timeout=5)

        mock_session_request.assert_called_once_with(
            method='get',
            url=url,
            params=params,
            timeout=5
        )
        self.assertEqual(response, mock_response)

    @patch('requests.sessions.Session.request')
    def test_options(self, mock_session_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session_request.return_value = mock_response

        url = 'http://example.com'

        response = requests_api.options(url, timeout=5)

        mock_session_request.assert_called_once_with(
            method='options',
            url=url,
            timeout=5
        )
        self.assertEqual(response, mock_response)

    @patch('requests.sessions.Session.request')
    def test_head(self, mock_session_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session_request.return_value = mock_response

        url = 'http://example.com'

        response = requests_api.head(url, timeout=5)

        mock_session_request.assert_called_once_with(
            method='head',
            url=url,
            allow_redirects=False, # Default for HEAD
            timeout=5
        )
        self.assertEqual(response, mock_response)

    @patch('requests.sessions.Session.request')
    def test_post_with_data(self, mock_session_request):
        mock_response = MagicMock()
        mock_session_request.return_value = mock_response
        url = 'http://example.com/post'
        data_payload = {'key': 'value'}
        response = requests_api.post(url, data=data_payload, timeout=5)
        mock_session_request.assert_called_once_with(
            method='post',
            url=url,
            data=data_payload,
            json=None,
            timeout=5
        )
        self.assertEqual(response, mock_response)

    @patch('requests.sessions.Session.request')
    def test_post_with_json(self, mock_session_request):
        mock_response = MagicMock()
        mock_session_request.return_value = mock_response
        url = 'http://example.com/post'
        json_payload = {'key': 'value'}
        response = requests_api.post(url, json=json_payload, timeout=5)
        mock_session_request.assert_called_once_with(
            method='post',
            url=url,
            data=None,
            json=json_payload,
            timeout=5
        )
        self.assertEqual(response, mock_response)

    @patch('requests.sessions.Session.request')
    def test_put_with_data(self, mock_session_request):
        mock_response = MagicMock()
        mock_session_request.return_value = mock_response
        url = 'http://example.com/put'
        data_payload = {'key': 'value'}
        response = requests_api.put(url, data=data_payload, timeout=5)
        mock_session_request.assert_called_once_with(
            method='put',
            url=url,
            data=data_payload,
            timeout=5
        )
        self.assertEqual(response, mock_response)

    @patch('requests.sessions.Session.request')
    def test_put_with_json(self, mock_session_request):
        mock_response = MagicMock()
        mock_session_request.return_value = mock_response
        url = 'http://example.com/put'
        json_payload = {'key': 'value'}
        response = requests_api.put(url, json=json_payload, timeout=5)
        mock_session_request.assert_called_once_with(
            method='put',
            url=url,
            data=None,
            json=json_payload,
            timeout=5
        )
        self.assertEqual(response, mock_response)

    @patch('requests.sessions.Session.request')
    def test_patch_with_data(self, mock_session_request):
        mock_response = MagicMock()
        mock_session_request.return_value = mock_response
        url = 'http://example.com/patch'
        data_payload = {'key': 'value'}
        response = requests_api.patch(url, data=data_payload, timeout=5)
        mock_session_request.assert_called_once_with(
            method='patch',
            url=url,
            data=data_payload,
            timeout=5
        )
        self.assertEqual(response, mock_response)

    @patch('requests.sessions.Session.request')
    def test_patch_with_json(self, mock_session_request):
        mock_response = MagicMock()
        mock_session_request.return_value = mock_response
        url = 'http://example.com/patch'
        json_payload = {'key': 'value'}
        response = requests_api.patch(url, json=json_payload, timeout=5)
        mock_session_request.assert_called_once_with(
            method='patch',
            url=url,
            data=None,
            json=json_payload,
            timeout=5
        )
        self.assertEqual(response, mock_response)

    @patch('requests.sessions.Session.request')
    def test_delete(self, mock_session_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_session_request.return_value = mock_response

        url = 'http://example.com/delete'

        response = requests_api.delete(url, timeout=5)

        mock_session_request.assert_called_once_with(
            method='delete',
            url=url,
            timeout=5
        )
        self.assertEqual(response, mock_response)
