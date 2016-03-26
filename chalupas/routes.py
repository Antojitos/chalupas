from flask import g, request, send_from_directory
from chalupas import app
from chalupas.models import Document

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
    document = Document(request.files.get('document'))
    mime_type=document.convert(request.form.get('from'), request.form.get('to'))

    @after_this_request
    def delete_document_converted_file(response):
        document.delete_files()
        return response

    return send_from_directory(
        document.converted_file_directory,
        document.converted_file_name,
        mimetype=mime_type)
