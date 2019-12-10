# Murmur
A sample tracking application with python flask and elastic search. The alpha release based on spring data was revamped from scratch based on Flask python.

## Dependencies
* Elasticstore
* Python3
* Flask rest plus
* Venv
* Kibana

### Setup code base
1. Setup venv and python3
2. Clone git repo
3. Run `virtualenv -p `which python3` venv`
4. `source venv/bin/activate`
5. Run `cd <clone_directory>` , run `pip install -r requirements.txt`
6. `python setup.py develop`
7. Run `python murmur.py`
8. Open `http://localhost:8888/api/` for swagger
