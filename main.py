# РАССТОЯНИЕ ЛЕВЕНШТЕЙНА

str1 = input('ВВОД: ')
str2 = input('ВВОД: ')

def distans(a, b):
  def dist(i, j):
    if i == 0 or j == 0:
      return max(i, j)

    elif a[i-1] == b[j-1]:
      return dist(i-1, j-1)
    
    else:
      return 1 + min(
        dist(i, j-1),
        dist(i-1, j),
        dist(i-1, j-1),
        )
  return dist(len(a), len(b))

print(distans(str1, str2))
