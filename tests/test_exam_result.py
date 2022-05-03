from main import Student, ExamPoints
from classes.institute import Institute
from classes.examResult import getExamResult
import unittest

class TestAddExamResult(unittest.TestCase):
    # def test_one(self): #correct
    #     stud = Student(777777, 'Егоров Айтал Никитич')
    #     result = ExamPoints(stud, 59.9, 25.4)
    #     inst = Institute()
    #     inst.add_exam_marks(result)
    #     self.assertEqual(len(inst.exam_results), 1)
    #
    # def test_two(self): #correct
    #     stud = Student(777777, 'Егоров Айтал Никитич')
    #     result = ExamPoints(stud, 59.9, 25.4)
    #     result1 = ExamPoints(stud, 55.5, 30.0)
    #     inst = Institute()
    #     inst.add_exam_marks(result)
    #     inst.add_exam_marks(result1)
    #     self.assertEqual(len(inst.exam_results), 1)

    def test_three(self):
        stud = Student(777777, 'Егоров Айтал Никитич')
        result = ExamPoints(stud, 80.0, 10)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_four(self):
        stud = Student(777777, 'Егоров Айтал Никитич')
        result = ExamPoints(stud, 60.0, 40)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_five(self):
        stud = Student(777777, 'Егоров Айтал Никитич')
        result = ExamPoints(stud, -60.0, 40)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_six(self):
        result = ExamPoints(12, 60.0, 25)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_seven(self):
        stud = Student('', '777777')
        result = ExamPoints(stud, 60.0, 24)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_eight(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(123)
        self.assertEqual(len(inst.exam_results), 0)

    def test_nine(self):
        stud = Student(777777, 'Егоров Айтал Никитич')
        result = ExamPoints(stud, 60.0, -25)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

    def test_ten(self):
        stud = Student(777777, 'Егоров Айтал Никитич')
        result = ExamPoints(stud, 60, 25)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_marks(result)
        self.assertEqual(len(inst.exam_results), 0)

class TestGetExamMarks(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.institute = Institute()

        student1 = Student(777777, 'Егоров Айтал Никитич')
        student2 = Student(888888, 'Иванов Иван Иванович')

        self.institute.exam_results = [
            ExamPoints(student1, 54.1, 15),
            ExamPoints(student2, 60, 28.1),
        ]
        super(TestGetExamMarks, self).__init__(*args, **kwargs)

    def test_2(self):
        with self.assertRaises(Exception):
            self.institute.get_exam_marks("")

    def test_3(self):
        with self.assertRaises(Exception):
            self.institute.get_exam_marks(None)

if __name__ == "__main__":
    unittest.main()