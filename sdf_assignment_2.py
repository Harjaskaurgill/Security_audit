"""
Description: My second assignment
Author: Harjas kaur gill
Date: 21-09-2024
"""
# Ready for peer review

#SIMPLE DATA TYPES
first_name = "Harjas"
print(f"value: {first_name} type: {type(first_name)}")

has_valid_license = "True"
print(f"value: {has_valid_license} type:{type(has_valid_license)}")

current_year = 2024
print(f"this year: {current_year} type: {type(current_year)}")

next_year = current_year + 1
print(f"next year: {next_year} type: {type(next_year)}")

#CALCULATIONS

GST_RATE = 0.05

MANITOBA_PST_RATE = 0.07

vehicle_purchase_price = 65000.00

GST_for_the_vehicle = vehicle_purchase_price * GST_RATE
PST_for_the_vehicle = vehicle_purchase_price * MANITOBA_PST_RATE

final_cost_of_the_vehicle = vehicle_purchase_price + GST_for_the_vehicle + PST_for_the_vehicle

print(final_cost_of_the_vehicle)

print(f"pre-tax value: {vehicle_purchase_price}. "
      f"Provincial Tax: {PST_for_the_vehicle}."
      f"Federal Tax: {GST_for_the_vehicle}."
      f"Total: {final_cost_of_the_vehicle}.")

print(f"Pre-tax value: ${vehicle_purchase_price:,.2f}. "
      f"Provincial Tax: ${PST_for_the_vehicle:,.2f}."
      f"Federal Tax: ${GST_for_the_vehicle:,.2f}."
      f"Total: ${final_cost_of_the_vehicle:,.2f}.")

#LISTS
#Declare a variable storing the list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

# Verify the list has been created by printing its datatype
print("Data type:", type(numbers))

print("list:",numbers)

# Add first name to list between the value of 5 and 6
numbers.insert(5, "Harjas")

print("list with name:", numbers)

# Remove number 9
numbers.remove(9)

print("list without 9:", numbers)

# Declare a variable that stores a second list
letters = ["A","B","C"]

# Declare a variable that stores a third list
combined_list = numbers + letters

print("combined list:", combined_list)

#TUPLES

# Declare a variable that stores a tuple
canadian_provinces = ("Manitoba", "Alberta", "Ontario", "Nova Scotia")

print("data type:", type(canadian_provinces))

print("tuples:", canadian_provinces)

#DICTIONARIES

# Declare a variable to store a dictionary
canadian_currency = {
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

print("data type:", type(canadian_currency))

print("dictionary:",canadian_currency )

# Modify the values to use as whole numbers

canadian_currency = {coin: int(value * 100) for coin, value in canadian_currency.items()}

print("dictionary:",canadian_currency)

# Add Loonie and Toonie to the dictionary

canadian_currency.update({"loonie":100, "toonie":200})

print("dictionary:",canadian_currency)

#SETS

# Declare a variable to store a set

even_numbers = {2,4,6,8,10,12,14,16,18,20}

print("data type:",type(even_numbers))

print("set:",even_numbers)

#Declare a variable to store second set

multiples_of_5 = {5,10,15,20}

print("set:",multiples_of_5)

# Declare a variable to store a third set

union = even_numbers.union(multiples_of_5)

print(union)

# Declare a variable to store a fourth set

intersect = even_numbers.intersection(multiples_of_5)

print(intersect)

# Declare a variable to store a fifth set

difference = even_numbers.difference(multiples_of_5)

print(difference)

# Declare a variable to store a sixth set

difference = multiples_of_5.difference(even_numbers)

print(difference)



