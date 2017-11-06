import pytest
from ..performance import PagePerformance


@pytest.mark.parametrize("test_url", ("https://example.com", ))
class TestPerformance:
    def test_desktop(self, test_url):
        """Testing desktop performance metering"""
        test_page = PagePerformance(test_url)
        assert test_page.desktop_performance()["status_code"] == 200
        assert test_page.desktop_performance()["speed"] == 100
        with pytest.raises(KeyError):
            print(test_page.desktop_performance()["usability"])

    def test_mobile(self, test_url):
        """Testing mobile performance metering"""
        test_page = PagePerformance(test_url)
        assert test_page.mobile_performance()["status_code"] == 200
        assert test_page.mobile_performance()["speed"] == 100
        assert test_page.mobile_performance()["usability"] == 100


@pytest.mark.parametrize("test_url", ("https://example.com", ))
class TestPerformanceCustomized:
    def test_mobile(self, test_url):
        """Testing the case of mobile performance metering only"""
        test_page = PagePerformance(test_url, strategy='mobile')
        assert test_page.mobile_performance()["status_code"] == 200
        with pytest.raises(AttributeError):
            print(test_page.desktop_performance()["status_code"])

    def test_desktop(self, test_url):
        """Testing the case of desktop performance metering only"""
        test_page = PagePerformance(test_url, strategy='desktop')
        assert test_page.desktop_performance()["status_code"] == 200
        with pytest.raises(AttributeError):
            print(test_page.mobile_performance()["status_code"])

    def test_another(self, test_url):
        """Testing the case of unforeseen key"""
        test_page = PagePerformance(test_url, strategy='tytyutyutyut')

        assert test_page.mobile_performance()["status_code"] == 200
        assert test_page.desktop_performance()["status_code"] == 200
