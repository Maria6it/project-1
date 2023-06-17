class student:

    def std_mark(intgral_mark,it_fund,programming):

         marks = []
        # intgral_mark=float(input('enter intgral mark:'))
         marks.append(intgral_mark)
        # it_fund=float(input('enter it fundamentals mark:'))
         marks.append(it_fund)
        # programming=float(input('enter programming mark:'))
         marks.append(programming)
         print('your intgral_mark, it_fund, programming')
         return (intgral_mark,it_fund,programming)
    def std_grade(self):
        if self  <50:
            print('fail')
        else:
            print('pass')
    def file_fun(self):
        if self==1:
            file=open('project file.txt','r')
            r=file.read()
            print(r)
            file.close()
        if self==2:
            file = open('project file.txt', 'w')
            file.write(input('enter what you write:'))
            file.close()
        if self==3:
            file = open('project file.txt', 'a')
            file.write(input('enter what you write to append:'))
            file.close()
student.file_fun(1)
student.std_grade(60)
print(student.std_mark(90,100,110))











