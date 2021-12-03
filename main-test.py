from main import add

def testAdd():
    assert add(5,5) == 11
    print("Add function successfully executed!")

if __name__ == "__main__":
    testAdd()