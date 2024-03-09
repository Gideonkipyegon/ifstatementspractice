#for loop
names= ['john', 'paul', 'george', 'ringo']
for name in names:
    print(name)
#range function
Towns= ['london', 'new york', 'paris', 'oslo']
for i in range(5):
    print(Towns)

#while loop
count = 0
while count <=10:
   print(count)
   count +=1

#break
colors=['red','blue','white','yellow','green']
color_i_need='yellow'
for color in colors:
 if color == color_i_need:
  print('they have the color i need')
  break
print(color)

#continue
ages =[21,27,30,36]
for age in ages:
   if age<30:
    continue
   print(age)

#nested loop
groups=[['jane','boyt','kamau'],['john','kandi']]
for group in groups:
  for name in group:
    print(name)

#list comprehesions
nums=[20,39,40,56,-51]
doubled=[]
for num in nums:
  doubled.append(num*2)
  print (doubled)