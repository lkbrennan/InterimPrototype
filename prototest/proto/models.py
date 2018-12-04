from django.db import models

class Parent(models.Model):
    parent_name = models.CharField(max_length=200)
    parent_email = models.CharField(max_length=200)

    def __str__(self):
        return self.parent_name

class Class(models.Model):
    class_choices = (
        ('first', 'First Class'),
        ('second', 'Second Class'),
        ('third', 'Third Class'),
        ('fourth', 'Fourth Class'),
        ('fifth', 'Fifth Class'),
        ('sixth', 'Sixth Class'),
    )
    class_type = models.CharField(
        max_length=8,
        choices=class_choices,
        default='first',
    )
    class_key = models.CharField(max_length=20)

    def __str__(self):
        return self.class_type


class School(models.Model):
    school_name = models.CharField(max_length=200)
    school_email = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.school_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)
    teacher_email = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.teacher_name

class teachesAt(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class teachesClass(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)


class Student(models.Model):
    student_name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.student_name


class attendsClass(models.Model):
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Quiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Results(models.Model):
    score = models.IntegerField()
    percentage = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correctAnswer = models.IntegerField()
    var1 = models.IntegerField()
    var2 = models.IntegerField()
    operator = models.CharField(max_length=1)


class StudentAnswer(models.Model):
    answerGiven = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class methodology(models.Model):
    answer = models.ForeignKey(StudentAnswer, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500)

