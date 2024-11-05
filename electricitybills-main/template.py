# Import the necessary libraries 
import os
from pathlib import Path

# Define the package name 
package_name = "ElectricityBill"

# List the files to be created 
list_of_files = [
    Path(".github") / "workflows" / ".gitkeep", # github workflow directory
    f"src/__init__.py", 
    f"src/{package_name}/__init__.py", 
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/c_01_data_ingestion.py",
    f"src/{package_name}/components/c_02_data_validation.py",
    f"src/{package_name}/components/c_03_data_transformation.py",
    f"src/{package_name}/components/c_04_model_trainer.py",
    f"src/{package_name}/utils/__init__.py", 
    f"src/{package_name}/utils/commons.py", 
    f"src/{package_name}/config/__init__.py", 
    f"src/{package_name}/config/configuration.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/p_01_data_ingestion.py",
    f"src/{package_name}/pipelines/p_02_data_validation.py",
    f"src/{package_name}/pipelines/p_03_data_transformation.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/entity/configuration_entity.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/logger.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "setup.py",
    "requirements.txt",
    "research/trials.py",
    "templates/home.html",
    "templates/index.html"
]

# Loop through each file in the list 
for filepath in list_of_files:
    filepath = Path(filepath)

    # Split the filepath into a directory and filename 
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist 
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create an empty file if it doesn't exist or if empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath, 'w') as f:
            pass

