class student:
    count = 0
    def students(self):
        self.roll=int(input('Enter roll number:- '))
        self.name=input('Enter name:- ')
        self.course=input('Enter course:- ')
        self.branch=input('Enter branch:- ')
        self.math=float(input('Enter marks of maths:- '))
        self.discrete=float(input('Enter marks of Discrete:- '))
        self.python=float(input('Enter marks of Python:- '))
        self.coa=float(input('Enter marks of Computer organisation- '))
        self.ds=float(input('Enter marks of data structure:- '))
        self.fav=input('Enter favorite subject:- ')

    def result(self):
        self.percentage=(float)((self.math+self.discrete+self.python+self.coa+self.ds)/500*100);
        print('Roll number is:-',self.roll)
        print('Name is:-',self.name)
        print('Course is:-',self.course)
        print('Branch is:-',self.branch)
        print('Percentage is:-',self.percentage,'%')
        print('Favorite subject is:-',self.fav)

s1=student()
s1.students()
s1.result()