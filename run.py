from chalupas import app

app.debug = True
app.run(host=app.config['HOST'], port=app.config['PORT'])
