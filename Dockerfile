FROM python:2.7-alpine

COPY set-sg-desc.py /bin
COPY requirements.txt /

RUN /bin/sh -c 'pip install -r /requirements.txt'

ENTRYPOINT ["set-sg-desc.py"]
