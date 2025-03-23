#!/bin/bash

echo "Running End to End Test"

echo "Running Unit Tests"
pytest src/Tests

echo
echo "Running Main Program"

echo
python src/main.py --log_file end_to_end_test/programming-task-example-data.log

