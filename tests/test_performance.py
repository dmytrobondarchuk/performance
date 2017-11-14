import pytest
import os
from ..performance import PagePerformance
from ..performance import get_urls_from_file


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


class TestInputFromFile:
    """Test Suite for the cases related to url input functionality. """
    expected_urls_one = ['http://example.com/',
                         'https://www.python.org/', 'https://www.wikipedia.org/',
                         'https://en.wikipedia.org/wiki/Behavior-driven_development']

    @pytest.mark.parametrize("path_to_test_file_with_urls", ("tests/test_file_with_urls_one.txt", ))
    def test_read_urls_from_file(self, path_to_test_file_with_urls):
        """Valid urls are fed from the file."""
        urls_from_file = get_urls_from_file(path_to_test_file_with_urls)

        assert urls_from_file == self.expected_urls_one

    @pytest.mark.parametrize('path_to_absent_file', ("tests/nofile.txt", ))
    def test_no_file_with_urls(self, path_to_absent_file):
        """There are no file with urls. """
        with pytest.raises(FileNotFoundError):
            assert get_urls_from_file(path_to_absent_file)


# TODO: Replace single '@pytest.mark.parametrize' fixture by several one separately for '--urls' and '--file' arguments.


class TestInputArgs:
    """Test Suite for testing cases with command line argumets. """
    @pytest.mark.parametrize("command_line", (
            "python performance.py",
            "python performance.py --urls",
            "python performance.py --urls http://example.com",
            "python performance.py --file",
            "python performance.py --file test_file_with_urls_one.txt",
            "python performance.py --file test_file_with_urls_one.txt test_file_with_urls_one.txt",
            "python performance.py --urls --file",
            "python performance.py --urls http://example.com --file test_file_with_urls_one.txt"))
    def test_valid_input_args(self, command_line):
        """Test Suite to test input args. """
        pass
