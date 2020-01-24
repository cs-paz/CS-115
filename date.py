'''
Created on _______________________
@author:   _______________________
Pledge:    _______________________

CS115 - Hw 10 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
  
    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day

    def tomorrow(self):
        if self.day < DAYS_IN_MONTH[self.month]:
            #first check to see if it isn't the last day of the month
            self.day += 1
        else:
            #all of the following code is only for the last day of the month
            if self.month == 2 and self.isLeapYear() and self.day != 29:
                #leap year checker
                self.day += 1
                return
            self.day = 1 #set day to first of the next month
            if self.month < 12:
                #checks to see if it isn't december
                self.month += 1
            else:
                #december to january
                self.month = 1
                self.year += 1

    def yesterday(self):
        if self.day - 1 != 0:
            #first check to see if it isn't the first day of the month
            self.day -= 1
        else:
            #all of the following code is only for the first day of the month
            if self.month == 3 and self.isLeapYear():
                #checks if it is leap year and it is 3/1
                self.day = 29
                self.month = 2
                return
            if self.month == 1:
                #checks to see if it is january 1st
                self.month = 12
                self.day = 31
                self.year -= 1
            else:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month]

    def addNDays(self, N):
        for i in range(N):
            print(self)
            self.tomorrow()
        print(self)

    def subNDays(self, N):
        for i in range(N):
            print(self)
            self.yesterday()
        print(self)
        
    def isBefore(self, d2):
        if self.year == d2.year:
            if self.month == d2.month:
                return self.day < d2.day
            else:
                return self.month < d2.month
        else:
            return self.year < d2.year

    def isAfter(self, d2):
        #isBefore already checks if each item is equal
        return (not self.equals(d2) and not self.isBefore(d2))

    def diff(self, d2):
        if self.equals(d2):
            return 0
        
        temp = Date(self.month, self.day, self.year)
        #mutable copy of self object

        num = 1
        if self.isBefore(d2):
            num = -1

        difference = 0 #num is incremented to difference every time loop runs
        while True:
            difference += num
            if num == 1:
                temp.yesterday()
            else:
                temp.tomorrow()
            if temp.equals(d2):
                return difference

    def dow(self):
        #test fails when days aren't in this order for some reason
        daysOfWeek =  ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        return daysOfWeek[self.diff(Date(11, 9, 2011)) % 7]
    
        
        
        
        
        
