class PhoneCustomer:
    # DayOfSendingBill = "Monday"
    # CustomerID = 123
    # FirstName = "David"
    # LastName = "Stevenson"

    def __init__(self):
        self.DayOfSendingBill = "Monday"
        self.CustomerID = 123
        self.FirstName = "David"
        self.LastName = "Stevenson"

pc = PhoneCustomer()
print(F"Day of Sending Bill: {pc.DayOfSendingBill} Customer ID: {pc.CustomerID}")
print(f"FirstName: '{pc.FirstName}' LastName: '{pc.LastName}'")

# $ python PhoneCustomer.py 
# Day of Sending Bill: Monday Customer ID: 123
# FirstName: 'David' LastName: 'Stevenson'