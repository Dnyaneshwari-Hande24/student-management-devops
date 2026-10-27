from app import greet_student, validate_student


def test_greet_student():
    assert greet_student("Student") == "Welcome, Student!"


def test_valid_student_name():
    assert validate_student("Rahul") is True


def test_empty_student_name():
    assert validate_student("") is False


from app import validate_student_email

def test_valid_email():
    assert validate_student_email("student@gmail.com") == True

def test_invalid_email():
    assert validate_student_email("studentgmail.com") == False

def test_empty_email():
    assert validate_student_email("") == False

