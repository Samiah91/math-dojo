class MathDojo:
def __init__(self,result,num,nums):
    self.result=result
    self.num=num
    self.nums=nums



def add ( self,num, *nums):
    result = 0
    for i in nums:
    result += i
    self.result += result
    return self

def subtract (self,num, *nums):
    result = 0
    for i in nums:
    result += i
    self.result += result
    return self





x = MathDojo(0,0,0)

x.add(2).add(2,5,1).subtract(3,2)
print(x)	


