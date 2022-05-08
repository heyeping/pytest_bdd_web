import pytest,os
from public.public import get_pathfile

if __name__ == "__main__":
    base_url = os.getcwd()
    #print(base_url)
    runTestFile = os.path.join(base_url, 'testSteps/baiduSteps.py')
    #print(runTestFile)
    results_path = os.path.join(get_pathfile(), "report/allure-results")
    report_path = os.path.join(get_pathfile(), "report/allure-report")
    #pytest.main(["-vs", runTestFile])
    pytest.main(["-sq", runTestFile, "--alluredir", results_path])
    os.system("allure generate {} -o {} --clean".format(results_path, report_path))