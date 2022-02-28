#!/usr/bin/env python3
from __future__ import print_function
import os, sys
import pytest
import archive_test_reports

path = os.getcwd()
if len(sys.argv) == 2:
	path = sys.argv[1]

files = os.listdir(path)
#pytest.main(['-v', '-s', '-m', 'not slow', '--junitxml=test_reports/test_results.xml'] + files)

for name in files:
	full_path = os.path.join(path, name)
	if os.path.isfile(full_path):
		if len(name.split('.')) == 2 and name.split('.')[1] == 'py' and name != "tests.py":
			print("Unittest commences for {}".format(full_path))
   			# Create result files which can be read by Jenkins or other Continuous integration server
			pytest.main(['-v', '-s', '-m', 'not slow', '--junitxml=test_reports/test_results.xml', full_path])

# zip the test_reports folder
archive_test_reports.main()