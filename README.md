# Requirements
- python 3.9

# Setup
```shell
pip install -r requirements.txt
```

# Run a project 6_1
```shell
source var.sh
python python 6_selenium_projects/testing_project/dutchword_translator_bot/dutchword_translator_bot.py
```
# Run a project 7_1_flask_basics
```shell
export FLASK_APP="/Users/wentungwen/Desktop/python_practice/7_flask_projects/7_1_flask_basics/hello.py"
source var.sh
flask run
```


# Deactivate/activate environment
It is suggested to use Anaconda managing and building the environment.

- Create the environments.
```shell
conda create -n py_practice python=3.9
```

- Activate/deactivate environments.
```shell
conda activate py_practice
conda deactivate
```

- Show and remove the environment.
```shell
conda env list 
conda remove --name 5_8_amazon  --all
```

