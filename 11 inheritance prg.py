import math

class Triangledim():

    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.s = (self.l1+self.l2+self.l3) / 2.0

    def checktri(self):
        if (self.l1+self.l2>self.l3) and (self.l2+self.l3>self.l1) and (self.l1+self.l3>self.l2): 
            print("Perimeter of the triangle is: {}".format(self.s))
        else: 
            print("not the right triangle proportions") 

            else:
    def findArea(self):
        area = math.sqrt(self.s*(self.s-self.l1)*(self.s-self.l2)*(self.s-self.l3))
        print("The area of the triangle is: {}".format(area))

if __name__ == "__main__":
    p = Triangledim(7,5,10)
    p.checktri()
    p.findArea()
