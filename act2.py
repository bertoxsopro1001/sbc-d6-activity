range_ = int(input("Enter range :"))
for i in range(range_,-1,-1):
      if i == 1:
          print("*",end= "")
          print(" " * range_,end="* " )         
      else:
          print("*" * i)
for x in range(2,range_+ 1,1):
    print("*" * x)
    

                     
                
