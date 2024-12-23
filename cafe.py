class cafe:
    def __init__(self):
        self.menu = {
            "Tea":10,
            "coffee":15,
            "Veg Puff":15,
            "Egg puff":20,
            "Icecream":20
                    }

        self.order = []

    def display_menu(self):
        print("\nCafe Menu")
        for item , price in self.menu.items():
            print(f"{item}:{price:.2f}")

    def take_order(self):
        print("\nPlace order")
    
        self.display_menu()
        while True:
            choice = input("Enter the item (type 'done' to confirm order )").strip()
            if choice.lower() == "done":
           
                break
            elif choice in self.menu:
                self.order.append(choice)

            print(f"{choice} added to your order.")
        else:
            print("Choose from Menu ")
    def view_order(self):
        if not self.order:
            print("\nYour order is empty.")
        else:
            print("\nYour current order:")
            total = 0
            for order in self.order:
                price = self.menu[order]
                total += price  

            print(f"Total: {total:.1f}Rupees")
    def cancel_order(self):
        if not self.order:
            print("\nYour order is empty.")
            return

        self.view_order()
        item_to_remove = input("Enter the name of the item to remove: ").strip()
        if item_to_remove in self.order:
            self.order.remove(item_to_remove)
            print(f"{item_to_remove} has been removed from your order.")
        else:
            print(f"{item_to_remove} is not in your order.")

    def run(self):
            while True:
                print("\nWelcome to the Cafe!!")
                print("1. View Menu\n2. Place Order\n3. View Order\n4. Cancel Order\n5. Exit")
                choice = input("Choose an option: ").strip()

                if choice == "1":
                    self.display_menu()
                elif choice == "2":
                    self.take_order()
                elif choice == "3":
                    self.view_order()
                elif choice == "4":
                    self.cancel_order()
                elif choice == "5":
                    print("Thank you, visit again!!")
                    break
                else:
                    print("Invalid choice, Please try again.")
            
if __name__ == "__main__":
    shop = cafe()
    shop.run()