#name=input("enter your name")
#dd=int(input("enter your birth date (dd)"))
#mm=int(input("enter your birth month (mm)"))
#mm=int(mm)#handling the 0 case 
#yyyy=int(input("enter your birth year (yyyy)"))

address=input("enter your address : ")
#city=input("enter your city : ")



#function for checking the first condition that is is the city entered in the address.
def check_city(address,city):
    address.lower()
    city.lower()
    
    #create a list on the basis of whitespaces
    new_address=address.split()
    if new_address[-1]==city:
        return True
    else:
        return False

def remove_city(address,city):
    address=address.replace(city,"")
    return address



def remove_specialchar(address):
    new_address=""
    for i in address:
        if i.isalnum():
            continue
        else:
            new_address=address.replace(i,"")
    return new_address


                    #or
    #we can make it a list new_address=list(address)
    #and theb use new_address.remove(i) in the else condition

    #alternate method for this can also be using the following ethod:
    #new_address=""
    #for i in address:
    #    if i.isalnum():
    #        new_address+=i
    #return new_address


            #or 

    #new_add=[]
    #for i in address:
    #    if i.isalnum():
    #        new_add.append(i)
    #return "".join(new_add)
#def relpacement(address):
    #vowels=["a","e","i","o","u"]
    #for i in address:
        #if i in vowels:
         #   address=address.replace(i,chr(ord(i)+1))
        #else:
       #     while i not in vowels:
      #          i=chr(ord(i)+1)
                #need to check this out it is a goodthing


    
    #return address


def check_validity(dd,mm,yyyy):
    if dd<1 or dd>31:
        return False
    if mm<1 or mm>12:
        return False
    if yyyy<1900 or yyyy>2024:
        return False
    return True






def next_prime(dd):
    if dd==1:
        return 2
    else:
        while True:
            dd+=1
            if dd>31:
                dd=2
            for i in range(2,dd):
                if dd%i==0:
                    break
            else:
                return dd


import math

def check_arm(yyyy):
    #check if yyyy is armstrong number
    dgt=0
    summ=0
    num=10
    while yyyy>0:
        dgt+=yyyy%num
        summ=summ+math.pow(dgt,3)
        num*=10
        yyyy//=num
    if summ==yyyy:
        return True
    else:
        return False
def check_palin(dd,mm,yyyy):
    dob=str(dd)+str(mm)+str(yyyy)
    if dob==dob[::-1]:
        return True
    else:
        return False
def count_alphanum(address):
    count=0
    for i in address:
        if i.isalnum():
            count+=1
    return count




def check_simialr(address,dd,mm,yyyy):
    dob=str(dd)+str(mm)+str(yyyy)
    same=[]
    for i in address:
        if i in dob:
            same.append(i)
    return same


def check_divisiblity(dd,mm,yyyy):
    summ_ofyear=0
    dob=str(dd)+str(mm)+str(yyyy)
    year=(yyyy)

    while year>0:
        summ_ofyear+=year%10
        year//=10
    if int(yyyy)%summ_ofyear==0:
        print(f"{yyyy} is divisible by sum of digitsof year that is {summ_ofyear}")
    if int(dob)%(summ_ofyear)==0:
        print(f"{dob} is divisible by sum of digits of year  that is  {summ_ofyear}")
    else:
        print("none of them is  divisible")
def patternn_printing(dd):
    if dd%2==0:
        n = int(input("Enter the number of levels for the pyramid: "))

        for i in range(1, n + 1):
            spaces = n - i
    
            print(" " * spaces, end="")
    
            print(" ".join([str(i)] * i))
    else:
        n = int(input("Enter the number of levels for the pyramid: "))

        for i in range(1, n + 1):
            spaces = n - i
            print(" " * spaces, end="")
    
            for j in range(i):
                print(i + j, end=" ")
    
            print()

def replacechar(address):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    new_address = ""
    for i in address:
        if i in vowels:
            index_of_i = alphabets.index(i)
            while index_of_i < len(alphabets) and alphabets[index_of_i] in vowels:
                index_of_i += 1
            if index_of_i < len(alphabets):
                new_address += alphabets[index_of_i]
            else:
                new_address += i
        elif i in consonants:
            index_of_i = alphabets.index(i)
            while index_of_i < len(alphabets) and alphabets[index_of_i] not in vowels:
                index_of_i += 1
            if index_of_i < len(alphabets):
                new_address += alphabets[index_of_i]
            else:
                new_address += i
        else:
            new_address += i

    return new_address

print(replacechar(address))
