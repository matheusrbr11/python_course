import secrets
import string

def createPw(pwlength=12):
    letters = string.ascii_letters
    digits = string.digits
    specialchars = string.punctuation
    
    alphabet = letters + digits + specialchars
    pwd = ''
    pwStrong = False
    
    while not pwStrong:
        pwd = ''
        for i in range(pwlength):
            pwd += ''.join(secrets.choice(alphabet))
        
        if (any(char in specialchars for char in pwd) and sum(char in digits for char in pwd) >=2):
            pwStrong = True
    return pwd

print(createPw())