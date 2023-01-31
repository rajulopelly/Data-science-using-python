class test:
    n=1
    def _init_ (self):
        print("In constructor ",self.n)
    def disp(self, val):
        self.n = val
        print("disp called",self.n)
    def print(self):
        print(val)
t4=test()
print(t4.n)
#print(t4.val)
t4.disp(10)
t4.print()
