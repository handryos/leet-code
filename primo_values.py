import math


def ehPrimo(n):
  if n == 1:
    return False
  elif n != 2 and n % 2 == 0:
    return False
  else:
    primo = True
    raiz = int(math.sqrt(n))
    for i in range(3, raiz + 1, 2):
      if n % i == 0:
        primo = False
        break
    return primo


def storeValuesRecursivo(current, limit, values=[]):
  if current >= limit:
    return values
  if ehPrimo(current):
    values.append(current)
  return storeValuesRecursivo(current + 1, limit, values)


def storeValues(limit):
  values = []
  for i in range(1, limit):
    if ehPrimo(i):
      values.append(i)

  return values


print(storeValuesRecursivo(1, 100))
print(storeValues(100))
