import sys
import os
import unittest
import magic

# Path hack. http://stackoverflow.com/questions/6323860/sibling-package-imports
sys.path.insert(0, os.path.abspath('../chalupas'))
import chalupas
from chalupas import app

class ChalupasTestCase(unittest.TestCase):

    def setUp(self):
        chalupas.app.config['TESTING'] = True

        self.app = chalupas.app.test_client()

    def set_original_document(self, file_name):
        self.original_document_name = file_name
        self.original_document_path = os.path.join('tests/fixtures', self.original_document_name)
        self.original_document = open(self.original_document_path, 'r')

    def tearDown(self):
        pass

    #
    # From HTML
    #

    def test_html_to_md(self):
        """HTML to MD"""

        self.set_original_document('demo.html')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'html',
                    'to': 'md'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'octet-stream' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'text/x-c++'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

    def test_html_to_rst(self):
        """HTML to RST"""

        self.set_original_document('demo.html')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'html',
                    'to': 'rst'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'octet-stream' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'text/x-c'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

    def test_html_to_docx(self):
        """HTML to DOCX"""

        self.set_original_document('demo.html')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'html',
                    'to': 'docx'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

    #
    # From MD
    #

    def test_md_to_html(self):
        """MD to HTML"""

        self.set_original_document('demo.md')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'md',
                    'to': 'html'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'text/html' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'text/html'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

    def test_md_to_rst(self):
        """HTML to RST"""

        self.set_original_document('demo.md')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'md',
                    'to': 'rst'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'octet-stream' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'text/x-c'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

    def test_md_to_docx(self):
        """HTML to DOCX"""

        self.set_original_document('demo.md')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'md',
                    'to': 'docx'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

    #
    # From RST
    #

    def test_rst_to_html(self):
        """RST to HTML"""

        self.set_original_document('demo.rst')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'rst',
                    'to': 'html'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'text/html' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'text/html'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

    def test_rst_to_md(self):
        """RST to MD"""

        self.set_original_document('demo.rst')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'rst',
                    'to': 'md'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'octet-stream' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'text/plain'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []


    def test_rst_to_docx(self):
        """RST to DOCX"""

        self.set_original_document('demo.rst')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'rst',
                    'to': 'docx'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

    #
    # From DOCX
    #

    def test_docx_to_html(self):
        """DOCX to HTML"""

        self.set_original_document('demo.docx')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'docx',
                    'to': 'html'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'text/html' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'text/html'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []


    def test_rst_to_html(self):
        """RST to HTML"""

        self.set_original_document('demo.rst')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'rst',
                    'to': 'html'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'text/html' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'text/html'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

    def test_docx_to_md(self):
        """DOCX to MD"""

        self.set_original_document('demo.docx')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'docx',
                    'to': 'md'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'octet-stream' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'text/plain'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

    def test_docx_to_rst(self):
        """DOCX to RST"""

        self.set_original_document('demo.docx')

        response = self.app.post('/convert/',
                buffered=True,
                content_type='multipart/form-data',
                data={
                    'document': (self.original_document, self.original_document_name),
                    'from': 'docx',
                    'to': 'rst'
                })

        destination_document = response.data

        assert '200' in response.status
        assert 'octet-stream' in response.content_type
        assert magic.from_buffer(destination_document, mime=True) == 'text/plain'
        assert os.listdir(app.config['CONVERSION_FOLDER']) == []

if __name__ == '__main__':
    unittest.main()
