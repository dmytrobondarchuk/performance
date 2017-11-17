"""Settings"""


# Google API settings:.
google_api_key = 'AIzaSyBXODcaGIeQDWqalKJTyzxOdqFbgAR8Vr8'
api_request_url = 'https://www.googleapis.com/pagespeedonline/v2/runPagespeed'


# Admissible value of page performance for the 'mobile' and the 'desktop' testing strategies
performance_acceptance_criteria = dict(
    mobile=75,
    desktop=75,
)


# Default paths:

default_path = dict(
    example_dir='',
    example_file=''
)
