import unittest
from unittests import UnitTests
import sys
import csv

def createSuite():
  return unittest.TestLoader().loadTestsFromTestCase(UnitTests)

if __name__ == '__main__':
  suite = createSuite()
  runner = unittest.TextTestRunner(verbosity=2)
  results = runner.run(suite)