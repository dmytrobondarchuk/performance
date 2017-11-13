FROM python:3

ADD tests/  /tests
ADD file_with_urls.txt  /
ADD __init__.py  /
ADD performance.py  /
ADD requirements.txt  /

RUN pip install -r requirements.txt

CMD ["/bin/bash", "-l"]

