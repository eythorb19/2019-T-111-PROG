# The foot (pl. feet; abbreviation: ft; symbol: ′, the prime symbol) is a unit of length in the imperial and US customary systems of measurement.
# Since the International Yard and Pound Agreement of 1959, one foot is defined as 0.3048 meter exactly.
# In customary and imperial units, the foot comprises 12 inches and three feet compose a yard.

class Height():
    CENTIMETERS_IN_FOOT = 30.48
    CENTIMETERS_IN_INCH = 2.54
    INCHES_IN_FEET = 12

    def __init__(self, feet, inches):
        self.__feet = feet
        self.__inches = inches

        self.fix()

    def __str__(self):
        return '{} ft, {} in'.format(self.__feet, self.__inches)
    
    def __add__(self, other):
        feet = self.__feet + other.__feet
        inches = self.__inches + other.__inches
        return Height(feet, inches)

    def __gt__(self, other):
        if self.__feet > other.__feet:
            return True
        elif self.__feet < other.__feet:
            return False
        else:
            return self.__inches > other.__inches
            
    def fix(self):
        if self.__inches >= self.INCHES_IN_FEET:
            self.__inches = self.__inches % self.INCHES_IN_FEET
            self.__feet += 1
    
    def cm(self):
        return self.__feet * self.CENTIMETERS_IN_FOOT + self.__inches * self.CENTIMETERS_IN_INCH
