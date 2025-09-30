# Ignore Middle
# Unpack values from a tuple of four elements, but only keep the first and last values.

data = (100, 200, 300, 400)

a, *_, c = data

print(a, c)