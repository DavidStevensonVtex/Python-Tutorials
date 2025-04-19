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

    def MethodName(self):
        return f"Day to send Bill: {self.DayOfSendingBill} Customer ID: {self.CustomerID}\n" \
            f"First Name: {self.FirstName} Last Name: {self.LastName}"

pc = PhoneCustomer()
print(pc.MethodName())

# $ python PhoneCustomer.py 
# Day to send Bill: Monday Customer ID: 123
# First Name: David Last Name: Stevenson