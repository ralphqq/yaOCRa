import os
import sys
import uuid

from flask import render_template, redirect, url_for, flash, \
    request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

from app import app
from app.forms import UploadPhotoForm
from app.utils.ocr import extract_text

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadPhotoForm()
    if form.validate_on_submit():
        f = form.file_name.data
        img_prep = form.prep_method.data

        fname = secure_filename(f.filename)
        filename = '-'.join([str(uuid.uuid4().hex)[:16], fname])
        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )
        f.save(filepath)
        return redirect(url_for('results', fp=filepath, img_prep=img_prep))

    return render_template('index.html', title='Extract text from image',
                           form=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
    filepath = request.args.get('fp')
    img_prep = request.args.get('img_prep')
    text = extract_text(filepath, img_prep)

    if os.path.exists(filepath):
        os.remove(filepath)

    return render_template('output.html', title='Results', text=text)


@app.route('/download_as_file', methods=['POST'])
def download_as_file():
    text = request.form.get('text')

    fname = '-'.join([str(uuid.uuid4().hex)[:16], 'yaOCRa.txt'])
    fpath = os.path.join(app.config['UPLOAD_FOLDER'], fname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(text)

    return redirect(url_for('download', filename=fname))


@app.route('/tmp/<filename>')
def download(filename):
    return send_from_directory(
        directory=app.config['DOWNLOAD_DIR'],
        filename=filename,
        as_attachment=True
    )
    return redirect(url_for('index'))
