# Email Slicer

# Email Slicer is an essential project that accepts
# an email address as its input and produces the
# username and domain of the entered email
# address.

print("Enter Your Email id:- ")
email = input().strip()

if email.find("@") != -1:
    username = email[:email.index("@")]
    domain = email[email.index("@") + 1:]
    print("Your username is:- ", username)
    print("Your domain is:- ", domain)
else:
    print("Please enter valid email Id.")