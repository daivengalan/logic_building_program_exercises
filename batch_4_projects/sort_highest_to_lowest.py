number_series = []

while True:
    entry = input("Enter a number (non-numeric to stop): ")
    if not entry.replace('.', '', 1).isdigit():
        break
    number_series.append(float(entry))

# The reverse=True argument sorts from largest to smallest
number_series.sort(reverse=True)

print("Numbers from highest to lowest:")
for value in number_series:
    print(value)