# ECOR 1042 Lab 4 - team submission

#import check module here
import check
#import load_data module here
import load_data
# Update "" with your the name of the active members of the team
__author__ = "Jacob Aydin - Spencer Edmonds - Anneli Sheridan - Pagalavan Sivakumar"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-111"

#==========================================#

# Place test_return_list function here


def test_return_list():
    #Complete the function with your test cases

    #test that student_school_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_school_list('student-test.csv', 'GP'), list), True)
    check.equal(isinstance(load_data.student_school_list('student-test.csv', 'CF'), list), True)
    check.equal(isinstance(load_data.student_school_list('student-test.csv', 'MB'), list), True)

    #test that student_age_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_age_list('student-test.csv', 15), list), True)
    check.equal(isinstance(load_data.student_age_list('student-test.csv', 17), list), True)
    check.equal(isinstance(load_data.student_age_list('student-test.csv', 18), list), True)

    #test that student_health_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_health_list('student-test.csv', 4), list), True)
    check.equal(isinstance(load_data.student_health_list('student-test.csv', 3), list), True)
    check.equal(isinstance(load_data.student_health_list('student-test.csv', 5), list), True)

    #test that student_failures_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_failures_list('student-test.csv', 0), list), True)
    check.equal(isinstance(load_data.student_failures_list('student-test.csv', 1), list), True)
    check.equal(isinstance(load_data.student_failures_list('student-test.csv', 2), list), True)

    #test that load_data returns a list (6 different test cases required)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('School', 'GP')), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('School', 'MB')), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Health', 3)), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Age', 16)), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('Failures', 3)), list), True)
    check.equal(isinstance(load_data.load_data('student-test.csv', ('All', -1)), list), True)

    #test that add_average returns a list (3 different test cases required)"""

    check.equal(isinstance(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}]), list), True)
    check.equal(isinstance(load_data.add_average([{'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}]), list), True)
    check.equal(isinstance(load_data.add_average([{'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}]), list), True)

    check.summary()

# Place test_return_list_correct_lenght function here


testfile = "student-test.csv"


def test_return_correct_dict_inside_list():
    #Complete the function with your test cases

    #test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(load_data.student_school_list(testfile, "GP")[0], {'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.student_school_list(testfile, "GP")[-1], {'Age': 15, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    check.equal(load_data.student_school_list(testfile, "GP")[1], {'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})

    #test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)

    check.equal(load_data.student_age_list(testfile, 15)[0], {'School': 'GP', 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    check.equal(load_data.student_age_list(testfile, 15)[-1], {'School': 'CF', 'StudyTime': 5, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7})
    check.equal(load_data.student_age_list(testfile, 15)[1], {'School': 'MB', 'StudyTime': 1, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12})

    #test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(load_data.student_health_list(testfile, 3)[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.student_health_list(testfile, 3)[-1], {'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12})
    check.equal(load_data.student_health_list(testfile, 3)[1], {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})
    #test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(load_data.student_failures_list(testfile, 0)[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.student_failures_list(testfile, 0)[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})
    check.equal(load_data.student_failures_list(testfile, 0)[1], {'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    check.equal(load_data.load_data(testfile, ('Age', 18))[0], {'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.load_data(testfile, ('Age', 18))[-1], {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})
    check.equal(load_data.load_data(testfile, ('Health', 3))[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.load_data(testfile, ('Health', 5))[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})
    check.equal(load_data.load_data(testfile, ('School', 'GP'))[0], {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(load_data.load_data(testfile, ('School', 'MS'))[-1], {'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})

     #test that add_average returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}]), [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}])
    check.equal(load_data.add_average([{'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}]), [{'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8, 'G_Avg': 8.33}])
    check.equal(load_data.add_average([{'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}]), [{'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}])

    check.summary()
#Place test_return_correct_dict_inside_list function here


#Place test_add_average function here


# Do NOT include a main script in your submission
