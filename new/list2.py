#list is the one created or initialized under square brackets
friends = ["jim","carry","singh","harii"]
lucky_numbers=[4 ,69,69,69,69]
print(friends[1:3])
friends.sort()
print(friends)
f2=friends.copy()
f2.reverse()
print(f2)
friends.extend(lucky_numbers)
print(friends)
friends.reverse()
print(friends)
friends.append("arpitbaala")
print(friends)
friends.insert(3,"wushang")
print(friends)
friends.remove("wushang")
print(friends)
friends.pop()
print(friends)

print(friends.index("carry"))#you have to use the print keyword before friends.index("carry"), using it directly does nothing

friends.clear()

print(friends)
print(friends)
print(friends)
print(friends)
