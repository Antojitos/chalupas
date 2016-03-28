from flask import g, request, send_from_directory
from werkzeug import FileStorage
from io import StringIO
from chalupas import app
from chalupas.models import Document
from chalupas.tools import random_string

def after_this_request(func):
    if not hasattr(g, 'call_after_request'):
        g.call_after_request = []
    g.call_after_request.append(func)
    return func

@app.after_request
def per_request_callbacks(response):
    for func in getattr(g, 'call_after_request', ()):
        response = func(response)
    return response

@app.route('/convert/', methods=['POST'])
def convert_document():
    if (request.files.get('document')):
        document=Document(request.files.get('document'))
    elif (not request.files.get('document') and
        request.form.get('document')):
        document=Document(FileStorage(
            StringIO(request.form.get('document')),
            '{name}.{extension}'.format(
                name=random_string(),
                extension=request.form.get('from'))
        ))

    mime_type=document.convert(request.form.get('from'), request.form.get('to'))

    @after_this_request
    def delete_document_files(response):
        document.delete_files()
        return response

    return send_from_directory(
        document.converted_file_directory,
        document.converted_file_name,
        mimetype=mime_type)
