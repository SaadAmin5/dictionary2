#count number of times a name is repeated using dictionary

list1=['john', 'mark', 'peter', 'peter', 'mark', 'peter', 'peter', 'mark']

a={}
for i in list1:
    a[i]=list1.count(i)
    
print(a)