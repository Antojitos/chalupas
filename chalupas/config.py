import string
import os

BASE_DIR=os.path.abspath(os.path.join(
                           os.path.dirname(__file__), '..'))

HOST='0.0.0.0'
PORT=5000

CONVERSION_FOLDER=os.path.join(BASE_DIR, 'files')

PANDOC_CONFIGS=[
    { # From HTML
        'from_extension': 'html',
        'from_format': 'html',
        'to_extension': 'docx',
        'to_format': 'docx',
        'extra_args': []
    },
    {
        'from_extension': 'html',
        'from_format': 'html',
        'to_extension': 'md',
        'to_format': 'markdown',
        'extra_args': []
    },
    {
        'from_extension': 'html',
        'from_format': 'html',
        'to_extension': 'rst',
        'to_format': 'rst',
        'extra_args': []
    },
    { # From MD
        'from_extension': 'md',
        'from_format': 'markdown',
        'to_extension': 'html',
        'to_format': 'html',
        'extra_args': []
    },
    {
        'from_extension': 'md',
        'from_format': 'markdown',
        'to_extension': 'docx',
        'to_format': 'docx',
        'extra_args': []
    },
    {
        'from_extension': 'md',
        'from_format': 'markdown',
        'to_extension': 'rst',
        'to_format': 'rst',
        'extra_args': []
    },
    { # From RST
        'from_extension': 'rst',
        'from_format': 'rst',
        'to_extension': 'html',
        'to_format': 'html',
        'extra_args': []
    },
    {
        'from_extension': 'rst',
        'from_format': 'rst',
        'to_extension': 'md',
        'to_format': 'md',
        'extra_args': []
    },
    {
        'from_extension': 'rst',
        'from_format': 'rst',
        'to_extension': 'docx',
        'to_format': 'docx',
        'extra_args': []
    },
    { # From DOCX
        'from_extension': 'docx',
        'from_format': 'docx',
        'to_extension': 'html',
        'to_format': 'html',
        'extra_args': [
            '--self-contained',
        ]
    },
    {
        'from_extension': 'docx',
        'from_format': 'docx',
        'to_extension': 'md',
        'to_format': 'md',
        'extra_args': []
    },
    {
        'from_extension': 'docx',
        'from_format': 'docx',
        'to_extension': 'rst',
        'to_format': 'rst',
        'extra_args': []
    }
]
