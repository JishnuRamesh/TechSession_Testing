
import unittest, os
loader = unittest.TestLoader()
start_dir = os.getcwd()
suite = loader.discover(start_dir)
runner = unittest.TextTestRunner()
runner.run(suite)