# yaOCRa
The acronym yaOCRa stands for "yet another OCR app" which basically describes what this app is all about.


## Dependencies
yaOCRa uses pytesseract, Flask, and [clipboard.js](https://github.com/zenorocha/clipboard.js) a third-party Javascript library for copying browser text to the clipboard.

For a full list of dependencies, please see the project's `requirements.txt` file.


## Running yaOCRa on Local Machine
Some special steps need to be taken to install and run yaOCRa on your local machine.

### Installing Tesseract Binary
First, you need to have the Tesseract binary installed on your machine.

* For macOS users: `$ brew install tesseract`
* For Ubuntu users: `$ sudo apt-get install tesseract-ocr`
* For Windows users: Download [UB Mannheim's unofficial installer](https://github.com/UB-Mannheim/tesseract/wiki) and run it. Note that yu also need to add the path to the Tesseract executable into your `PATH` environment variable.


### Validating Tesseract Installation
To check if you correctly installed Tesseract:

1. Open a terminal
2. Run `tesseract -v`
3. You should now see the version and compatible libraries on your screen. Otherwise, an error occurred.


### Getting reCAPTCHA Keys
yaOCRa uses Google's [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display) verification system. So, [sign up for an account](https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Fwww.google.com%2Frecaptcha%2Fadmin&followup=https%3A%2F%2Fwww.google.com%2Frecaptcha%2Fadmin&flowName=GlifWebSignIn&flowEntry=ServiceLogin) and save the corresponding private and public keys.


### Running the App

1. Clone this repo
2. Run `pip install -r requirements.txt`
3. Create a `.flaskenv` file in the project root (see next section for details)
4. Run `flask run`


## Settings and Environment Variables
You should define the following environment variables in the `.flaskenv` file:

```
FLASK_APP=ocr_app.py
FLASK_ENV=development
FLASK_DEBUG=0
SECRET_KEY=REPLACE_WITH_APPROPRIATE_VALUE_HERE
RECAPTCHA_PUBLIC_KEY=REPLACE_WITH_APPROPRIATE_VALUE_HERE
RECAPTCHA_PRIVATE_KEY=REPLACE_WITH_APPROPRIATE_VALUE_HERE
TESTING=0
```

**Notes:**

* Set `FLASK_ENV` to "production" upon deployment.
* Set `FLASK_DEBUG` to 1 to enable debug mode, but set it to 0 in a production environment.
* Set `TESTING` to 1 in order to disable reCAPTCHA during testing.

## Resources
The following useful resources helped made yaOCRa possible:

* [Installing Tesseract for OCR](https://www.pyimagesearch.com/2017/07/03/installing-tesseract-for-ocr/)
* [Using Tesseract OCR with Python](https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/)

## License
[MIT License](https://opensource.org/licenses/MIT)