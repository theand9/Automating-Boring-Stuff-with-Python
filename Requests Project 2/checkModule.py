import sys
import re
import subprocess
import requests
from requests.exceptions import HTTPError
import bs4


def webRequest(*args):
    """Basic Web Request and url builder.

    Returns:
        response object -- containing output of webpage
        None -- if error occurs
    """
    url = "".join(args)

    try:
        web_Response = requests.get(url)
        web_Response.raise_for_status()

        return web_Response

    except HTTPError as HttpError:
        print(f"An HTTP error has occurred: {HttpErro}")

    except Exception as OtherError:
        print(f"Some Other Error has occurred: {OtherError}")

    return None


def getPage(module_Name):
    """Web Scraping to Obtain Final Download Link.

    Arguments:
        module_Name {String} -- Module User wishes to install

    Returns:
        response object -- final webpage response
        string -- channel name

        None -- if no valid download found
    """
    url1 = "https://anaconda.org/search?q="
    web_Response = webRequest(url1, module_Name)

    scrape_Data = bs4.BeautifulSoup(web_Response.text, 'html.parser')
    select_Data1 = scrape_Data.select(
        "#search > div:nth-child(3) > div > div:nth-child(1) \
        > div > table > tbody > tr > td > h5 > a:nth-child(1)")
    select_Data2 = scrape_Data.select(
        "#search > div:nth-child(3) > div > div:nth-child(1) > div \
         > table > tbody > tr > td > h5 > a:nth-child(2) > strong")

    if (select_Data2 or select_Data1) == []:
        print(f"\nThe module {module_Name} is not available from any \
                 valid channel\n")
        sys.exit()

    url2 = "https://anaconda.org/"
    i, regex_Match = 0, select_Data2[0].text.strip()
    channel_List = ['conda-forge', 'anaconda', 'main', 'auto']

    while True:
        try:
            if re.match(regex_Match, select_Data2[i].text.strip()):
                for channel in channel_List:
                    if select_Data1[i].text.strip() == channel:
                        web_Response = webRequest(url2 + channel + "/" +
                                                  module_Name)

                        if web_Response is not None:
                            return web_Response, select_Data1[i].text.strip()

            i += 1

        except IndexError:
            return None


def getLink(web_Response):
    """Retrieves Final Download Command.

    Arguments:
        web_Response {response object} -- gives final webpage response object

    Returns:
        string -- final download command
    """
    scrape_Data = bs4.BeautifulSoup(web_Response.text, 'html.parser')
    select_Cmd = scrape_Data.select(
        "body > div.container > div:nth-child(2) > div > div:nth-child(4) \
             > div > div:nth-child(2) > div:nth-child(3) > code:nth-child(4)")

    return select_Cmd[0].text.strip()


if __name__ == "__main__":

    module_Name = input("Enter the module you wish to search for: ")
    next_Link, channel = getPage(module_Name)

    install_Link = getLink(next_Link)
    print(f"The module {module_Name} is available from channel {channel}. \
            \nInstallation will start now.\n")

    # To run directly on Shell
    subprocess.run(install_Link.split(), check=True)
