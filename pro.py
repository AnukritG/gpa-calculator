import streamlit as st

st.set_page_config(page_title="GPA CALCULATOR", page_icon="None")

def grades(marks):
    if marks >= 90:
        grade = 10
    elif marks >= 75:
        grade = 9
    elif marks >= 65:
        grade = 8
    elif marks >= 55:
        grade = 7
    elif marks >= 50:
        grade = 6
    elif marks >= 45:
        grade = 5
    elif marks >= 40:
        grade = 4
    else:
        grade = 0

    return grade


def cal(sem):
    theo = {}
    prac = {}
    GPA = 0
    flag = 0  # warning message when marks haven't been entered
    cred = 0

    if sem == 1:
        theo = {'App. Maths-I': 4, 'App. Physics-I': 3, 'Manufacturing Processes': 4, 'Electrical Science': 3,
                'Communication Skills': 3, 'App. Chemistry': 3}
        prac = {'App. Physics Lab-I': 1, 'Electrical Science Lab': 1, 'Egg. Graphics Lab': 2, 'App. Chemistry Lab': 1}
        cred = 25

    elif sem == 2:
        theo = {'App. Maths-II': 4, 'App. Physics-II': 3, 'Indian Constitution': 2, 'Intro To Programming': 3,
                'Engineering Mechanics': 3, 'Environmental Studies': 3, 'Human Values and Ethics': 1}
        prac = {'App. Physics Lab-II': 1, 'Programming Lab': 1, 'Workshop': 2, 'Engineering Mechanics Lab': 1,
                'EVS Lab': 1}
        cred = 25

    elif sem == 3:
        theo = {'App. Maths-III': 4, 'Foundation of CS': 4, 'Switching Theory & Logic Design': 4,
                'Circuits & Systems': 4, 'Data Structures': 4, 'Computer Graphics & Multimedia': 4, }
        prac = {'Switching Theory and Logic Design Lab': 1, 'Data Structure Lab': 1, 'Circuits & Systems Lab': 1,
                'Computer Graphics and Multimedia Lab': 1}
        cred = 28

    elif sem == 4:
        theo = {'App. Maths-IV': 4, 'Computer Organisation & Architecture': 4, 'Theory of Computation': 4,
                'Database Management': 4, 'Object Oriented Programming': 3, 'Communication Systems': 4}
        prac = {'App. Maths Lab': 1, 'COA Lab': 1, 'DBMS Lab': 1, 'OOPS Lab': 1, 'Communication Systems Lab': 1}
        cred = 28

    elif sem == 5:
        theo = {'Algo. Design & Analysis': 4, 'Software Engineering': 4, 'Java Programming': 4,
                'Industrial Management': 3, 'Digital Communication': 4, 'Communication Skills for Prof.': 1}
        prac = {'Algo. Design Lab': 1, 'Software Engineering Lab': 1, 'Java Programming Lab': 1, 'In-house Workshop': 1,
                'Digital Communication Lab': 1, 'Communication Skills Lab': 1}
        cred = 26

    elif sem == 6:
        theo = {'Compiler Design': 4, 'Operating Systems': 4, 'Computer Networks': 4,
                'Web Technology': 3, 'Artificial Intelligence': 4, 'Microprocessors & Microcontrollers': 4, }
        prac = {'Operating Systems Lab': 1, 'Computer Networks Lab': 1, 'Web Technology Lab': 1,
                'Microprocessor & Microcontroller Lab': 1}
        cred = 27

    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Theory Subjects"):
            for i in theo:
                marks = st.number_input("{}:".format(i), 0, 100)
                if marks == 0:
                    flag = 1
                num = grades(marks)
                GPA += num * theo[i]

    with col2:
        with st.expander("Practical Subjects"):
            for j in prac:
                marks = st.number_input("{}:".format(j), 0, 100)
                if marks == 0:
                    flag = 1
                num = grades(marks)
                GPA += num * prac[j]

    if flag:
        st.warning("Please enter the marks for all subjects")

    GPA = GPA / cred
    return GPA


