$env:FLASK_ENV = "development"
$env:FLASK_APP = "src"
python -m flask db init
