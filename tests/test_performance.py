import pytest
from ..performance import PagePerformance


@pytest.mark.parametrize("test_url", ("https://example.com", ))
class TestPerformance:
    def test_desktop(self, test_url):
        """Testing desktop performance metering"""
        test_page = PagePerformance(test_url)
        assert test_page.desktop_performance()["status_code"] == 200
        assert test_page.desktop_performance()["speed"] == 100

    def test_mobile(self, test_url):
        """Testing mobile performance metering"""
        test_page = PagePerformance(test_url)
        assert test_page.mobile_performance()["status_code"] == 200
        assert test_page.mobile_performance()["speed"] == 100
