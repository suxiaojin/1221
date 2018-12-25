class Student():
  #  name='qiyue'
   # age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
student1=Student('石敢当',20)
print(student1.__dict__)
student2=Student('喜小乐',30)
print(student1.name)
print(student2.name)
#print(Student.name)