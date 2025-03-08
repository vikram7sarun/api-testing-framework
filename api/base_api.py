import logging
import requests

logger = logging.getLogger(__name__)

class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def send_request(self, method, endpoint, params=None, data=None, headers=None, json=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending {method} request to {url}")
        if json:
            logger.info(f"Request Payload: {json}")

        response = self.session.request(
            method=method, url=url, params=params, data=data, headers=headers, json=json
        )

        logger.info(f"Response Code: {response.status_code}")
        logger.debug(f"Response Body: {response.text}")

        return response
