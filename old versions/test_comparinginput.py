# import pytest
from loadmatlab_workspace import load_mat
before=load_mat("before-updateseries-nopinone-unsure")
s=before['s']
def comparinginput(python_in):
    return python_in

def test_answer():
    assert comparinginput(s) == s