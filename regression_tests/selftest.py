import matplotlib
matplotlib.use('agg')
import unittest

class TestModuleImports(unittest.TestCase):

     def test_import_sygma(self):
          import SYGMA   
	
     def test_import_omega(self):
          import OMEGA

     def test_import_stellab(self):
          import STELLAB