def cal78(sems):
    theory={}
    practical={}
    GPA1=0
    creds=0
    flag=0

    if sems == 7:
        theory = {'Info. Security': 4, 'Software Testing': 3, 'Wireless Comm.': 3}
        practical = {'Info. Security Lab': 1, 'Software Testing Lab': 1, 'Wireless Comm. Lab': 1,'Certification': 1,
                     'Minor Project': 3}
        creds=24

        colu1, colu2, colu3 = st.columns(3)
        with colu1:
            with st.expander("Extra Subjects"):
                option = st.selectbox(
                    'Please choose one of the following subjects',
                    ('Complexity Theory','Intellectual Property Rights' 'Embedded Systems', 'Data Mining',
                   'Advanced Computer Architecture', 'Natural Language Processing'))
                st.write("")
                option2 = st.selectbox(
                    'Please choose one of the following subjects',
                    ('Digital Signal Processing', 'Simulation and Modelling', 'Advanced DBMS', 'Parallel Computing',
                 'Advanced Computer Networks', 'Sociology and Elements of Indian History', 'Control System'))
                option3 = str(option2)

        with colu2:
            with st.expander("Theory Subjects"):
                theory['{}'.format(option)] = 3
                theory['{}'.format(option2)] = 3
                for i in theory:
                    marks = st.number_input("{}:".format(i), 0, 100,value=0, step=None, format=None, key='mark')
                    if marks == 0:
                        flag = 1
                    num = grades(marks)
                    GPA1 += num * theory[i]

        with colu3:
            with st.expander("Practical Subjects"):
                practical['{}'.format(option3)] = 1
                for j in practical:
                    marks = st.number_input("{}:".format(j), 0, 100,value=0, step=None, format=None, key='mark1')
                    if marks == 0:
                        flag = 1
                    num = grades(marks)
                    GPA1 += num * practical[j]

    else:
        theory = {'Mobile Computing': 4, 'Machine Learning': 3, 'Human Values-II': 1}
        practical = {'Mobile Computing Lab': 1, 'Machine Learning Lab': 1, 'Major Project': 8}
        creds=26

        coll1, coll2, coll3 = st.columns(3)
        with coll1:
            with st.expander("Electives"):
                st.write("Group A")
                option = st.selectbox(
                    'Please choose one of the following subjects',
                    ('Digital Image Processing', 'MicroelectronicsAd Hoc and Sensor Networks', 'Soft Computing', 'VLSI Design',
                     'Distributed Systems', 'Object Oriented Software Engineering', 'Computer Vision',
                     'Software Project Management'))

                st.write("Group B")
                option2 = st.selectbox(
                    'Please choose one of the following subjects',
                    ('Human Computer Interaction', 'Information Theory and Coding','Web Intelligence and Big Data',
                     'Service Oriented Architecture','Multiagent Systems', 'Principles of Programming Languages',
                     'Telecommunication Networks','Selected Topics of Recent Trends in Computer Science and Engineering'))
                option3 = str(option)
                option4 = str(option2)
        with coll2:
            with st.expander("Theory Subjects"):
                theory['{}'.format(option)] = 3
                theory['{}'.format(option2)] = 3
                for i in theory:
                    marks = st.number_input("{}:".format(i), 0, 100,value=0, step=None, format=None, key='marks1')
                    if marks == 0:
                        flag = 1
                    num = grades(marks)
                    GPA1 += num * theory[i]

        with coll3:
            with st.expander("Practical Subjects"):
                practical['{}'.format(option3)] = 1
                practical['{}'.format(option4)] = 1
                for j in practical:
                    marks = st.number_input("{}:".format(j), 0, 100,value=0, step=None, format=None, key='marks2')
                    if marks == 0:
                        flag = 1
                    num = grades(marks)
                    GPA1 += num * practical[j]

    if flag:
        st.warning("Please enter the marks for all subjects")

    GPA1 = GPA1 / creds
    return GPA1


cl1, cl2, cl3 = st.columns(3)
with cl2:
    st.image("https://bharatividyapeeth.edu/img/bvpnew.png")

st.markdown("<style>.head {font-size: 48px;font-family: algerian; text-align: center; color:green;}</style>", unsafe_allow_html=True)
st.markdown('<p class="head">CALCULATOR</p>', unsafe_allow_html=True)
st.markdown("<style>.Shead {font-size: 32px;font-family: algerian; text-align: center; color:orange;}</style>", unsafe_allow_html=True)
st.markdown('<p class="Shead">GPA Calculator of a semester for B.Tech(CSE)</p>', unsafe_allow_html=True)

with st.container():
    name = st.text_input("ENTER YOUR NAME")

    if name:
        st.write("Hello", name, '!!')
        sem1 = st.number_input("ENTER YOUR SEMESTER", 0, 8)

        if sem1<7:
            st.write("")
            st.markdown("<h4 style='text-align: center; '>Enter Marks</h4>", unsafe_allow_html=True)

            gpa = cal(sem1)

            st.write("")

            fin1 = st.button("Calculate")

            if fin1:
                msg = "Your GPA is {}".format(str(round(gpa, 2)))
                st.markdown(f"<h3 style='text-align: center; color: blue '>{msg}</h3>", unsafe_allow_html=True)
                if gpa >= 7.5:
                    st.balloons()
                    st.snow()

        elif sem1<9:

            st.write("")
            st.markdown("<h4 style='text-align: center; '>Enter Marks</h4>", unsafe_allow_html=True)

            GPA = cal78(sem1)
            st.write("")

            fin1 = st.button("Calculate")

            if fin1:
                msg = "Your GPA is {}".format(str(round(GPA, 2)))
                st.markdown(f"<h3 style='text-align: center; color: blue '>{msg}</h3>", unsafe_allow_html=True)
                if GPA >= 7.5:
                    st.balloons()
                    st.snow()


