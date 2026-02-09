#sawed email address
#a)draw name from email in the form name@service.com
email1 = input("Enter an email address(name@service.com) ")
#to print only the name before @
print(email1.split("@")[0])

#if the mail is ghansikareddy@gmail.com
#it prints only (ghansikareddy)


#b)draw name from email in the form of info@name.com
email2 = input("Enter an email address(info@name.com) ")
print(email2.split("@")[1].split(".com")[0])