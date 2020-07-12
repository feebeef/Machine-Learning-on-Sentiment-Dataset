


a = w[1000:2000]

# print(len(a))
# print(a[len(a)-1])
res = {}

def recursion(l):
    if(len(l) == 0):
        print("none")
    else:
        temp = re.findall(l[0], ''.join(l))
        res[temp[0]] = len(temp)
        filtered = filter(lambda i: i != temp[0] , l) 
        recursion(filtered)

recursion(a)

items = res.items()

sorted_items = sorted(res.items(), key=operator.itemgetter(1))
print(sorted_items)

