"""this is a simple program hello world."""
print("Hello, World!")
a=1
print('a =',a)

def print_emails(fname):
    file = open('email_address.txt','r')
    Lines = file.readlines()
    
    count = 0
    for line in Lines:
        count += 1
        print ("Line(): ()" .format(count, line))