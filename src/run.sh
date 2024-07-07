# sudo apt install python3.10-venv

#!/bin/bash
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the dependencies from requirements.txt
pip install -r requirements.txt

# Run the main application
python3 main.py

# Deactivate the virtual environment
deactivate