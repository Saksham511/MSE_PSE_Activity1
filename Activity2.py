hours_worked = int(input("Enter how many hours you worked:"))
hourly_pay_rate = int(input("Enter the hourly pay rate:"))

gross_pay = hours_worked * hourly_pay_rate

if gross_pay > 0 and gross_pay <= 15600:
    tax_rate = 10.5
elif gross_pay >= 15601 and gross_pay <=53500:
    tax_rate = 17.5
elif gross_pay >= 53501 and gross_pay <= 78100:
    tax_rate = 30
elif gross_pay >= 78101 and gross_pay <= 180000:
    tax_rate = 33
elif gross_pay >+ 180001:
    tax_rate = 39
else:
    print ("Enter valid number: ")

after_tax = gross_pay-(gross_pay*tax_rate/100)
print("Your gross income is", gross_pay)
print("Your net income after tax deduction is", after_tax)
