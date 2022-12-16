#company_name = input("name company khod ra vared konid:")
#print("name:",company_name.title())

#your_first_name = input ("enter your first name:")
#message = input ("enter your massege:")
#print(f"your last name is {your_first_name} and your message is {message} welcome to my site")

#additon = "parsa" * 2000
#print(additon)
#f = 43
#m = 37
#me = 17
#j =(f + m + me) // 3
#print(j)


#andaze_ghaedeh = int(input("meghdar ghaedeh:") ) 
# andaze_ertefah = int(input("meghdar ertefah:"))
# a = andaze_ghaedeh * andaze_ertefah
#print(andaze_ghaedeh,andaze_ertefah,a)

# list = ["pouya","parsa",1,3,5,6,6,6,6,6]
# list.pop()  
# list.append() به اخر اضافه میکنه
#list.copy()
# x = list.count(6)
#cars = ["bmw","benz","ferari"]
# list.extend(cars)لیست هارو باهم مخلوظ میکند
#x = list.index("pouya")  برای کشتن است
# list.insert(0,"ali")اضافه میکنیم
#list.remove("parsa")برای حذف کردن
#list.reverse()لیست را معکوس میکند
# print(list)



#تمرین سوم
#tedadelitr = int(input("chand litr ab darid:"))
#harlitr = 950
#zarb =tedadelitr * harlitr
#molokol = harlitr // 3 * (10 ** -23)
#print("tedadelitr:,javab")






# تمرین شماره چهار
#hoghogh = int(input("hohgohg shoma cheghadr ast:"))
#m = hoghogh // 10
#b = hoghogh //100 * 7
#print(hoghogh,m,b) 


#تمرین 5
#liststd = []
#std1 = int(input("moadel ra vared konid:"))
#std2 = int(input("moadel ra vared konid:"))
#std3 = int(input("moadel ra vared konid:"))
#std4 = int(input("moadel ra vared konid:"))
#liststd.sort()
#print(liststd)

#تمرین 6
#listaadad = ["aadad1","aadad2","aadad3","aada4","m"]
#aadad1 = int(input("aad aval ra vard konid:"))
#aadad2 = int(input("aad dovom ra vared konid:"))
#aadad3 = int(input("aad sevom ra vared konid:"))
#aadad4 = int(input("adad charom ra vared konid:" ))
#m = (aadad1 + aadad2 + aadad3 + aadad4) // 4
#print(aadad1,aadad2,aadad3,aadad4,m)




#name = "parsa golzar"
#print(name[0:5])



#age = int(input("how old are you:"))
#if age < 20:
 #   print("you are so gogoli")
#else:
#    print("vaghte zan gereftane pasaram")    


#name = input("your name:")
#if name[::-1]  == name:
 #   print("thats same")
#else:
 #   print("nemishe dasham")    




# tedadelitr = int(input("chand litr ab darid:"))
# harlitr = 950
# zarb =tedadelitr * harlitr
# molokol = harlitr // 3 * (10 ** -23)
# javab = zarb / molokol
# print(javab)


     

# sen = int(input("how old are you: "))
# daghighe = 60
# saat = daghighe * 60
# roz = saat * 24
# sal = roz * 365
# javab = sal * sen
# print(javab) 

# mylist = []
# for i in range(4):
#     aad = int(input("aad ra vared ko:"))
#     mylist.append(aad)
# print(mylist)

# listaad = []
# oodlist = []
# aad = int(input("aad ra vared kon: "))
# for i in range(aad+1):
#     if i % 2 == 0:
#         listaad.append(i)
#     else:
#         oodlist.append(i)
#         continue
# print(len(listaad))
# print(len(oodlist))
import random

laps = 10
hadsaval = 1
for i in range(laps):
    aadsistem = random.randint(0,2)
    adadshoma = int(input("enter your number: "))
    if aadsistem == adadshoma:
        print(f"thats true.with{hadsaval}")
        break
    else:
        hadsaval += 1
        
        print("try agane")










