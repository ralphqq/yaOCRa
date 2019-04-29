FROM python:3.6

RUN apt-get update && \
    apt-get install tesseract-ocr -y && \
    apt-get clean && \
    apt-get autoremove

WORKDIR /home/ocr-app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY ocr_app.py config.py boot.sh ./

RUN chmod a+x boot.sh

ENV FLASK_APP ocr_app.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]