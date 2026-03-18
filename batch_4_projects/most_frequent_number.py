collected_data = []

while True:
    entry = input("Enter a number (non-numeric to stop): ")
    if not entry.replace('.', '', 1).isdigit():
        break
    collected_data.append(float(entry))

if collected_data:
    # Use max with a key to find the item with the highest count
    most_frequent = max(set(collected_data), key=collected_data.count)
    print(f"The number with the most duplicates is: {most_frequent}")