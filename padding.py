def padding(message):
  l = len(message)
  k = (448 - l - 1) % 512
  l64 = format(l, '064b')
  return message + "1" + ("0" * k) + l64