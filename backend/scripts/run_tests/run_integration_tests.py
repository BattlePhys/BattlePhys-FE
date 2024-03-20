import pytest
import os

def run_integration_tests():
    os.environ['ENV'] = 'test'
    os.chdir('tests/integration')
    pytest.main(['-v', '-s'])  


if __name__ == "__main__":
    run_integration_tests()

