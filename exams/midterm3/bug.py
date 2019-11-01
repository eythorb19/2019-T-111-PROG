class Bug:
    MAX = 20
    MIN = 1

    def __init__(self, pos):
        self.__pos = pos
        self.__fix_pos()
        self.__step = 1

    def __fix_pos(self):
        if self.__pos > Bug.MAX:
            self.__pos = Bug.MAX
        elif self.__pos < Bug.MIN:
            self.__pos = Bug.MIN

    def move(self):
        self.__pos += self.__step
        self.__fix_pos()

    def turn(self):
        self.__step *= -1
        
    def __str__(self):
        line_str = ''
        for i in range(Bug.MIN, Bug.MAX+1):
            if i == self.__pos:
                line_str = line_str + 'b'
            else:
                line_str = line_str + 'x'
        return line_str
    
    def __gt__(self, other):
        return self.__pos > other.__pos
    
    def __add__(self, other):
        new_bug = Bug(self.__pos + other.__pos)
        return new_bug


