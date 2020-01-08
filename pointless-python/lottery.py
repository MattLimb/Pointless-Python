import random
import sys

def pick_number(lott_min, lott_max):
    nums_1 = [random.randint(lott_min, lott_max) for _ in range(0,10)]       
    nums_2 = [random.randint(lott_min, lott_max) for _ in range(0,10)]
    nums_3 = [random.randint(lott_min, lott_max) for _ in range(0,10)]
    nums_4 = [random.randint(lott_min, lott_max) for _ in range(0,10)]
    nums_5 = [random.randint(lott_min, lott_max) for _ in range(0,10)]

    nums = [nums_1, nums_2, nums_3, nums_4, nums_5]

    return random.choice(random.choice(nums))

try:
    lines = int(sys.argv[1])
except IndexError:
    lines = int(input("How Many Lines Do You Want To Make: "))
except ValueError:
    print("Value inputted not a number.")
    quit()

if lines > 70:
    print("You cannot buy more than 10 Tickets of 7 Lines each, at any one time in the UK. Please choose 70 or less lines.")
    quit()

all_lines = []

for _ in range(0, lines):
    all_lines.append([pick_number(1, 59) for _ in range(0, 6)])

lc = 1

for count, line in enumerate(all_lines):
    if count == 0:
        print(f"Ticket 1")
        print(f"________")

    if (count % 7 == 0) and (count != 0):
        print()
        print(f"Ticket {(count//7)+1}")
        print(f"________")
        lc = 1

    print(("Line {}: "+("{} "*6)).format(lc, line[0], line[1], line[2], line[3], line[4], line[5]))
    lc += 1