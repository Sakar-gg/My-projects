# 1. A Terminal-Based Shopping Cart

#         This shifts your focus onto managing data structures, which is exactly how a backend handles an e-commerce checkout system.
#         Concepts practiced: Lists, Dictionaries, for loops, and string formatting.

#         The Logic:

#             Create a dictionary representing available items and their prices: {"apple": 0.99, "bread": 2.50, "milk": 3.00}.
#             Run a while loop that keeps asking the user to 1. View Items, 2. Add to Cart, 3. View Cart & Total, or 4. Checkout.
#             When they view the cart, use a for loop to iterate through their items, calculate the running total, and print it nicely.




# Setting up initial Data

store_items = {
    "apple": 0.99,
    "bread": 2.50,
    "milk": 3.00,
    "eggs": 2.00,
    "cheese": 4.00
}


# Shopping cart as a list of item names
shopping_cart = []

print("Welcome to my terminal based shopping cart")
print("--------------------------------------------")


running = True
    while running:
        print()
        print("What would you like to do?")
        print("1. View Items")
        print("2. Add to Cart")
        print("3. View Cart & Total")
        print("4. Checkout")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\nAvailable Items:")
            for item, price in store_items.items():
                print(f"{item.capitalize()}: ${price:.2f}")

        elif choice == "2":
            print("\nAdd to Cart:")
            item_to_add = input("Enter the item you want to add: ").strip().lower()

            if item_to_add in store_items:
                shopping_cart.append(item_to_add)
                print(f"Added {item_to_add} to your cart.")
            else:
                print(f"Sorry, {item_to_add} is not available in the store. Please check if there is a spelling error.")

        elif choice == "3":
            print("\nYour Cart:")

            if len(shopping_cart) == 0:
                print("Your cart is empty.")
            else:
                total_cost = 0
                for item in shopping_cart:
                    price = store_items[item]
                    total_cost += price
                    print(f"{item.capitalize()}: ${price:.2f}")
                print(f"\nTotal items in cart: {len(shopping_cart)}")
                print(f"Total Cost: ${total_cost:.2f}")

        elif choice == "4":
            print("\nCheckout:")
            if len(shopping_cart) == 0:
                print("Thanks for stopping by! Your cart is empty.")
            else:
                final_total = 0.00
                for item in shopping_cart:
                    final_total += store_items[item]
                print(f"Your final total is: ${final_total:.2f}")
                print("Thank you for shopping with us!")
running = False

    else
        print("Invalid choice. Please enter a number between 1 and 4.")

