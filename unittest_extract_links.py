import unittest
from unittest.mock import patch, mock_open
from extractor import extract_links


class TestExtractLinks(unittest.TestCase):
    @patch('extractor.requests.get')
    def test_extract_links(self, mock_get):
        # Create a mock response with some HTML content
        mock_response = mock_get.return_value
        mock_response.content = b'<html><body><a href="https://example.com">example</a></body></html>'

        # Call the extract_links method with the mock response
        links = extract_links(mock_response.content)

        # Verify that the method returned the correct link
        self.assertEqual(links, ['https://example.com'])


if __name__ == '__main__':
    unittest.main()
