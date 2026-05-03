"""
Mini Project: Simple Console Based Calculator

Features:
- Class based calculator
- Basic Operations
- Loop for repeated use
- History stored in a list
- Save and load history using a text file
- Simple error handling
"""

HISTORY_FILE =  "calc_history.txt"

class Calculator:
    
    def __init__(self):
        pass

    def load_history(self):
        pass

    def save_history(self):
        pass

    def get_number(self):
        pass

    def add(self, a, b):
        return a + b
    
    def sub(self,a ,b):
        return a - b
    
    def mult(self, a ,b):
        return a * b
    
    def div(self, a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Cannot be divided by zero")
            return None
        
    def calculate(self):
        pass

    def show_history(self):
        pass

    def main():
        calc = Calculator()

        while True:
            print("\nSimple Calculator")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiplication")
            print("4.Division")
            print("5.Show History")
            print("6.Exit")

            choice = input("Choose an  option : ")

            if choice in ['1','2','3,','4']:
                calc.calculate(choice)
            elif choice=='5':
                calc.show_history()
            elif choice =='6':
                calc.save_history()
                print("Goodbye, History saved.")
            else:
                print("Invalid choice. Try again.")

    if __name__ == "main":
        main()