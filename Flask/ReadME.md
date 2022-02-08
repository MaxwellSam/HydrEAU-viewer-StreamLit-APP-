# Flask 
## running a flask app
### Dev mode in powershell
`$env:FLASK_APP = "app"`
`$env:FLASK_ENV = "development"`
`python -m flask run`
## Project content
- `API_test_1`
  - apply.py: the API application source code
  - data.py: script for local data loading and preparation
  -  main.py: testing request on API 
  -  notebook.ipynb: laboratory for data manipulation (testing things before implementation)