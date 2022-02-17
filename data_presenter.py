cupcake_inv = open('./CupcakeInvoices.csv')

for row in cupcake_inv:
    print(row)

cupcake_inv.seek(0,0)

for row in cupcake_inv:
    order = row.split(',')
    print(order[2])

cupcake_inv.seek(0,0)

for row in cupcake_inv:
    order = row.split(',')
    inv_total = round(float(order[3]) * float(order[4]), 2)
    print(inv_total)

cupcake_inv.seek(0,0)

total = 0

for row in cupcake_inv:
    order = row.split(',')
    total += float(order[3]) * float(order[4])
    total = round(total, 2)

print(total)

cupcake_inv.seek(0,0)


import matplotlib.pyplot as plt

choc_total = 0
van_total = 0
stra_total = 0

for row in cupcake_inv:
    order = row.split(',')
    if order[2] == 'Chocolate':
        choc_total += float(order[3]) * float(order[4])
        choc_total = round(choc_total, 2)
    elif order[2] == 'Vanilla':
        van_total += float(order[3]) * float(order[4])
        van_total = round(van_total, 2)
    elif order[2] == 'Strawberry':
        stra_total += float(order[3]) * float(order[4])
        stra_total = round(stra_total, 2) 

cupcake_inv.close()

left = [1, 2, 3]

height = [choc_total, van_total, stra_total]

tick_label = ['Chocolate', 'Vanilla', 'Strawberry']

plt.bar(left, height, tick_label = tick_label, width = .8, color = [(0.48,0.25,0.00), (1, .992, .816, 1), 'pink'])

plt.xlabel('Flavor')

plt.ylabel('Sales ($)')

plt.title('Cupcake Sales')

# function to show the plot
plt.show()