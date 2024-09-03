# Synthetic Data Hub

These Python scripts generate new sample data.

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

## Running the `files_generator.py` Script

The `files_generator.py` script automates running multiple `.py` files in the current directory. It allows you to run each script multiple times, passing specific arguments like `--locale` and `--records`.

### Usage

Run the `files_generator.py` script with the following options:

`python files_generator.py --locale en_US --runs 5 --records 1000 --random`

### Arguments
 `--locale` : Specifies the locale argument to pass to the scripts. 
 
 `--runs` : Number of times to run each script. 
 
 `--records` : Maximum number of records to create. 
 
 `--random` : Use a random number of records between 1 and --records if specified. If --random is not provided, it will use the value of --records. 

### Examples

#### Run with Random Records:


`python files_generator.py --locale en_US --runs 5 --records 1000 --random`

This will run each .py file 5 times, passing --locale en_US and a random number of records between 1 and 1000 to each run.

#### Run with Fixed Records:

`python files_generator.py --locale en_US --runs 5 --records 1000`

This will run each .py file 5 times, passing --locale en_US and --records 1000 to each run.
