

install requirements
1. `pyenv virtualenv 3.12 myenv`
2. `pyenv activate myenv`
3. `pip install -r requirements.txt`
4. set up python path `export PYTHONPATH=$PYTHONPATH:$(pwd)/src` under `buzz/` folder


## Challenge 1
To run the API from the root folder
`uvicorn src.main:app --reload`

To run the test suite
`pytest`

use the `python test.py` file to test the API 


## Challenge 2
from the root folder /buzz
run this script `python challenge2/scraping_script.py `
