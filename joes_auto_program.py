import joes_auto_classes as j


#CUSTOMER 
name = "John Doe"      
address = "123 Main St. Waco TX 76706"     
phone = "214-555-1112"

#CAR
make = "Honda"
model = "Accord LX"    
year = 2016

#SERVICE QUOTE
pcharge = 1210.5
lcharge = 765.00

#CREATE INSTANCES
customer = j.Customer(name, address, phone)
car = j.Car(make, model, year)
service_quote = j.ServiceQuote(pcharge, lcharge)

#PRINT
print(f"Customer: {customer.get_name()}\tAddress: {customer.get_address()}\tPhone: {customer.get_phone()}")
print(f"Make: {car.get_make()}\tModel: {car.get_model()}\tYear: {car.get_year()}")
print("Sevice Quote")
print("Parts:","$"+ str(format(service_quote.get_parts_charges(), ",.2f")))
print("Labor:", "$"+ str( format(service_quote.get_labor_charges(), ",.2f")))
print("Sales Tax:",  "$"+ str(format(service_quote.get_sales_tax(), ",.2f")))
print("Total Charges:", "$"+ str( format(service_quote.get_total_charges(), ",.2f")))