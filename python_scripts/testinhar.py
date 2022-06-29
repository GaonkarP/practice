
import regex as re

def countwords():

  instr = input("please input the string:")
  newstr = instr.split()
  print(f"number of words in string are-->{len(newstr)}")
  uppercase = 0
  lowercase = 0
  splchar = 0

  otherspl = 0
  for charr in instr:
    if((charr >= 'a' and charr <= 'z') or (charr == " ") or (charr >= 'A' and charr <= 'Z') or (charr >= '0' and charr <= '9')): 
        pass
    else:
        print("printing char")
        splchar += 1 
  


    if charr.isprintable():
        if charr.isupper():
            uppercase += 1
        elif charr.islower():
            lowercase += 1
        elif charr.isalnum():
            lowercase += 1
        elif charr.isdigit():
            pass
        else:
            otherspl +=1

      

  print(f"special char{splchar}")
  print(f"number of uppercase character in string are-->{uppercase}")
  print(f"number of lowercase character in string are-->{lowercase}")
  print(f"number of special character in string are-->{otherspl}")

  revstr = instr[::-1]
  print(f" reversed string {revstr}")

countwords()