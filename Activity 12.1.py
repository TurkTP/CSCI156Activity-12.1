__author__ = 'Luke'
#1. Write a program that asks for a users email address.
#2. Pass this email address, as a string, to a function that uses a tuple to split the email address into username, domain, and generic
#top level domain (gTLD - .com, .gov, .edu, .org, .mil, .net).
#3. Make sure your functions tests that they have provided a proper email address format: it must have an @ symbol and a
#. followed by a proper gTLD. For this assignment a proper gTLD is .com, .gov, .edu, .org, .mil, or .net, the actual list
#of proper gTLD's is much longer.
#4. Your function should return the username, domain, and gTLD as a tuple.

email=str(input('Enter an email address examplename@exampledomain.etc:'))
def cut(email):
    testat = '@' in email
    testdot = '.' in email
    if testat == True and testdot == True:
        username, domainname = email.split('@')
        xmail, dotwha = domainname.split('.')
    else:
        print("Incorrect email format")
    print(username)
    print(domainname)
    print(xmail)
    print(dotwha)
