FROM python:latest

RUN apt update
RUN apt -y install \
    tesseract-ocr \
    tesseract-ocr-jpn \
    libgl1-mesa-dev;
RUN apt-get clean

COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt

# ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]