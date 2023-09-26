def descriptografar(permutacao, frase_embaralhada):
  """
  Descriptografa uma frase que foi criptografada usando uma permutação inversível.

  Args:
    permutacao: Uma sequência de 26 letras minúsculas que representam a ordem das letras do alfabeto na frase criptografada.
    frase_embaralhada: A frase criptografada.

  Returns:
    A frase original.
  """

  alfa_normal = [chr(ord("a") + i) for i in range(26)]
  frase_correta = ""

  for letra in frase_embaralhada:
    indice = permutacao.index(letra)
    frase_correta += alfa_normal[indice]

  return frase_correta

if __name__ == "__main__":
  permutacao = input("Digite a permutacao: ")
  frase_embaralhada = input("Digite a frase criptografada: ")

  frase_correta = descriptografar(permutacao, frase_embaralhada)

  print("A frase original é:", frase_correta)
