from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return f'{self.pk}번의사 {self.name}'
        
        
class Patient(models.Model):
    name = models.TextField()
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    #Relation 정보만 쓸때는 through='Reservation', 만 써서 사용 가능하지만, 
    # 정보으로 역추적 하기 위해서는
    # retated_name 을 부여해 들어갈 수 있다
    # In [2]: doctor1.patients.all()
    # Out[2]: <QuerySet [<Patient: 2번 환자 세환>, <Patient: 2번 환자 세환>]>

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, 
#     on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, 
#     on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id} 번 의사의 {self.patient_id}번 환자'