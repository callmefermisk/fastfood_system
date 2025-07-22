def _choice(option_list: list):
    try:
        choice_num = int(input("Enter the number of the choice: ")) + 1
        if 0 < choice_num < len(option_list) + 1:
            return option_list[choice_num - 1]
        else:
            return "invalid choice"
    except ValueError:
        return "invalid choice"


class Data:

    def __init__(self):
        self.__foods = {
            "burger": "100",
            "sandwich": "70",
            "taco": "90"
        }

    def show_price(self):
        print("Available foods:")
        for i, (food, price) in enumerate(self.__foods.items()):
            print(f"{i + 1} - {food} ${price}")

        food_names = list(self.__foods.keys())
        choice = _choice(food_names)
        print(f"Your choice is: {choice}")  # Fixed: was 'price'
        if choice != "invalid choice":
            self._pay_the_value(choice)

    def _pay_the_value(self, item):
        value = self.__foods.get(item)
        if value:
            print(f"You should pay this value: ${value}")
            choice_to_pay = input("Would you like to proceed with payment? (yes/no): ")
            if choice_to_pay.lower() in ("yes", "y"):
                self._to_pay(value)  # Fixed: was calling _pay_the_value again
            else:
                print("Payment Cancelled")
        else:
            print("Item not found!")

    def _to_pay(self, value):
        way_to_pay = input("""
How would you like to pay:
1 - by credit card
2 - cash
Enter your choice: """)
        if way_to_pay in ("1", "2"):
            if way_to_pay == "1":
                self._pay_with_credit_card(value)  # Fixed: was _credit_cart
            else:
                self._pay_with_cash(value)
        else:
            print("Invalid payment method!")
            return self._to_pay(value)  # Ask again

    def _pay_with_credit_card(self, value):
        print(f"Processing credit card payment of ${value}...")
        print("Payment successful!")

    def _pay_with_cash(self, value):
        print(f"Please prepare ${value} in cash.")
        print("Payment received!")

