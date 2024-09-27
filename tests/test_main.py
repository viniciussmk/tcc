import os
import sys

from src.main import somar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_somar():
    assert somar(2, 3) == 5
