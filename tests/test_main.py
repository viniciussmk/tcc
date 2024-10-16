import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import somar

def test_somar():
    assert somar(2, 3) = 5
