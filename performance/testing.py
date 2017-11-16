from .page_performance import PagePerformance

message = {'no_urls': "We need an URL of the page to test,\n" +
                      "for example 'https://example.com'.\n\n" +
                      "Also there can be multiple urls, separated by comma,\n" +
                      "for example: https://example1.com https://example2.com https://example3.com\n\n" +
                      "Also urls of the page can be read from the file 'file_with_urls.txt'"
                      "Please, retry ...",
           'using_urls_from_file': "We've got urls from the file 'file_with_urls.txt'",
           'test_results': "\n{:-^80}\n".format(" Results of performance testing "),
           }


def testing(urls_to_test):
    """
    Provides the process of performance testing
    """
    for i in urls_to_test:
        test_result = PagePerformance(i).performance_adequacy()
        print("{:-^80}".format(" " + i + " "))
        print("  - mobile performance: {value}/100 {de} {status}".format(
            value=test_result["mobile"][2],
            de='{:.<41}'.format(""),
            status=test_result["mobile"][1]))
        print("  - desktop performance: {value}/100 {de} {status}\n".format(
            value=test_result["desktop"][2],
            de='{:.<40}'.format(""),
            status=test_result["desktop"][1]))