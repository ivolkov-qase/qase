import pytest
from qaseio.pytest import qase

@qase.id(5)
@qase.title("H2O supply systems < 1")
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	assert x == y,"test failed"

@qase.id(319)
@qase.title("Launchpad")
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed" 
