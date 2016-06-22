#ProjectEuler problem 19
#Solved: 14 Jun 2016
#NOTE: I wanted to solve this problem by introducing the notion of time to the
#computer by building a class, there are much shorter approaches to this problem

class time(object):
    
    def __init__(self,d,m,y,dayCount):
        self.d = d
        self.m = m
        self.y = y
        self.dayCount = dayCount
        self.leap = False
        self.lim = 31
        self.day = 'm'
        
    def leapYear(self):
        if self.y % 100 == 0:
            if self.y % 400 == 0:
                self.leap =  True
            else:
                self.leap = False
        else:
            if self.y % 4 == 0:
                self.leap = True
            else:
                self.leap = False
            
    def limit(self):
        self.leapYear()
        thrity = [4,6,9,11]
        thrity_one = [1,3,5,7,8,10,12]
        if self.m in thrity:
            self.lim = 30
        elif self.m in thrity_one:
            self.lim = 31
        elif self.m == 2:
            if self.leap:
                self.lim = 29
            else:
                self.lim = 28
        else:
            raise 'Error during month decleration!'
                
    def increaseDay(self):
        self.determineDay()
        self.limit()
        day_limit = self.lim
        if self.d < day_limit:
            self.d += 1
        else:
            self.increaseMonth()
        self.dayCount += 1
        
    def increaseMonth(self):
        if self.m < 12:
            self.m += 1
            self.d = 1
        else:
            self.increaseYear()

    def increaseYear(self):
        self.y += 1
        self.m = 1
        self.d = 1

    def determineDay(self):
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.day = days[self.dayCount % 7]

    def displayInfo(self):
        self.determineDay()
        print '''
Date: %d/%d/%d
It is a %s
''' % (self.d,self.m,self.y,self.day)
                
d = input('Enter the day: ')
m = input('Enter month: ')
y = input('Enter year: ')
day = input('Enter the name of the day in number (1:mon 7:sun): ') - 1
date = time(d,m,y,day) #1/1/1901 is a Tuesday if 1/1/1900 is a Monday
date.displayInfo()
print '_ _ _ _ _ _'

counter = 0
final = input('Enter the final year: ')
while date.y < final:
    date.increaseDay()
    if date.d == 1 and date.day == 'Sunday':
        counter += 1

print '%d Sundays fell to the first day of the month until date %d/%d/%d' %(counter,date.d,date.m,date.y)
