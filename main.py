from Func import *
import numpy as np

def SHA512(message):
  bin_data = stringToBinary(message)

  #Padding
  bin_data=bin_data.replace(" ", "")
  length_message="{0:0128b}".format(len(bin_data))
  n = int((len(bin_data) + len(length_message)) % 1024)
  final_message=""
  if n == 0:
      final_message= bin_data + length_message
  else:
      final_message += bin_data+'1' + format(0, 'b').zfill(1024-1 - n) + length_message

  #So khoi tin
  N = int(len(final_message) / 1024)
  print(N)
  #Dau vao ban dau
  a = "0110101000001001111001100110011111110011101111001100100100001000"
  b = "1011101101100111101011101000010110000100110010101010011100111011"
  c = "0011110001101110111100110111001011111110100101001111100000101011"
  d = "1010010101001111111101010011101001011111000111010011011011110001"
  e = "0101000100001110010100100111111110101101111001101000001011010001"
  f = "1001101100000101011010001000110000101011001111100110110000011111"
  g = "0001111110000011110110011010101111111011010000011011110101101011"
  h = "0101101111100000110011010001100100010011011111100010000101111001"
  prea=a; preb=b; prec=c; pred=d; pree=e; pref=f; preg=g; preh=h;
  
  for i in range(N):
    M = ''
    M += final_message[i * 1024:(i + 1) * 1024]

    #Word Expansion
    W=[]
    for j in range(16):
      W.append(M[j*64 : (j + 1)*64])
    for j in range(16, 80):
      st = ''
      st += additionModulo(RS19616(W[j - 2]), RS187(W[j - 15]))
      st = additionModulo(st, W[j - 7])
      st = additionModulo(st, W[j - 16])
      W.append(st)


    #80 Round
    for j in range(80):
      tron1 = additionModulo(RA(a), maj(a, b, c))

      tron2 = additionModulo(h, conditional(e, f, g))
      tron2 = additionModulo(tron2, RE(e))
      tron2 = additionModulo(tron2, W[j])    
      tron2 = additionModulo(tron2, Key[j])    
      
      h = g
      g = f
      f = e
      e = additionModulo(d, tron2)
      d = c
      c = b
      b = a
      a = additionModulo(tron1, tron2)

    #Cong modulo voi H truoc do  
    a= additionModulo(prea, a)
    b= additionModulo(preb, b)
    c= additionModulo(prec, c)
    d= additionModulo(pred, d)
    e= additionModulo(pree, e)
    f= additionModulo(pref, f)
    g= additionModulo(preg, g)
    h= additionModulo(preh, h)
    prea=a; preb=b; prec=c; pred=d; pree=e; pref=f; preg=g; preh=h;
  
  H = a + b + c + d + e + f + g + h
  result = ''
  for i in range(128):
    p, qw = hex(int(H[i * 4:(i + 1) * 4], 2)).split('x')
    result += qw
  return result

    


    
print (SHA512("Thuat toan cua minh thuc su la so mot cua viet nam luon do nha.Thuat toan cua minh thuc su la so mot cua viet nam luon do nha."))
