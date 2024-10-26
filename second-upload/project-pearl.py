# Add your program code here.
print("Welcome to Project Pearl!")

'''---------------------------------------INTRODUCTIONS--------------------------------------------'''
# Edit the intros for each respective topic, make sure the text are similar to each other

def show_main_intro(): # The follow lines of code will introduce the user to the first page
   pass

def show_general_intro(): # The follow lines of code will introduce the user to the general page
   pass

def show_menstrual_intro(): # The follow lines of code will introduce the user to the mesnstrual page
   pass

def show_mental_health_intro(): # The follow lines of code will introduce the user to the mental health program
   pass

'''---------------------------------------MENUS FOR NAVIGATION------------------------------------'''
# Edit the many branches for each topic with numbers

def show_main_menu(): # The following lines of code will give the user options to the main page
   print("Please choose an option:")
   print("1. choice 1")
   print("2. choice 2")
   print("3. choice 3")
   print("4. Bibliography")
   print("Q. Quit")

def show_general_menu(): # The following lines of code will give the user options to the main page
   print("Please choose an option:")
   print("1. choice 1")
   print("Q. Quit")

def show_menstrual_menu(): # The following lines of code will give the user options to the main page
   print("Please choose an option:")
   print("1. choice 1")
   print("Q. Quit")

def show_mental_health_menu(): # The following lines of code will give the user options to the main page
   print("Please choose an option:")
   print("1. choice 1")
   print("Q. Quit")

'''-----------------------------------------NAVIGATION BACKEND---------------------------------------'''
# Edit the choices for each number

def main():
   show_main_intro()
   while True:
      show_main_menu()
      choice = input("Enter your choice (1-4): ")
      if choice == '1':
         show_general_menu()
      elif choice == '2':
         show_menstrual_menu()
      elif choice == '3':
         show_mental_health_menu()
      elif choice == '3':
         show_biblography()
      elif choice == 'Q' or choice == 'q':
         print("Thank you for using the tool! Goodbye!")
         break
      else:
         print("Invalid choice. Please enter a number between 1 and 4.")

def general():
   show_general_intro()
   while True:
      show_general_menu()
      choice = input("Enter your choice (1-#): ")
      if choice == '1':
         pass # Write the function for choice 1
      elif choice == 'Q' or choice == 'q':
         print("Thank you for using the tool! Goodbye!")
         break
      else:
         print("Invalid choice. Please enter a number between 1 and #.")

def menstrual():
   show_menstrual_intro()
   while True:
      show_menstrual_menu()
      choice = input("Enter your choice (1-#): ")
      if choice == '1':
         pass # Write the function for choice 1
      elif choice == 'Q' or choice == 'q':
         print("Thank you for using the tool! Goodbye!")
         break
      else:
         print("Invalid choice. Please enter a number between 1 and #.")

def mental_health():
   show_mental_health_intro()
   while True:
      show_mental_health_menu()
      choice = input("Enter your choice (1-#): ")
      if choice == '1':
         pass # Write the function for choice 1
      elif choice == 'Q' or choice == 'q':
         print("Thank you for using the tool! Goodbye!")
         break
      else:
         print("Invalid choice. Please enter a number between 1 and #.")

'''------------------------------------------MAIN CONTENT------------------------------------------'''
# Type the main content of your topic using print statements

def show_general(): 
   pass

def show_menstrual():
   pass

def show_mental_health():
   pass

def show_bibliography():
   pass


# Do not edit this
if __name__ == "__main__":
    main()