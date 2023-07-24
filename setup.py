from setuptools import setup

with open('README.md') as file:
    long_description = file.read()


setup(
    name="chalupas-files",
    version="0.1.1",
    author="Antonin Messinger",
    author_email="antonin.messinger@gmail.com",
    description=" Convert any document",
    long_description=long_description,
    license="MIT License",
    url="https://github.com/Antojitos/chalupas",
    download_url="https://github.com/Antojitos/chalupas/archive/0.1.1.tar.gz",
    keywords=["chalupas", "convert", "document"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],

    packages=['chalupas'],
    install_requires=[
        'Flask==2.2.5',
        'pypandoc==1.1.3'
    ],

    tests_require=[
        'python-magic==0.4.11',
    ],
    test_suite='tests.main'
)
