a = [10, 20, 30, 40]
b = a

b[1] = 50

# print(b)

# print(a)

# a = [10, 20, 30, 40]
# b = a.copy()
# b[1] = 50
# print(a)
# print(b)

print(id(a))
print(id(b))

a = {"next":{"next":{"next":{"next":{"next":{"next":{"final":{"employer":"Deloitte"}}}}}}}}
d = a
for item in d:
    key = item
    break
while d[key]:
    d = d[key]
    print(d)
    for item in d:
        key = item
        break
    try:
        d[key]
    except:
        break


a = {"next":{"next":{"next":{"next":{"next":{"next":{"final":{"employer":"Deloitte"}}}}}}}}
b = a["next"]
while type(b)==type(a):
    for i in b:
        x=i
    b=b[x]
print(b)



# Testing