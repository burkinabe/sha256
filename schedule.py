from sigma1 import sigma1
from add import add
from sigma0 import sigma0

def calculate_schedule(block):
    chunk = len(block)
  # The message block provides the first 16 words for the message schedule (512 bits / 32 bits = 16 words)
    schedule = []
    schedule = [ int(block[i:i+32], 2) for i in range(0, chunk, 32) ]# convert from binary string to integer for calculations
    # Calculate remaining 48 words
    for i in range(16, 63):
        print(i)
        schedule.append(add(sigma1(schedule[i - 2]), schedule[i - 7], sigma0(schedule[i - 15]), schedule[i - 16]))

    return schedule
