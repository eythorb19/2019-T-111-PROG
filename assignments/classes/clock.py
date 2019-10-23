class Clock(object):
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds        
        
    def __str__(self):
        return '{} hours, {} minutes and {} seconds'.format(self.hours,self.minutes,self.seconds)
        
    def str_update(self,str):
        hours,minutes,seconds=[int(n) for n in str.split(':')]
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def add_clocks(self,clk):
        carry_minutes,seconds= divmod((self.seconds + clk.seconds),60)
        carry_hours,minutes= divmod((self.minutes + clk.minutes),60)
        carry_days,hours = divmod((self.hours + clk.hours),24)

        total_hours = hours + carry_hours
        total_minutes = minutes + carry_minutes
        if total_minutes == 60:
            total_hours += 1
            total_minutes = 0
        return Clock(total_hours,total_minutes,seconds)

clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
print(clock2)
clock3 = clock1.add_clocks(clock2)
print(clock3)

clock1 = Clock()
clock2 = Clock()
clock1.str_update("20:10:52")
clock2.str_update("08:49:24")
print(clock1)
print(clock2)
clock3 = clock1.add_clocks(clock2)
print(clock3)



