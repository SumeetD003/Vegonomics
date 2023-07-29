import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Step 1: Prepare the Data
# Assume you have a dataset containing dish names, prices, and their corresponding labels
data = pd.read_csv('Dataset1.csv')
X = data[['NAMES', 'PRICE']]
y = data['CLASS']

# Step 2: Train the Machine Learning Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Step 3: Input Dish Details from User
new_dishes = []
dish_name = input("Enter the name of the dish (or 'done' to finish): ")

while dish_name != 'done':
    new_dishes.append(dish_name)
    dish_name = input("Enter the name of the dish (or 'done' to finish): ")

# Step 4: Calculate Bill Split
total_bill = float(input("Enter the total bill amount: $"))
num_diners = int(input("Enter the number of diners: "))

veg_subtotal = 0
non_veg_subtotal = 0

for dish_name in new_dishes:
    price = float(input(f"Enter the price for '{dish_name}': $"))

    # Predict the veg/non-veg category for the dish
    dish_data = pd.DataFrame({'dish_name': [dish_name], 'price': [price]})
    prediction = model.predict(dish_data)[0]

    # Calculate the subtotal based on veg/non-veg category
    if prediction == 1:
        non_veg_subtotal += price
    else:
        veg_subtotal += price

# Calculate the share per person for veg and non-veg items
veg_share = veg_subtotal / num_diners
non_veg_share = non_veg_subtotal / num_diners

# Calculate the total bill per person
total_per_person = total_bill / num_diners

# Print the results
print(f"Total Bill: ${total_bill}")
print(f"Veg Subtotal: ${veg_subtotal}")
print(f"Non-Veg Subtotal: ${non_veg_subtotal}")
print(f"Veg Share per Person: ${veg_share}")
print(f"Non-Veg Share per Person: ${non_veg_share}")
print(f"Total per Person: ${total_per_person}")
