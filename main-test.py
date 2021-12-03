from main import add

def testAdd():
    assert add(5,5) == 10
    assert add(2,2) == 4
    print("Add function successfully executed!")

if __name__ == "__main__":
    testAdd()