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
ENV FLASK_ENV=production
ARG SECRET_KEY
ARG RECAPTCHA_PUBLIC_KEY
ARG RECAPTCHA_PRIVATE_KEY
ARG TESTING
ARG LOG_TO_STDOUT

EXPOSE 5000

# Uncomment when not running on Heroku
#ENTRYPOINT ["./boot.sh"]

# Comment if not running on Heroku
CMD gunicorn --bind 0.0.0.0:$PORT ocr_app:app
