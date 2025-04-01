l=["red", "yellow", "green"]
print(l[1])
l[1]="pink"
print(l)
l[0]= "pink"
l[1]= "red"
l.append("violet")
print(l)
l.insert(1,"blue")
l2=["orange", "peach"]
l.extend(l2)
print(l)
l.remove(l[2])
print(l)
l.clear()
print(l)