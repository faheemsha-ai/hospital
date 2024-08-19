from django.db import models

class Department(models.Model):
    # Item = Department.objects.all()
    department_name = models.CharField(max_length=50,blank=False)
    department_description = models.TextField(max_length=500,blank=False)

    def __str__(self):
        return self.department_name
    

class Doctor(models.Model):
    doc_name = models.CharField(max_length=50,blank=False)
    doc_image = models.TextField(max_length=500,blank=False)
    doc_dep = models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_sep = models.TextField(max_length=500,blank=False)
    def __str__(self):
        return self.doc_name
    
class Booking(models.Model):
    name = models.CharField(max_length=12,blank=False)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15,blank=False)
    doc_name = models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=False)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    booked_on = models.DateField(auto_now_add=True)
    message = models.TextField(max_length=200,blank=False)
    def __str__(self):
        return self.name