#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(Weekdays, Vacation):

# (not weekdays,on  vacation )true   Weekend or vacation = true
# weekday , on vaction  false        not weekday and vacation = False    weekend and vacation 

 if not Weekdays or Vacation:
    return True
 else: 
    return False
sleep_in(False,False)  
sleep_in(False,True) 
sleep_in(True,False) 

#==================================================================================================

#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
 if  21 >=n:
  return (21-n)
 else:
   return ((n-21)* 2)

print (diff21(2))

#===================================================================================================

#Given an int n, return True if it is within 10 of 100 or 200. 
#Note: abs(num) computes the absolute value of a number.


def near_100(n):
 if  n > 90:
   return True 
 else: 
    return False

#near_100(67)
near_100(97)

#===================================================================================================

#Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
#The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str,n):

# We will be using string slicing 

 front= str[:n]
 back= str[n+1:]

 return front+back

missing_char("apple",2)

#=================================================================================================


#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
#We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    
# we have two conditions to work on if both smiling trouble and if even single not smiling trouble 

#first condition both smiling trouble

 if a_smile and b_smile:
    return True
#Even single not smiling trouble

 if not a_smile and not b_smile:
    return True
 return False

#different cases to check 
#monkey_trouble(True, True)
#monkey_trouble(True, False)
monkey_trouble(False, False)

#================================================================================================
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
#We are in trouble if the parrot is talking and the hour is before 7 or after 20.
#Return True if we are in trouble.

def parrot_trouble(talking, hour):
    
#We have two conditions binding to one talking hour less than 7 and hour more than 20 is trouble 
    if talking and hour < 7 or hour > 20:
        return True
    else:
        return False
#parrot_trouble(True, 6)    
parrot_trouble(True, 21)

#================================================================================================
#Given 2 int values, return True if one is negative and one is positive. 
#Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
 if a < 0  and b < 0 and negative:
       return True
 if a<0  or b<0 and not negative:
       return True 
 else:
        return False
    
pos_neg(1, -1, False)
#pos_neg(-1, 1, False) 
#pos_neg(-4, -8, True) 

#=================================================================================================
#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:-1]  # this will slice the tring from front and back with indices 0 and -1
  print(mid)
  # last + mid + first
  #return str[len(str)-1] + mid + str[0]
  return str[-1] + mid + str[0] 

front_back('Apple')

#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

#====================================================================================================
#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    if a==b:
     return ((a+b)*2)
    else:
     return (a+b)   
sum_double(5,5)
#sum_double(4,9)

#=======================================================================================================

#Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.

def makes10(a, b):
    
 if a==10 or b==10 or a+b==10:
        return True
 else:
        return False

makes10(9, 10) #→ True
#makes10(9, 9) # → False
#makes10(1, 9) #→ True

#======================================================================================================
#Given a string, return a new string where "not " has been added to the front. 
#However, if the string already begins with "not", return the string unchanged.

def not_string(str):
  if  str[:3] == "not":   #if first three character 'Not' 
    return "This string already begins with not."
  else:
    return "Not "+ str
#not_string("possible")
not_string("not possible")
#=======================================================================================================

#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. 
#Return a new string which is 3 copies of the front.

def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:3]
  return front *3 #multiply the front * 3 
front3('sagir') 


