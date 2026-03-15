import os
from pathlib import Path #pathlib is a modern way to handle file paths.
import logging  #logging module is used to track program execution.
logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]: %(message)s:') 

project_name = "textSummarizer"

list_of_files = [".github/workflows/.gitkeep",
                 f"src/{project_name}/__init__.py",
                 f"src/{project_name}/conponents/__init__.py",
                 f"src/{project_name}/utils/__init__.py",
                 f"src/{project_name}/utils/common.py",
                 f"src/{project_name}/logging/__init__.py",
                 f"src/{project_name}/config/__init__.py",
                 f"src/{project_name}/config/configuration.py",
                 f"src/{project_name}/pipeline/__init__.py",
                 f"src/{project_name}/entity/__init__.py",
                 f"src/{project_name}/constants/__init__.py",
                 "config/config.yaml",
                 "params.yaml",
                 "app.py",
                 "main.py",
                 "Dockerfile",
                 "requirementes.txt",
                 "setup.py",
                 "resaerch/trials.ipynb",
                 "test.py"
                 ]
for i in list_of_files:
    i = Path(i)
    filedir,i = os.path.split(i) 

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"creating directory:{filedir} for the filev{i}")

    if (not os.path.exists(i)) or (os.path.getsize(i) == 0):
        with open(i,'w') as f:
            pass
            logging.info(f"creating empty file:{i}")

    else:
        logging.info(f"{i} is already exists")