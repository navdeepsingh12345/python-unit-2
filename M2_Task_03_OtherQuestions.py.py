#1-Sum of number digits in List

sum=0
lst=[1,2,3,"A","Hello",123.5,4,5,6,7,8,9]
for i in lst:
    if(type(i)==int):
        sum+=i
print(sum)
    
#Extact Words starting with K in String List.
slist=["Hey this is Rahul","my name is rakesh","Ravan is a bad boy"]
result=[]
K='R'
for s in slist: 
    l=s.split()
    for j in l:
        if(j[0].lower()==K.lower()):
            result.append(j)
print(result)
    

#Split String of list on Character
slist=["Hey this is Rahul","my name is rakesh","Ravan is a bad boy"]
result=[]
K="t"
for i in slist:
    l=i.split()
    result=result+l
print(result)


4- Count how many times ‘Ram’ has appeared in given phrase using string and list
s="However, Ram has been in the news for all the wrong reasons too. Illiterate bigots have weaponized the slogan Jai Shri Ram for wanton acts of violence, crime and hatred, which are anathema to what Ram actually stands for. These lumpen elements do not know that Ram is maryada purushottam, the epitome of rectitude, the touchstone of impeccable behaviour, the role model of the perfect human being, and the very incarnation of saumya rasa, harmonious equilibrium"
total=0
list=s.split()
for i in list:
    if(i=="Ram"):
        total+=1
print(total)

 #5-Replace ‘Ram’ with ‘Shree Ram’ in above phrase
s1=s.replace("Ram","Shree Ram")
print(s1)

#6- Sort all the words in above phrase in descending order using string and list
list=s.split(" ")
list.sort(reverse=True)
string=""
for i in list:
    string =string +i +" "
s3=string.rstrip()
print(s3)
s4=str(list)
print(s4)

s4=str(list)
print(s4)
print(s4[0])

#7- check if the list is sorted or not. If it is sorted then print “List is 
#sorted” else “List is not sorted” should be printed

lst=[1,2,3,4,5,7,6]# slicing return element
temp=lst[:]# list.sort() changes in existing file it didnot return anything
temp.sort() #temp=lst so they are pointing to the same memory
print(lst)
print(temp)
if(lst==temp):
     print("List is sorted")
else:
    print("Not Sorted")   