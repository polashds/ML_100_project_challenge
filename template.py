import os
from pathlib import Path

project_name = "ML_100_project"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/datasets/__init__.py",
    f"{project_name}/datasets/raw_data/__init__.py",
    f"{project_name}/datasets/processed_data/__init__.py",
    f"{project_name}/datasets/external_data/__init__.py",
    f"{project_name}/notebooks/__init__.py",
    f"{project_name}/notebooks/data_analysis.ipynb",
    f"{project_name}/notebooks/feature_enineering.ipynb",
    f"{project_name}/src/__init__.py",
    f"{project_name}/src/data/__init__.py",
    f"{project_name}/src/models/__init__.py",
    f"{project_name}/src/utils/__init__.py",
    f"{project_name}/src/visualizaton/__init__.py",
    f"{project_name}/test/__init__.py",
    "requirements.txt",
    ".gitignore",
    "README.md",
    "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath, "w") as f:
            pass
    else:
        print(f"File {filename} already exists")
