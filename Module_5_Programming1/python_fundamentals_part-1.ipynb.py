Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> input()
data science
'data science'
>>> a = 5
>>> if a == 5:
	# 4 indented spaces to this block of code
	print("a equals 5")

	
a equals 5
>>> 
>>> myString = 'hello world'
>>> print(type(myString))
<class 'str'>
>>> 
>>> n = 10
>>> print(type(n))
<class 'int'>
>>> 
>>> n_float = 7.5
>>> print(type(n_float))
<class 'float'>
>>> 
>>> single_string = 'Its a single quote string'
>>> print(double_string)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(double_string)
NameError: name 'double_string' is not defined
>>> single_string = 'Its a single quote string'
>>> print(single_string)
Its a single quote string
>>> double_string = "It's a double quote string"
>>> print(double_string)
It's a double quote string
>>> 
>>> n1 = 5
>>> n2 = 7.5
>>> print(n1+n2)
12.5
>>> 
>>> nstrl = "abc"
>>> print(nstrl + n1)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(nstrl + n1)
TypeError: can only concatenate str (not "int") to str
>>> 
>>> nstr2 = "def"
>>> print(nstrl + nstr2)
abcdef
>>> 
>>> n1, n2 = 10, 11
>>> n1
10
>>> n2
11
>>> 
>>> 
>>> result = 3 + 4.0 / 2 * 5 # DMAS
>>> print(result)
13.0
>>> # module operator #
>>> remainder = 17%10
>>> print(remainder)
7
>>> # x ^ n
>>> x = 5
>>> n = 4
>>> print(x ** n)
625
>>> 
>>> nstr = "abc"
>>> ans = nstr * 10
>>> print(len(ans))
30
>>> 
>>> 
>>> 
>>> name = "Harshit"
>>> print("%s is a data scientist!" %name)
Harshit is a data scientist!
>>> name.upper()
'HARSHIT'
>>> name.lower()
'harshit'
>>> nstr = "it is a nice day today."
>>> nstr.capitalize()
'It is a nice day today.'
>>> name.index('s')
3
>>> name[2:5]
'rsh'
>>> name[2:6:2]
'rh'
>>> alist = [3,4,5]
>>> print(alist)
[3, 4, 5]
>>> alist = ['harshit' , 2, 5.5]
>>> print(alist)
['harshit', 2, 5.5]
>>> alist.append(10)
>>> alist.append(15)
>>> print(alist)
['harshit', 2, 5.5, 10, 15]
>>> alist.pop()
15
>>> alist.pop()
10
>>> alist.pop()
5.5
>>> print(alist)
['harshit', 2]
>>> alist[3]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    alist[3]
IndexError: list index out of range
>>> alist.pop()
2
>>> alist.append(10)
>>> alist.append(15)
>>> print(alist)
['harshit', 10, 15]
>>> alist = ['harshit', 2, 5.5]
>>> print(alist)
['harshit', 2, 5.5]
>>> alist.append(10)
>>> alist.append(15)
>>> print(alist)
['harshit', 2, 5.5, 10, 15]
>>> alist.pop()
15
>>> alist[3]
10
>>> alist[1:]
[2, 5.5, 10]
>>> alist.append([1,2,3])
>>> print(alist)
['harshit', 2, 5.5, 10, [1, 2, 3]]
>>> alist*2
['harshit', 2, 5.5, 10, [1, 2, 3], 'harshit', 2, 5.5, 10, [1, 2, 3]]
>>> alist + alist
['harshit', 2, 5.5, 10, [1, 2, 3], 'harshit', 2, 5.5, 10, [1, 2, 3]]
>>> 