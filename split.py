def split(message, size = 512):
    chunk = len(message)
    return [ message[i:i+size] for i in range(0, chunk, size) ]

