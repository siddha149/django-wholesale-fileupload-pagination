from django.http import Http404

"""
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
"""


def validate_file_upload(myfile):
    content_types = ['application/pdf', 'application/zip']
    max_upload_size = 5242880
    content_type = myfile.content_type
    file_size = myfile.size
    if content_type in content_types:
        if file_size > max_upload_size:
            return 'File cannot be uploaded since file size exceeds present upload limit OF 5 MB. Please choose again.'
        else:
            return 'No error'

    else:
        return 'File cannot be uploaded since only .pdf and .zip files allowed. Please choose again.'


def validate_file(file_type,file_size):
    content_types = ['application/pdf', 'application/zip']
    max_upload_size = 5242880
    if file_type in content_types:
        if file_size > max_upload_size:
            return 'File size exceeds present upload limit of 5 MB. Please choose again.'
        else:
            return 'No error'

    else:
        return 'Only .pdf and .zip files allowed. Please choose again.'
