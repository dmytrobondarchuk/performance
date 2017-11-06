# -*- coding: utf-8 -*-
import requests
import sys


class PagePerformance:
    """
    Performance analysis. It uses Google PageSpeed API under the hood.

    Example of usage:
        test = PageSpeed("https://example.com/")

    """
    api_request_url = 'https://www.googleapis.com/pagespeedonline/v2/runPagespeed'
    key = 'AIzaSyBXODcaGIeQDWqalKJTyzxOdqFbgAR8Vr8'

    def __init__(self, url, strategy='all'):
        self.url = url

        if strategy == 'mobile':
            self.res_mobile = requests.get(self.api_request_url,
                                           params={'url': self.url,
                                                   'strategy': 'mobile',
                                                   'key': self.key})
        elif strategy == 'desktop':
            self.res_desktop = requests.get(self.api_request_url,
                                            params={'url': self.url,
                                                    'strategy': 'desktop',
                                                    'key': self.key})
        else:
            self.res_mobile = requests.get(self.api_request_url,
                                           params={'url': self.url,
                                                   'strategy': 'mobile',
                                                   'key': self.key})

            self.res_desktop = requests.get(self.api_request_url,
                                            params={'url': self.url,
                                                    'strategy': 'desktop',
                                                    'key': self.key})

    def mobile_performance(self):
        """
        Mobile performance testing
        :return: {'status_code': status code of the response ('int'),
                  'id': url of the page under the performance test ('str'),
                  'title': the title of the page under test ('str'),
                  'speed': speed score of the page under test (score = 0...100, 'int'),
                  'usability': usability (for mobile only) of the page under test (value = 0...100, 'int'),
                   }

        """
        return {'status_code': self.res_mobile.json()["responseCode"],
                'id': self.res_mobile.json()["id"],
                'title': self.res_mobile.json()["title"],
                'speed': self.res_mobile.json()["ruleGroups"]["SPEED"]["score"],
                'usability': self.res_mobile.json()["ruleGroups"]["USABILITY"]["score"],  # for mobile only
                }

    def desktop_performance(self):
        """
        Desktop performance testing
        :return: {'status_code': status code of the response ('int'),
                  'id': url of the page under the performance test ('str'),
                  'title': the title of the page under test ('str'),
                  'speed': speed score of the page under test (score = 0...100, 'int'),
                   }
        """
        return {'status_code': self.res_desktop.json()["responseCode"],
                'id': self.res_desktop.json()["id"],
                'title': self.res_desktop.json()["title"],
                'speed': self.res_desktop.json()["ruleGroups"]["SPEED"]["score"],
                }

    def performance_adequacy(self, admissible_mobile=90, admissible_desktop=90):
        """
        The adequacy of mobile and desktop performance
        :param admissible_mobile: the value of mobile performance that is admissible
        :param admissible_desktop: the value of desktop performance that is admissible
        :return: dictionary {"mobile": mobile_status,
                             "desktop": desktop_status}
        """
        if self.res_mobile.json()["responseCode"] == 200:
            if self.res_mobile.json()["ruleGroups"]["SPEED"]["score"] >= admissible_mobile:
                mobile_status = (True, 'PASSED')
            else:
                mobile_status = (False, 'FAILED')
        else:
            mobile_status = (False, 'ERROR')

        if self.res_desktop.json()["responseCode"] == 200:
            if self.res_desktop.json()["ruleGroups"]["SPEED"]["score"] >= admissible_desktop:
                desktop_status = (True, 'PASSED')
            else:
                desktop_status = (False, 'FAILED')
        else:
            desktop_status = (False, 'ERROR')

        return {"mobile": mobile_status,
                "desktop": desktop_status}


def testing(*args):
    """
    Provides the testing process
    """
    for i in args[0]:
        test_result = PagePerformance(i)
        print("Performance testing {page}:".format(page=i))
        print("  - mobile performance: {value}/100 ............................................. {status}".format(
            value=test_result.mobile_performance()['speed'],
            status=test_result.performance_adequacy()["mobile"][1]))
        print("  - desktop performance: {value}/100 ............................................ {status}\n".format(
            value=test_result.desktop_performance()['speed'],
            status=test_result.performance_adequacy()["desktop"][1]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        page_url = sys.argv[1:]
        testing(page_url)
    else:
        print("We need an URL of the page to test,\n" +
              "for example 'https://example.com'.\n\n" +
              "Also there can be multiple urls, separated by comma,\n" +
              "for example: https://example1.com https://example2.com https://example3.com\n\n" +
              "Please, retry ...")
