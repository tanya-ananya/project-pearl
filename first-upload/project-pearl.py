# Add your program code here.
print("Welcome to Project Pearl!")

# Check and print column names
print("Column names in the dataset:")

def show_intro(): # The follow lines of code will introduce the user to the program
   pass

def show_menu(): # The following lines of code will give the user options
   print("Please choose an option:")
   print("1. choice 1")
   print("2. choice 2")
   print("3. choice 3")
   print("4. Bibliography")
   print("5. Quit")

def show_general(): 
   pass

def show_menstrual():
   pass

def show_mental_health():
   pass

def show_bibliography():
   pass

def main():
   show_intro()
   while True:
      show_menu()
      choice = input("Enter your choice (1-4): ")
      if choice == '1':
         show_general()
      elif choice == '2':
         show_menstrual()
      elif choice == '3':
         show_mental_health()
      elif choice == '3':
         show_biblography()
      elif choice == '5':
         print("Thank you for using the tool! Goodbye!")
         break
      else:
         print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()