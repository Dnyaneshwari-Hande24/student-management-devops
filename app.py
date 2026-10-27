def greet_student(name):
    return f"Welcome, {name}!"

def test_greet_student():
    assert greet_student("Student") == "Welcome, Student!"

if __name__ == "__main__":
    print(greet_student("Student"))
