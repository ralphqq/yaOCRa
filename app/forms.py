from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField, SelectField, SubmitField


class UploadPhotoForm(FlaskForm):
    """Form for uploading a photo."""
    file_name = FileField(
            'Choose a photo',
            validators=[FileRequired(),
                        FileAllowed(['jpg', 'jpeg', 'gif', 'png', 'tif'],
                                    'Only JPEG, PNG, TIF, and GIF allowed.')]
    )
    prep_method = SelectField(
        'Image preprocessing',
        choices=[
            ('raw', 'None'),
            ('thresh', 'Threshold'),
            ('blur', 'Blur')
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Extract text')
