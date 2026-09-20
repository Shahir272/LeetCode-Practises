d="abcdabz"
arr = [0] * 26
for i in range(len(d)):
  arr[ord(d[i])-ord('a')] += 1
for i in range(len(d)):
  if arr[ord(d[i])-ord('a')] == 2:
    print(d[i])
    break