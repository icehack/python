class tailrec:
    def __init__(self,func):
        self.func = func
        self.recursivecall = False
        self.lastcall = False
    def __call__(self,*args,**kargs):
        print('Intercept call {0}{1}'.format(self.func, (args,kargs)))
        if self.recursivecall:
            self.recursivecall = False
            self.lastcall = False
            return (args, kargs)
        else:
            newargs, newkargs = args, kargs
            while True:
                self.recursivecall = True
                self.lastcall = True
                x = self.func(*newargs, **newkargs)
                if self.lastcall: return x
                newargs, newkargs = x[0], x[1]


@tailrec
def tailrecsum(x,y):
    ''' Efficient sum algorithm :) '''
    return y if x==0 else tailrecsum(x-1,y+1) 
    
print(tailrecsum(3,2))
