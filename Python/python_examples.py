for i in range(1,11):
	print(i*i)

#Result: 
#1
#4
#9
#16
#25
#36
#49
#64
#81
#100

for i in [1,3,5,7,9]:
	print(i, ":", i**3)
print(i)

#Result:
#(1, ':', 1)
#(3, ':', 27)
#(5, ':', 125)
#(7, ':', 343)
#(9, ':', 729)
#9

ans = 0
for i in range(1,11):
	ans = ans + i*i
	print(i)
print(ans)

#Result:
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10
#385

for ch in "aardvark":
	print(ch)
#Result:
#a
#a
#r
#d
#v
#a
#r
#k

for w in "Now is the winter of our discontent...".split():
	print(w)

#Result
#Now
#is
#the
#winter
#of
#our
#discontent

msg = ""
for s in "secret".split("e"):
	msg = msg + s
print(msg)

#Result:
#scrt

msg = ""
for ch in "secret":
	msg = msg + chr(ord(ch)+1)
print(msg)

#Result:
#tfdsfu





