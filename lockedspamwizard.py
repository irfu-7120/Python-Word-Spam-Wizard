print("welcome to spam wizard")
print("this program would let you have the termimal SPAM the word you want for any number of times")
i=1
while i<=3:
      print("type EXIT to exit")
      z=str(input("enter the password to get access"))
      i=i+1
      while z=="nigga":
            i=1
            print("to stop, type in 'stop'")
            x=str(input("type the word"))
            if x=="stop":
                   break
            y=int(input("how many times you wanna spam the word"))
            count=1
      
            while count<=y:
                  print (x)
                  count= count+1


      if z=="EXIT":
             break

      if z!="nigga" and z!="EXIT":
             print("wrong password dummy")
             match i:
                   case 2:
                        print("two attempts remaining")
                   case 3:
                        print("nga u got one more last attempt")



            
            
