# for loop example
emails=['my@gmail.com','your@hotmail.com','their@gmail.com']
for item in emails:
    if 'gmail' in item:
        print(item)
        
# multiple for loop
names=['aldrin','francis','sydney']
email_domains=['yahoo','hotmail','gmail']

for i,j in zip(names, email_domains):
    print(i,j)
        
# while loop example
password=''
while password != 'helloworld':
    password=input("Enter password: ")
    if password == 'helloworld':
        print("You are logged in!")
    else:
        print("Sorry, try again!")