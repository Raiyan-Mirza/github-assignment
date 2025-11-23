#Raiyan Mirza
#19-oct-2025
#python 1st assignment - Daily calorie Tracker

print("hey this is your daily calorie tracker")
n=int(input("enter total number of meals"))
meal=[]
cal=[]
sum=0
l=int(input("enter your daily calories limit:"))
for i in range(n):
  m=input("enter meal name")
  meal.append(m)
  c=int(input("enter calories"))
  cal.append(c)
  sum=sum+c
print("Meal Name", "   " , "Calories")
print("------------------------")
avg=sum/n
for i in range(len(meal)):
  print( meal[i],"    ",cal[i])
print("total calories you ate:",sum)
print("average calories per meal:",avg)
if(sum>l):
    print("Warning calories surplus")
else:
    print("within limit")        


  
  
  