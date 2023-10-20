import os
import shutil
import subprocess
import tempfile
import unittest

from cookiecutter.main import cookiecutter


#TODO: parameterized test https://stackoverflow.com/questions/32899/how-do-you-generate-dynamic-parameterized-unit-tests-in-python


def bake_and_make(archetype: str):
  dirpath = tempfile.mkdtemp()
  cookiecutter(f'../{archetype}', no_input=True, output_dir=dirpath)
  output = subprocess.run(['ls', dirpath], capture_output=True, text=True).stdout.rstrip()
  builddir = f'{dirpath}/build'
  os.makedirs(builddir)
  subprocess.run(['cmake', '-S', f'{dirpath}/{output}', '-B', builddir], check=True)
  subprocess.run(['make', '-C', builddir, 'all'], check=True)
  shutil.rmtree(dirpath)


class TestMakeAll(unittest.TestCase):

  def test_string(self):
    bake_and_make('cpp-cmake-simple')

  def test_boolean(self):
    a = True
    b = True
    self.assertEqual(a, b)

if __name__ == '__main__':
  unittest.main()
