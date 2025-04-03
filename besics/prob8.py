password ="levelup96@Ddas"

if  len(password)<6:
    strength = "weak"
elif  len(password)<=10:
    strength = "medium"
else:
    strength="strong"

print("your password is", strength)