# Loop through all numbers from 0 to 100
for i in range(101):
    # Numbers ending in zero are always divisible by 10 with no remainder
    # We skip 0 itself as well based on the logic
    if i % 10 != 0:
        print(i)