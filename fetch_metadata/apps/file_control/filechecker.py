from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from storages.backends.s3boto3 import S3Boto3Storage

class ContentTypeRestrictedFileField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB - 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types", [])
        self.max_upload_size = kwargs.pop("max_upload_size", 0)

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        """
        Validates the file to ensure seamless flow

        Raises:
            forms.ValidationError: If filetype is not among the ones listed
            forms.ValidationError: When the filetype is larger than specified in the models

        Returns:
            the uploaded file
        """
        data = super().clean(*args, **kwargs)

        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file.size > self.max_upload_size:
                    raise forms.ValidationError('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file.size))
            else:
                raise forms.ValidationError('Filetype not supported.')
        except AttributeError:
            pass

        return data






# class MediaStorage(S3Boto3Storage):
    # bucket_name = 'my-app-bucket'
    # location = 'media'

# class StaticStorage(S3Boto3Storage):
    # bucket_name = 'my-app-bucket'
    # location = 'static'
