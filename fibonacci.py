functionType = input(
    "Digite 1 para uma função linear e 0 para uma função recursiva: ")


def fib(n: int):
  if functionType == "1":
    if n == 0:
      return 0
    elif n == 1 or n == 2:
      return 1
    prev_value = 1
    current_value = 1
    for _ in range(3, n + 1):
      next_value = prev_value + current_value
      prev_value = current_value
      current_value = next_value
    return current_value
  else:
    if n == 0:
      return 0
    elif n == 1 or n == 2:
      return 1
    return fib(n - 1) + fib(n - 2)


try:
  n = int(input("Digite um número inteiro: "))
  resultado = fib(n)
  print(resultado)

except ValueError:
  print("Insira um número inteiro válido.")
