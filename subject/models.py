from django.db import models

# Create your models here.
class item(models.Model):
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
    Semester = models.CharField(choices=Sem_Choices, max_length=15)
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
    Sem_Subject = models.CharField(choices=sub_choices, max_length=15)
    MicroSyllabus_file=models.FileField(default='NULL',blank=True,null=True)
    Book_file=models.FileField(default='NULL',blank=True,null=True)
    Question_file=models.FileField(default='NULL',blank=True,)
    Sub_discription=models.CharField(max_length=100)
    Sub_image=models.ImageField(upload_to="subject_img")

    def __str__(self):
        return self.Sem_Subject