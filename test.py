# class Calculator:
#     def __init__(self, n1, n2):
#         self.n1 = n1
#         self.n2 = n2
    
#     def add(self):
#         print(self.n1+self.n2)
    
#     def subtract(self):
#         print(self.n1-self.n2)

# calc = Calculator(10, 6)
# calc.add()
# calc.subtract()


# l = [3,4,5,6,89,89,54]
# l1 = set(list(l))
# l1 = sorted(l1)
# print(l1[-2])


# s = '@Arun@@'
# result = '@Arun'

# for i in s:
#     if 


import pandas as pd

d = {
    'name':['Arun', 'Aman', 'Ravi'],
    'age':[25,26,27],
    'last_name':['Kumar', 'Singh', 'Pandey'],
}

df = pd.DataFrame(d)
print(df)

df = df.rename(columns={'name':'first_name'})
print(df)







