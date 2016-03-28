import os
import hashlib
import mimetypes
import random
import string

from chalupas import app

def get_mimetype(file_path):
    mimetypes.init()
    return mimetypes.guess_type(file_path)[0]

def reset_file(file):
    file.stream.seek(0)

def random_string(size=12):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))

def save_file_to_disk(file, file_path):
    file_folder = os.path.dirname(file_path)

    if not os.path.exists(file_folder):
        os.makedirs(file_folder)

    reset_file(file)
    file.save(file_path)

def get_pandoc_config(from_extension, to_extension):
    config=None

    for c in app.config['PANDOC_CONFIGS']:
        if (c['from_extension']==from_extension and
            c['to_extension']==to_extension):
            return c

    raise Exception('Unsupported format', from_extension, to_extension)
