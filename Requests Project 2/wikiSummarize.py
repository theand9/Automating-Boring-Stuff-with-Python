import sys
import nltk
import pyperclip
import requests
from requests.exceptions import HTTPError


def getData(url, srch_Str):

    try:
        web_Response = requests.get(url + srch_Str)
        web_Response.raise_for_status()

    except HTTPError as HTTP_ERROR:
        print(f"An HTTP error has occurred: {HTTP_ERROR}")

    except Exception as Other_ERROR:
        print(f"Some Other Error has occurred: {Other_ERROR}")


def dataSummarize(web_Data):
    pass


def automateProc():
    pass


if __name__ == "__main__":

    url = "https://en.wikipedia.org/wiki/"
    getData(url, pyperclip.paste())
