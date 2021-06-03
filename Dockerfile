
FROM python:latest

RUN apt-get update
RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-deu \
    libgl1-mesa-dev; 
RUN apt-get clean

RUN pip install --upgrade pip; \
    pip install \
    pillow \
    opencv-python \
    pytesseract \
    meilisearch \
    pandas

ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]