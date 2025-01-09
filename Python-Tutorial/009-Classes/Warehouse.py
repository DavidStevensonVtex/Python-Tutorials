class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print("w1", w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print("w2", w2.purpose, w2.region)
print("w1", w1.purpose, w1.region)

# $ python Warehouse.py
# w1 storage west
# w2 storage east
# w1 storage west