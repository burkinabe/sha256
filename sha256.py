from char_to_bit import charToBit
from padding import padding
from split import split
from compression import IV
from schedule import calculate_schedule
from compression import compression
from compression import K


def sha256(string):
  # 0. Convert String to Binary
  # ---------------------------
  message = charToBit(string)
  print("Message original : "+string)
  print("Message en bit : "+message)

  # 1. Preprocessing
  # ----------------
  # Pad message
  padded = padding(message)
  print("Message paddé : "+padded)

  # Split up in to 512 bit message blocks
  blocks = split(padded, 512)
  print("Blocs de message : ")
  print(blocks)

  # 2. Hash Computation
  # -------------------
  # Set initial hash state using initial hash values
  hash = IV
  print("Valeurs initiales : ")
  print(hash)
  # For each message block
  for block in blocks:
    # Prepare 64 word message schedule
    schedule = calculate_schedule(block)

    # Remember starting hash values
    initial = hash

    # Apply compression function to update hash values
    hash = compression(initial, schedule, constants = K)

  print("Après compression : ")
  print(hash)
  # 3. Result
  # ---------
  # Convert hash values to hexadecimal and concatenate
  hashResult = ""
  for h in hash:
      hashResult = hashResult+hex(h)
  return hashResult.replace('0x', '')