import os.path

ProjectRoot = os.path.dirname(os.path.dirname(__file__))
AbsoluteProjectRoot = os.path.abspath(ProjectRoot)

if __name__ == "__main__":
    print(AbsoluteProjectRoot)
