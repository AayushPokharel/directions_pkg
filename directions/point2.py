##!/usr/bin/python3

import os.path

ProjectRoot = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
AbsoluteProjectRoot = os.path.abspath(ProjectRoot)
ChromeDriverLocation = os.path.join(ProjectRoot,"WebDriver","chromedriver.exe")

if __name__ == "__main__":
    print(AbsoluteProjectRoot)
