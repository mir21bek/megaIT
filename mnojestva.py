months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
months_c = months_a.union(months_b)
print(months_c)
months_c.add('dec')
print(months_c)
months_c = {"Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "dec"}
for i in months_c:
    print(months_c)

x = {1, 2, 3}
y = {4, 3, 6}
a = x.intersection(y)
print(a)