import streamlit as st 

def get_avg(score_dict):
    avg_score = sum(score_dict.values())/len(score_dict.values())
    return avg_score

def get_grade(avg_score):
    if avg_score >= 0 and avg_score < 40:
        return "F"
    elif avg_score >= 40 and avg_score < 45:
        return "E"
    elif avg_score >= 45 and avg_score < 50:
        return "D"
    elif avg_score >= 50 and avg_score < 60:
        return "C"
    elif avg_score >= 60 and avg_score < 70:
        return "B"
    elif avg_score >= 70 and avg_score <= 100:
        return "A"
    else:
        return "Invalid Score"
    
# Main Streamlit App
st.title("Student Information App")

# Initialize session state for dynamic subjects
if "subjects" not in st.session_state:
    st.session_state.subjects = ["Math", "English", "Chemistry", "Physics"]
    
with st.form("Student form"):
    st.subheader("Enter your details")
    
    sid = st.text_input("Student ID: ")
    fn = st.text_input("First Name: ")
    ln = st.text_input("Last Name: ")
    gender = st.radio("Gender: ", options=["Male", "Female"])
    mobile = st.text_input("Mobile Number: ")
    email = st.text_input("Email Address: ")
    
    st.subheader("Enter your scores")
    
    subject_scores = {}
    for subject in st.session_state.subjects:
        score = st.text_input(f"Enter your {subject} score: ")
        subject_scores[subject] = score
        
    new_subject = st.text_input("Add a new subject (optional): ")
    if new_subject:
        if new_subject not in st.session_state.subjects:
            st.session_state.subjects.append(new_subject)
            
    btn_submit = st.form_submit_button("Submit")
    
    
    if btn_submit:
        if not all([sid, fn, ln, gender, mobile, email]) or any(value.strip() == "" for value in subject_scores.values()):
                st.warning("All fields must be filled out and scores must be \
                           provided for all subjects")
                
        else:
            try:
                valid_scores = {subject: float(score) for subject, score in subject_scores
                                .items()}
                
                if any(score < 0 or score > 100 for score in valid_scores.values()):
                    st.warning("Scores must be between 0 and 100")
                else:
                    avg_score = get_avg(valid_scores)
                    grade = get_grade(avg_score)
                    
                    # Display student information and score
                    st.info("Student Details:")
                    st.write("Student ID:",sid)
                    st.write("First Name:",fn)
                    st.write("Last Name:",ln)
                    st.write("Gender:",gender)
                    st.write("Mobile:",mobile)
                    st.write("Emial:",email)
                    
                    st.subheader("Scores:")
                    st.write(valid_scores)
                    st.write("Average Score:",avg_score)
                    st.write("Grade:",grade)
                    
            except ValueError:
                st.warning("Please, enter valid numeric scores for all subjects")
                    
                    
    
    