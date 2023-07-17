price = 10

while True:
    input_toping = input("Enter of pizza toppings ('quit' to stop): ")
    if input_toping.lower() == "quit":
        break
    else:
        price += 2.5
        print(f"Adding {input_toping} to your pizza!")

print(f"Your pizza costs {price} NIS.")
