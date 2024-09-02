import os
import random
import subprocess
import argparse

def run_file(file_name, locale, num_runs, max_records, use_random):
    for _ in range(num_runs):
        if use_random:
            records = random.randint(1, max_records)
        else:
            records = max_records
        subprocess.run(["python3", file_name, "--locale", locale, "--records", str(records)])

def main():
    parser = argparse.ArgumentParser(description="Run all genegrate synthetic date .py files with specified arguments.")
    parser.add_argument("--locale", default="en_US", help="Locale argument to pass to the scripts.")
    parser.add_argument("--runs", type=int, default=1, help="Number of times to run each script.")
    parser.add_argument("--records", type=int, default=10, help="Maximum number of records to create.")
    parser.add_argument("--random", action="store_true", help="Use random number of records between 1 and --max if true, else use --max.")    
    args = parser.parse_args()

    # Get all .py files in the current directory
    py_files = [f for f in os.listdir('.') if f.endswith('.py') and f != os.path.basename(__file__)]

    # Run each file X times with the arguments
    for py_file in py_files:
        run_file(py_file, args.locale, args.runs, args.records, args.random)

if __name__ == "__main__":
    main()
