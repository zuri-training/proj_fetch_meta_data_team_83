from .exifcreator import create_meta_file
from celery import shared_task


@shared_task()
def create_metadata(input_file):
    return create_meta_file(input_file)




