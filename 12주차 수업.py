from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()


# form itertools import combinations   <-- iterools 에샤, combinations만 호출
import itertools

# Sample list of items
items = ['A', 'B', 'C', 'D']

# Generate combinations of 2 items at a time
combinations_of_2 = list(itertools.combinations(items, 2))

# Generate combinations of 3 items at a time
combinations_of_3 = list(itertools.combinations(items, 3))

# Print the combinations
print("Combinations of 2 items:")
for combo in combinations_of_2:
    print(combo)

print("\nCombinations of 3 items:")
for combo in combinations_of_3:
    print(combo)
