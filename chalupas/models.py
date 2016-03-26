import os

import pypandoc

from chalupas import app
from chalupas.tools import save_file_to_disk, get_mimetype, get_pandoc_config

class Document(object):

    def __init__(self, file):
        self.file_name=file.filename
        self.file_directory = app.config['CONVERSION_FOLDER']
        self.converted_file_directory=app.config['CONVERSION_FOLDER']

        save_file_to_disk(
            file,
            os.path.join(self.file_directory, self.file_name))

    def convert(self, from_extension, to_extension):
        config=get_pandoc_config(from_extension, to_extension)

        self.converted_file_name='{filename}.{extension}'.format(
            filename=self.file_name,
            extension=config['to_extension'])
        file_path=os.path.join(self.file_directory, self.file_name)
        converted_file_path=os.path.join(
            self.converted_file_directory,
            self.converted_file_name)

        pypandoc.convert(
            source=file_path,
            format=config['from_format'],
            to=config['to_format'],
            outputfile=converted_file_path,
            extra_args=config['extra_args'])

        return get_mimetype(converted_file_path)

    def delete_files(self):
        os.remove(os.path.join(
            self.file_directory,
            self.file_name))
        os.remove(os.path.join(
            self.converted_file_directory,
            self.converted_file_name))
