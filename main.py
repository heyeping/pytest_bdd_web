import pytest,os

if __name__ == "__main__":
    base_url = os.getcwd()
    print(base_url)
    runTestFile = os.path.join(base_url, 'testSteps/baiduSteps.py')
    print(runTestFile)
    pytest.main(["-vs", runTestFile])