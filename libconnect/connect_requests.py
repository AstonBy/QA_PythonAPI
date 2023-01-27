import allure
import requests
from requests import api

from lib.logger import Logger


class ConnectRequests:
    # @staticmethod
    # def get(url: str = None, data: dict = None, cookies: dict = None, headers: dict = None):
    #     return ConnectRequests._send(url, data, cookies, headers, "GET")
    #
    # @staticmethod
    # def post(url: str = None, data: dict = None, cookies: dict = None, headers: dict = None):
    #     return ConnectRequests._send(url, data, cookies, headers, "POST")
    #
    # @staticmethod
    # def put(url: str = None, data: dict = None, cookies: dict = None, headers: dict = None):
    #     return ConnectRequests._send(url, data, cookies, headers, "PUT")
    #
    # @staticmethod
    # def delete(url: str = None, data: dict = None, cookies: dict = None, headers: dict = None):
    #     return ConnectRequests._send(url, data, cookies, headers, "DELETE")


    @staticmethod
    def send(method: str, url: str, params: str = None, data: dict = None, json: dict = None, cookies: dict = None, headers: dict = None):
        url = f"https://qa06-connect.stage-twill.health/api/{url}"

        Logger.add_request(url, data, json, headers, cookies, method)
        with allure.step(f"{method} request to URL '{url}'"):
            response = requests.request(method, url, params=params, data=data, json=json, cookies=cookies, headers=headers)

        Logger.add_response(response)
        # if method == "GET":
        #     response = requests.get(url, params=data, cookies=cookies, headers=headers)
        # elif method == "POST":
        #     response = requests.post(url, json=data, cookies=cookies, headers=headers)
        # elif method == "PUT":
        #     response = requests.put(url, data=data, cookies=cookies, headers=headers)
        # elif method == "DELETE":
        #     response = requests.delete(url, data=data, cookies=cookies, headers=headers)

        return response
