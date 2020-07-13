# country = ‘India,Pakistan,Nepal,Srilanka’
# SyntaxError: invalid character in identifier

# a,b,c,d=country.split(',')
# s = d.upper + ‘ VS ’ + a.upper
# syntaxError: invalid character in identifier
# print(s)

country = "India, Pakistan, Nepal, Srilanka"
a, b, c, d = country.split(',')
s = d.upper() + ' VS ' + a.upper()
print(s)