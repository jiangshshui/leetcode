
# def test():
#     return [s+t for s in "ab" for t in "cd"]
#
# print(test())

# a=['asd','ddf','32432']
# print(a.pop())
# a.append("sb123")
# print(a)

# a=set()
# a.add(1)
# a.add(12)
# for item in a:
#     print(item)


# for i in range(10-1,-1,-1):
#     print(i)
# i=0
#
# i+=9+1
# print(i)


# class spam():
#     pass
#
# s=spam()
# s2=spam()
# print(s)
# print(s2)
# print(s and s2)


# a=1
# print(bin(a))
# b=bin(a)
# print(type(b))
# print(a==b)

# print(9//2)

# mappings={
#     1:'a',
#     2:'b'
# }
# print(mappings[1])

# a='A'
# print(ord(a))
# print(ord('0'))
# print(ord('1'))
# print(ord(a)-ord('0'))

# a="432b"
# print(int())

# a=[[1,2],[3,4]]
# print(len(a)*len(a[0]))

# print('ABc'.isupper())

# a="abcdef"
# print(a[1:])

# print((12%9+35%9)%9)
#
# print(47%9)


# s1=set("abced")
# s2=set("abc")
# print("".join(s1-s2))
# print(s2-s1)

# a=b=0
# print(a,b)


# def MapTest(A):
#     return [a+2 for a in A]
# A=[1,2,3]
# B=[4,5,6]
# l=map(MapTest,(A,B))
# print(A)
# print(B)
# print(*l)


# A=[(1,'b'),(1,'a'),(2,'a'),(0,'c'),(0,'a')]
# print(min(A))
# print(sorted(A))

# a="12345"
# index=a.find('1')
# print(index)
# a=a[:index]+a[index+1:]
# print(a)

print([x for x in range(10,1,-1)])

# from queue import PriorityQueue
# q=PriorityQueue()
# q.put((3,"ad"))
# q.put((4,"ad"))
# q.put((5,"ad"))
# print(q)
#
# while q.qsize():
#     print(q.get())


a=['12','23']
a.append(['dfg','gf'])
a.extend(['dfg','gf'])
print(a)

