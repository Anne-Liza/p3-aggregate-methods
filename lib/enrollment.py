from datetime import datetime
class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()
    
    def total_enrollments(self):
        return len(self._enrollments)
    
    def all_enrolled_courses(self):
        return {enrollment.course for enrollment in self._enrollments}

class Course:
    def __init__(self, title):

        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

    def total_enrollments(self):
        return len(self._enrollments)

    def all_enrolled_students(self):
        return {enrollment.student for enrollment in self._enrollments}

class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date
    
    @classmethod
    def total_enrollments(cls):
        return len(cls.all)

    @classmethod
    def enrollments_by_student(cls, student):
        if isinstance(student, Student):
            return [enrollment for enrollment in cls.all if enrollment.student == student]
        else:
            raise TypeError("student must be an instance of Student")

    @classmethod
    def enrollments_by_course(cls, course):
        if isinstance(course, Course):
            return [enrollment for enrollment in cls.all if enrollment.course == course]
        else:
            raise TypeError("course must be an instance of Course")