shopList=['apple','mango','carrot','banana']
print('i have', len(shopList), 'items to purchase')

print('These items are:', end=' ')
for i in shopList:
    print(i,end=' ')

print('\ni also have to buy rice')
shopList.append('rice')
print('My shopping list is now', shopList)

print('lets sort my list')
shopList.sort()
print('sorted shopping list is',  shopList)

print('the first item i will buy is', shopList[0])
oldItem=shopList[0]
del shopList[0]
print('i bought', oldItem)
print('my shopping list is now', shopList)

print(type(shopList))