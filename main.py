'''1st .lenth of the string
x="ram, gopal"
print(len(x))
2nd.converta string which is anumber innature into integer and float
a=("10")
b=10.5
c=10.5
print(type(a))
print(int(b))
print(float(c))
x=float(5)
y=int(5.8)
z=complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
4th . list tuple converted
list=[1,2,3,4,5]
print((list))
print(type(list))
cov_tuple=(tuple (list))
print (cov_tuple)
print(type(cov_tuple))
5th . values of some keys in a dictionary
dic1={'a':2,'b':4}
dic2={'key1':'value1','key2':'value2'}
print(dic1)
print(dic2)
dic1={'a':1,'b':2}
dic2={'a':1,'b':2}
print(dic1)
print(dic2)
import sys
6th different size of tuple and list
list_=[1,2,3,4,5]
tuple_=(1,2,3,4,5)
print(sys.getsizeof(list_))
print(sys.getsizeof(tuple_))
7th . input:'welcome to python' output:ome to
name='welcome to python'
print(name[4:10])
 8th . print the following string in reverse order
name="my name is ram"
print(name[::-1])
x="hai ram"
print(x[::-2])
9th , write a program to get the following output
x=[10,5,4,20,1,15,12]
x.sort()
print(x)
ram=[3,2,43,45,12]
ram.sort()
print(ram)
10th .
list=[2,4,6,8,10,11,12,13,14,15]
# out_list=[]
# for i in list:
#     if i%2==0:
#         out_list.append(i)
# print(out_list)

#list compressions
print([i for i in list if i%2==0])
print([i for i in range(101) if i%2!=0])
print([i for i in range(51) if i%2!=0])


print({i:i**3 for i in range(10) if i%2!=0})
3rd .
j= [('a','  hi'),('b','hello'),('c','bye')]
print(type(j))
k =dict(j)
print(type(k))'''