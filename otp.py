import secrets
print("we are generating otp")
sec=secrets.SystemRandom()
otp=sec.randrange(1000,9999)
print("your otp is",otp)
