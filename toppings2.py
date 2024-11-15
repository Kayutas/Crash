requested_topings = ['extra cheese', 'mushrooms', 'extra cheese']

for requested_topping in requested_topings:
    if requested_topping == 'extra cheese':
        print("Sorry, we are out of extra cheese right now.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")