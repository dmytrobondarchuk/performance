# -*- coding: utf-8 -*-
import requests


class PageSpeed:
    """
    Performance analysis. It uses Google PageSpeed API under the hood.

    Example of usage:
        test = PageSpeed("https://example.com/")

        print("Status code:", test.status_code())
        print("ID:", test.id())
        print("Title:", test.title())
        print("Speed:", test.speed())
        print("Usability:", test.usability())
    """

    def __init__(self, url, strategy):
        self.url = url
        self.strategy = strategy  # mobile, desktop
        self.res = requests.get('https://www.googleapis.com/pagespeedonline/v2/runPagespeed',
                                params={'url': self.url,
                                        'strategy': self.strategy,
                                        'key': "AIzaSyBXODcaGIeQDWqalKJTyzxOdqFbgAR8Vr8"})

    def status_code(self):
        """
        Returns Status Code of the response
        :return: status code:  int
        """
        return self.res.json()["responseCode"]

    def id(self):
        """
        Returns ID (url of the page under test)
        :return: ID: str
        """
        return self.res.json()["id"]

    def title(self):
        """
        Returns Title of the page under test
        :return: title: str
        """
        return self.res.json()["title"]

    def speed(self):
        """
        Returns Speed score for the page under test (score = 0...100)
        :return: speed score:  int
        """
        return self.res.json()["ruleGroups"]["SPEED"]["score"]

    def usability(self):
        """
        Returns Usability score for the page under test (score = 0...100)
        :return:
        """
        if self.strategy == "mobile":
            return self.res.json()["ruleGroups"]["USABILITY"]["score"]

        else:
            return None


if __name__ == '__main__':
    pass
