# -*- coding: utf-8 -*-
"""Tool for web-application performance analysis. It's based on Google's PageSpeed."""

import requests
from performance import settings


class PagePerformance:
    """
    Performance analysis. It uses Google PageSpeed API under the hood.

    Examples of usage:

        from performance.page_performance import PageSpeed

        test_mobile = PageSpeed("https://example.com/").mobile_performance() # returns the value of mobile performance
        test_desktop = PageSpeed("https://example.com/").desktop_performance() # returns the value of desktop performance

        assert test_mobile >= 85
        assert test_desktop >= 75

        test_page = PageSpeed("https://example.com').performance_adequacy(admissible_mobile=85, admissible_desktop=80)

        assert test_page["mobile"]
        assert test_page["desktop"]
    """

    api_request_url = settings.api_request_url
    key = settings.google_api_key

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

    def performance_adequacy(self, admissible_mobile=settings.performance_acceptance_criteria['mobile'],
                             admissible_desktop=settings.performance_acceptance_criteria['desktop']):
        """
        The adequacy of mobile and desktop performance
        :param admissible_mobile: the value of mobile performance that is admissible
        :param admissible_desktop: the value of desktop performance that is admissible
        :return: dictionary {"mobile": mobile_status,
                             "desktop": desktop_status}
        """
        if self.res_mobile.status_code == 200:
            value_mobile = self.res_mobile.json()["ruleGroups"]["SPEED"]["score"]
            if value_mobile >= admissible_mobile:
                mobile_status = (True, 'PASSED', value_mobile)
            else:
                mobile_status = (False, 'FAILED', value_mobile)
        else:
            value_mobile = 0
            mobile_status = (False, 'ERROR', value_mobile)

        if self.res_desktop.status_code == 200:
            value_desktop = self.res_desktop.json()["ruleGroups"]["SPEED"]["score"]
            if value_desktop >= admissible_desktop:
                desktop_status = (True, 'PASSED', value_desktop)
            else:
                desktop_status = (False, 'FAILED', value_desktop)
        else:
            value_desktop = 0
            desktop_status = (False, 'ERROR', value_desktop)

        return {"mobile": mobile_status,
                "desktop": desktop_status}


__author__ = "Dmytro Bondarchuk"
__version__ = "0.2.3"
