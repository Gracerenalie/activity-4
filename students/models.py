from django.db import models

class Student(models.Model):
    YEAR_LEVEL_CHOICES = [
        ('1st', '1st Year'),
        ('2nd', '2nd Year'),
        ('3rd', '3rd Year'),
        ('4th', '4th Year'),
    ]

    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Others', 'Others'),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, blank=True, null=True)  # optional
    last_name = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    year_level = models.CharField(max_length=4, choices=YEAR_LEVEL_CHOICES)

    @property
    def name(self):
        parts = [self.first_name]
        if self.middle_name:
            parts.append(self.middle_name)
        parts.append(self.last_name)
        return " ".join(parts)

    class Meta:
        db_table = 'student_records'
