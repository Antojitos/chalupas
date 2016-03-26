# chalupas ![Build Status](https://travis-ci.org/Antojitos/chalupas.svg?branch=master)

Convert any document.

## Installation

`python setup.py install`

## Run the app

`python run.py`

or using [gunicorn](http://gunicorn.org/):

`gunicorn chalupas:app`

## API

### Post a file

#### Endpoint

`POST /convert/`

  Parameter   |    Type    | Required
------------- | ---------- | --------
  document    |    file    |   yes
   format     |   string   |   yes

#### Example

##### Request

`curl -F "file=@tests/fixtures/demo.docx" --form "from=docx" --form "to=html" 127.0.0.1:5000/convert/`

##### Response

file

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
