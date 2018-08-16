x	=	50
def	func():
				global	x
				print('x	is',	x)
				x	=	2
				print('Changed	global	x	to',	x)
func()
print('Value	of	x	is',	x)

list1 = [1,2,3,4,5]
list2 = [2*i for i in list1 if i >= 3]
print('list 2 is',list2)
x=list2.pop()
print(x)
print(list2)