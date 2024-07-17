FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get upgrade \
    && apt-get install -y --no-install-recommends \
    wget \
    python3-pip 

RUN wget https://github.com/pdf2htmlEX/pdf2htmlEX/releases/download/v0.18.8.rc1/pdf2htmlEX-0.18.8.rc1-master-20200630-Ubuntu-focal-x86_64.deb \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 


RUN apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && apt install ./pdf2htmlEX-0.18.8.rc1-master-20200630-Ubuntu-focal-x86_64.deb -y 

RUN rm pdf2htmlEX-0.18.8.rc1-master-20200630-Ubuntu-focal-x86_64.deb \
    && rm google-chrome-stable_current_amd64.deb 

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt


WORKDIR /code

COPY . .
RUN pip install --no-cache-dir -r requirements.txt 

RUN mkdir media


EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]