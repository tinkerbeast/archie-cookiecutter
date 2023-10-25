import os
import shutil
import subprocess
import tempfile
import unittest

from cookiecutter.main import cookiecutter


#TODO: parameterized test https://stackoverflow.com/questions/32899/how-do-you-generate-dynamic-parameterized-unit-tests-in-python


def bake_and_make(archetype: str, target, cmake_flags=[]):
  dirpath = tempfile.mkdtemp()
  cookiecutter(f'../{archetype}', no_input=True, output_dir=dirpath)
  output = subprocess.run(['ls', dirpath], capture_output=True, text=True).stdout.rstrip()
  builddir = f'{dirpath}/build'
  os.makedirs(builddir)
  #
  cmake_cmd = ['cmake', '-S', f'{dirpath}/{output}', '-B', builddir]
  cmake_cmd.extend(cmake_flags)
  subprocess.run(cmake_cmd, check=True)
  subprocess.run(['make', '-C', builddir, target], check=True)
  shutil.rmtree(dirpath)


class TestMakeAll(unittest.TestCase):

  def test_all(self):
    bake_and_make('cpp-cmake-simple', 'all')

  def test_check(self):
    bake_and_make('cpp-cmake-simple', 'check', ['-DARCHIE_ENABLE_GTEST=ON'])

  def test_boolean(self):
    a = True
    b = True
    self.assertEqual(a, b)

if __name__ == '__main__':
  unittest.main()
