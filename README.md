# chalupas

[![Build Status](https://travis-ci.org/Antojitos/chalupas.svg?branch=master)](https://travis-ci.org/Antojitos/chalupas)

Convert any document.

## Installation

`python setup.py install`

## Run the app

`python run.py`

or using [gunicorn](http://gunicorn.org/):

`gunicorn chalupas:app`

## API

### Convert a document

#### Endpoint

`POST /convert/`

  Parameter   |          Type        | Required
------------- | -------------------- | --------
  document    |    file  or string   |   yes
  from        |        string        |   yes
  to          |        string        |   yes

#### Examples

##### Request

- From file

`curl -F "document=@tests/fixtures/demo.docx" --form "from=docx" --form "to=html" 127.0.0.1:5000/convert/`

- From string

`curl -F "document=#This is a test" --form "from=md" --form "to=docx" 127.0.0.1:5000/convert/`

##### Response

file

## Conversion Table

|      | HTML | MD  | RST | DOCX |
|------|------|-----|-----|------|
| HTML | x    | yes | yes | yes  |
| MD   | yes  | x   | yes | yes  |
| RST  | yes  | yes | x   | yes  |
| DOCX | yes  | yes | yes | x    |

## Tests

`python setup.py test`


## Deployment

Before start to deploying you need to have root access into a remote
server using SSH with a public key.

Install [ansible](<http://docs.ansible.com/ansible/intro_installation.html>) and run:

```shell
cp deploy/hosts.example hosts
vim hosts # add your remote server
ansible-playbook -i hosts deploy/site.yml
```
