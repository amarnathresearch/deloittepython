a = {}

a["key1"] = "Amarnath"
a["key2"] = "Deloitte"
a[3] = "India"
print(a)

print(a["key2"])

b = {"id":'100', "name":"Amar", "desig": "trainer"}
print(b)

print(b["id"])


c ={"ids":[10, 20, 30], "names":["amar", "deloitte", "India"]}
print(c)

print(c["names"][1])


d = [10, 20, 30, c]

print(d)


e = (100, 200, 300)

print(e)

print(e[0])
print(e[2])

f = (400, 500, 600)

g = e+f
print(g)

# g.append(800)

# SET ?

h = {10, 20, 30, 10, 10}
print(h)

for i in h:
    print(i)

for i in f:
    print(i)

print(dir(h))

u = {"id":"10", "name":"amarnath", "desig":"mentor"}

for i in u:
    print(i, u[i])
    
a = {"next":{"next":{"next":{"next":{"next":{"next":{"final":{"employer":"Deloitte"}}}}}}}}

# print(a)

# while( b != "Deloitte"):
    
#     b = a["next"]
# print(b)


b = a["next"]
print(b)

c = b["next"]
print(c)

d = c["next"]
print(d)

e = d["next"]
print(d)

f = e["next"]
print(f)

g = f["next"]
print(g)

h = g["final"]
print(h)

i = h["employer"]
print(i)

a = {"next":{"next":{"next":{"next":{"next":{"next":{"final":{"employer":"Deloitte"}}}}}}}}

b = a["next"]

while b != "Deloitte":
    
    if b == "Deloitte":
        break
    elif b == "next":
        b = b["next"]
    elif b == "final":
        b = b["final"]
    elif b == "employer":
        b = b["employer"]
    else:
        b = b["next"]
    
print("output", b)
