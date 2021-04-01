import requests as requests
from termcolor import colored
import sys as sys

from .error import SearchError

class UpdateApplication(object):
    def __init__(self, current_version):
        self.current_version = current_version
        self.release_api_url = "https://api.github.com/repos/IndianOpenSourceFoundation/dynamic-cli/releases/latest"

        self.check_for_updates()

    def check_for_updates(self):
        try:
            data = requests.get(self.release_api_url)
            data = data.json()
        
            if 'message' in data:
                if data['message'] == "Not Found":
                    print(colored("The application do not have any release", "yellow"))
                    return None

            if data.tag_name == self.current_version:
                print(colored("Yeah! You have the latest version", "green"))
            else:
                print(colored(f"New release found - {data.tag_name}", "red"))
            
        except Exception as exception:
            exception = SearchError(str(exception), "Try later")
