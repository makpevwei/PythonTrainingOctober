def get_grade(exam_score):
    if exam_score >= 0 and exam_score < 40:
        return "F"
    elif exam_score >= 40 and exam_score < 45:
        return "E"
    elif exam_score >= 45 and exam_score < 50:
        return "D"
    elif exam_score >= 50 and exam_score < 60:
        return "C"
    elif exam_score >= 60 and exam_score < 70:
        return "B"
    elif exam_score >= 70 and exam_score <= 100:
        return "A"
    else:
        return "Invalid Score"
    
    
def show_student_info(sid, ln, fn, gender, mobile, email, score):
    print()
    print("Student Grade App")
    print("-" * 16)
    print("Student ID:",sid)
    print("First Name:",fn)
    print("Last Name:",ln)
    print("Gender:",gender)
    print("Mobile Number:",mobile)
    print("Email:",email)
    print("Exam Score:",score)
    

def get_student_info():
    try:
        student_id = input("Enter your student id: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        gender = input("Enter your gender: ")
        mobile = input("Enter your mobile number: ")
        email = input("Enter your email address: ")
        exam_score = float(input("Enter your exam score: "))
        
        show_student_info(student_id, first_name, last_name, gender, mobile, email, exam_score)
        
    except ValueError as error:
        print("Error:",error)
        print("Invalid input. Please enter a numeric value.")
        
student = get_student_info()
student