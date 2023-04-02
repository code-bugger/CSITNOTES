from django.db import models

# Create your models here.
class Semester(models.Model):
    Sem_Choices = [
        ('First','First'),
        ('Second','Second'),
        ('Third','Third'),
        ('Fourth','Fourth'),
        ('Fifth','Fifth'),
        ('Sixth','Sixth'),
        ('Seventh','Seventh'),
        ('Eighth','Eighth')
    ]
    semester = models.CharField(choices=Sem_Choices, max_length=15)
    def __str__(self):
        return self.semester


class Subject(models.Model):
    sub_choices = [
        ('1', (
            ('IIT', 'IIT'),
            ('C-Prog.', 'C-Prog.'),
            ('DL', 'DL'),
            ('Math', 'Math'),
            ('Physics', 'Physics')
        )),
        ('2', (
            ('DS', 'DS'),
            ('OOP', 'OOP'),
            ('MP', 'MP'),
            ('MATH-II', 'MATH-II'),
            ('STAT-I', 'STAT-I'),
        )),
        ('3', (
            ('DSA', 'DSA'),
            ('NM', 'NM'),
            ('CA', 'CA'),
            ('CG', 'CG'),
            ('STAT-II', 'STAT-II'),
        )),
        ('4', (
            ('TOC', 'TOC'),
            ('CN', 'CN'),
            ('OS', 'OS'),
            ('DBMS', 'DBMS'),
            ('AI', 'AI'),
        )),
        ('5', (
            ('DAA', 'DAA'),
            ('SAD', 'SAD'),
            ('CRYPTO', 'CRYPTO'),
            ('SAM', 'SAM'),
            ('WT', 'WT'),
            ('SAE', 'SAE')
        )),
        ('6', (
            ('SE', 'SE'),
            ('CDC', 'CDC'),
            ('E-GOV', 'E-GOV'),
            ('NCC', 'NCC'),
            ('TW', 'TW'),
            ('E-COM', 'E-COM'),
        )),
        ('7', (
            ('AJP', 'AJP'),
            ('DW & DM', 'DW & DM'),
            ('POM', 'POM'),
            ('P-WORK', 'P-WORK'),
            ('IR', 'IR'),
            ('DA', 'DA'),
            ('SPM', 'SPM'),
            ('NS', 'NS'),
            ('DSD', 'DSD')
        )),
        ('8', (
            ('AD', 'AD'),
            ('CC', 'CC'),
            ('AN-IPV6', 'AN-IPV6'),
            ('DSS & ES', 'DSS & ES'),
            ('DN', 'DN'),
            ('ESP', 'ESP'),
            ('GT', 'GT'),
            ('GS', 'GS'),
            ('IM', 'IM'),
            ('MAD', 'MAD'),
            ('NSA', 'NSA'),
            ('RTS', 'RTS'),
        )),
    ]
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    Subject_Name = models.CharField(choices=sub_choices, max_length=15)
    MicroSyllabus_file=models.FileField(default='NULL',blank=True,null=True)
    Book_file=models.FileField(default='NULL',blank=True,null=True)
    Sub_discription=models.CharField(max_length=100,blank=True)
    Sub_image=models.ImageField(upload_to="subject_img",blank=True,null=True)
    def __str__(self):
        return self.Subject_Name

class Note(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    Subject_Name=models.ForeignKey(Subject, on_delete=models.CASCADE)
    Chapter=models.CharField(max_length=30)
    Note_file=models.FileField(default='NULL',blank=True,null=True)
    def __str__(self):
        return self.Chapter

class Question(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    Subject_Name=models.ForeignKey(Subject, on_delete=models.CASCADE)
    year=models.CharField(max_length=4)
    Question_file=models.FileField(default='NULL',blank=True,)
    def __str__(self):
        return self.year