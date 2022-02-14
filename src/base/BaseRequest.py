from ast import Raise
from requests.exceptions import HTTPError
import requests
from ..config import BaseRequestConfig

class BaseRequest():
    def __init__(self, timeout=BaseRequestConfig.timeout) -> None:
        self._session = None
        self._timeout = timeout
        try:
            self._session = requests.session()
            self._session.headers.update(BaseRequestConfig.headers)
            
        except BaseException as error:
            print(f"Could not create Session Object: { error }")
            exit
        
    @property
    def session_headers(self):
        return self._session.headers
    
    def setCustomHeader(self, header):
        self._session.headers.update(header)
        return print(self._session.headers)
        
    def get(self, url):
        req = self._session.get(url, timeout=self._timeout)
        if req.status_code != 200:
            raise HTTPError(
                f"The HTTP Request failed with status code: {req.status_code} \n at url { req.url }")
        return req.json()
    
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value