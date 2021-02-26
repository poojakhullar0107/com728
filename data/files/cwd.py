
def cwd():
    import os
    path = os.getcwd()
    print(f"The current working directory is  {path}")
    for file in os.listdir(path):
        print("The directory contains the following files:")
        print(file)
def run():
    print("Processing....")
    cwd()

if __name__ ==  "__main__":
    run()