# Synthetic Data Hub
These Python scripts generates new sample data. 


## Creating a Virtual Python Environment
Follow these steps to create a virtual Python environment and use it to install the necessary packages from a `requirements.txt` file. This method ensures that all required dependencies are managed efficiently and isolated from other projects.


Step 1: Create a virtual environment  
`python -m venv myenv`
  
Step 2: Activate the virtual environment  
On macOS/Linux  
`source myenv/bin/activate`

On Windows  
`myenv\Scripts\activate` 
  
Step 3: Install required packages using requirements.txt  
`pip install -r requirements.txt`  
  
Step 4: Verify installation  
`pip list`  

Step 5: Run the scripts to generate 100 records of en-US data as default  
 `python scriptname.py` 

Optionally, you can specify the following arguments to change the locale and number of records
 `python scriptname.py --locale en_AU --records 1000` 


Step 6: "Optional" Deactivate the virtual environment when done  
`deactivate` 
