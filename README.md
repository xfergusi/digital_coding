# Welcome

Thank you for taking the time to review my coding challenge submission. I appreciate your feedback and look forward to any suggestions you may have for improving my code. Please find the instructions and details about the project below.

## Simplest Way to Review the Code

Start at `src/main.py` and start at the `main()` function. I added a few comments, for readability, in the main fuction to give an idea of how my program was designed. 

## Assumptions
- Python 3.8 or higher is installed.
- The log file format is consistent and correctly formatted.
- In the event there are ties in the "Top 3", we only show 3 stats, some may be trucated. 
- I only ran this on my macbook, the commands below should work on mac, but has not been tested on Windows or Linux.

## Improvements
- Optimize file reading to handle large files efficiently.
- Refactor the code to improve the performance of extracting the top three entries from the hashmap.
- Add error handling and logging for better debugging and maintenance.
- Write additional unit tests to cover edge cases and improve code coverage.
- Set up instruction to venv

## How to Run
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/DigitalTask.git
    cd DigitalTask
    ```
2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

#### Your Environment is now set up, I would reccomend running the end to end test to showcase a working project.

- Run the end to end test
    ```sh
    chmod 755 end_to_end_test/E2E_test.sh
    end_to_end_test/E2E_test.sh
    ```

- Run the main script (manually):
    ```sh
    python src/main.py --log_file logs/small.log
    ```
- Run the unit tests:
    ```sh
    pytest src/Tests
    ```

