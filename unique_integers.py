#Given an integer n, return any array containing n unique integers such that they add up to 0.

def unique_integers(n):
  list = []
  if n == 0:
    return list
  sum = 0
  for i in range(1, n):
    list.append(i)
    sum = sum + i
  list.append(-sum)
  return list

if __name__ == "__main__":
    for i in range(1,10):
        print(unique_integers(i))
