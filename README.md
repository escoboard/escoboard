# Escoboard
Web-UI for visualizing results

### Install dependencies
```
$ pip install -r requirements.txt
```

### Set `summary` folder path
Edit `SUMMARY_PATH` in `runserver.py` file 
```
SUMMARY_PATH = '/path/to/summary'
```

### Run
```
$ export FLASK_APP=runserver.py
$ flask run --host=0.0.0.0
```

Open link [0.0.0.0:5000](http://0.0.0.0:5000/)
