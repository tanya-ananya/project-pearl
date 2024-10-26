# Add your program code here.
print("Welcome to Project Pearl!")

'''---------------------------------------INTRODUCTIONS--------------------------------------------'''
# Edit the intros for each respective topic, make sure the text are similar to each other

def show_main_intro(): # The follow lines of code will introduce the user to the first page
   pass

def show_general_intro(): # The follow lines of code will introduce the user to the general page
   pass

def show_mensPregn_intro(): # The follow lines of code will introduce the user to the mesnstrual page
   pass

def show_mental_health_intro(): # The follow lines of code will introduce the user to the mental health program
   pass

'''---------------------------------------MENUS FOR NAVIGATION------------------------------------'''
# Edit the many branches for each topic with numbers

def show_main_menu(): # The following lines of code will give the user options to the main page
   print("Please choose an option:")
   print("1. choice 1")
   print("2. Menstruation and Pregnancy")
   print("3. choice 3")
   print("4. Bibliography")
   print("Q. Quit")

def show_general_menu(): # The following lines of code will give the user options to the main page
   print("Please choose an option:")
   print("1. choice 1")
   print("Q. Quit")

def show_mensPregn_menu(): # The following lines of code will give the user options to the main page
   print("Please choose an option:")
   print("1. Menstruation")
   print("2. Pregnancy")

def show_menstrual_menu(): # The following lines of code will give the user options to the mentrual topics options
   print("1. Cycle and Timing")
   print("2. Symptoms")
   print("3. Nutrition and Exercise")
   print("4. Sex Life")
   print("Q. Quit")

def show_pregnancy_menu(): # The following lines of code will give the user options to the pregnancy topics options
   print("1. Birth Control and Pregnancy Planning")
   print("2. Nutrition and Food Aversions")
   print("3. Exercise and Health")
   print("4. Anxiety and Emotional Health")
   print("5. Pregnancy Milestones and Self-Care")
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
         show_mensPregn_menu()
      elif choice == '3':
         show_mental_health_menu()
      elif choice == '3':
         show_biblography()
      elif choice == 'Q' or choice == 'q':
         print("Thank you for using the tool! Goodbye!")
         break
      else:
         print("Invalid choice. Please enter a number between 1 and 4.")
print()

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

def mensPregn():
   show_mensPreg_intro()
   print()
   while True:
      show_mensPregn_menu()
      main_choice = input("Enter your choice (1-2): ")
      if main_choice == '1':
         while True:
            show_menstruation_menu()
            choice = input("Enter your choice (1-4): ")
            if choice == '1':
               print("Cycle and Timing: A typical menstrual cycle lasts between 21 to 35 days,"+ 
               "with menstruation itself (the period) typically spanning 3 to 7 days. This cycle"+
               "includes four stages: menstruation, follicular phase, ovulation, and luteal phase,"+
               "each governed by hormones that prepare the body for a potential pregnancy. The"+ 
               "cycle can change with age and factors like stress and lifestyle.")
               print("\033[1mSources: Cleveland Clinic, 2024  & Nuffield Health 2024\033[0m")
               pass
            elif choice == '2':
               print("2. Symptoms: Common symptoms during menstruation include cramps, mood changes,"+
               "and bloating. Some people also experience headaches or fatigue due to hormonal shifts."+
               "Period symptoms and severity can vary, especially for teens and those nearing menopause,"+
               "when cycles may become less predictable.")
               print("\033[1mSources: Flo Health, 2024 &  mindbodygreen 2024\033[0m")
               pass
            elif choice == '3':
               print("3. Nutrition and Exercise: Diet and exercise impact the menstrual cycle. Foods"+ 
               "rich in iron and nutrients, along with light activities like yoga, can help alleviate"+
               "discomfort. High-intensity exercise may be better timed during specific phases, such"+ 
               "as the follicular phase when energy levels are higher.")
               print("\033[1mSources: mindbodygreen, 2024 & Cleveland Clinic 2024\033[0m")
               pass
            elif choice == '4':
               print("4. Sex Life: Hormonal changes throughout the cycle influence libido, often increasing"+
               "during ovulation. Communication with healthcare providers can be helpful if there are"+
               "questions about timing or changes in libido related to the cycle.")
               print("\033[1mSources: mindbodygreen, 2024 & Cleveland Clinic 2024\033[0m")
               pass # Write the function for choice 1
            elif choice == 'Q' or choice == 'q':
               print("Thank you for using the tool! Goodbye!")
               break
            else:
               print("Invalid choice. Please enter a number between 1 and #.")
      elif main_choice == '2':
         while True:
            show_pregnancy_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
               print("1. Birth Control and Pregnancy Planning: Birth control helps prevent pregnancy, with"+
               "different options like hormonal pills and IUDs. When stopping birth control, it may take"+
               "some time for regular cycles to resume, depending on the type.")
               print("\033[1mSources: Flo Health, 2024\033[0m")
               pass
            elif choice == '2':
               print("2. Nutrition and Food Aversions: Eating a balanced diet is essential during pregnancy,"+
               "with special emphasis on folate, iron, and protein. Many experience food aversions due to"+
               "heightened senses, particularly in early pregnancy.")
               print("\033[1mSources: Nuffield Health, 2024\033[0m")
               pass
            elif choice == '3':
               print("3. Exercise and Health: Exercises such as walking, swimming, and prenatal yoga can"+
               "improve mental health and ease labor preparation. However, high-impact activities are often"+
               "discouraged. Always consult with a healthcare provider for personalized recommendations.")
               print("\033[1mSources: Cleveland Clinic, 2024\033[0m")
               pass
            elif choice == '4':
               print("4. Anxiety and Emotional Health: Hormonal changes can heighten anxiety, making "+
               "support systems and mindfulness practices beneficial. Severe anxiety should be discussed"+
               "with a healthcare provider to explore options that are safe for both parent and child.")
               print("\033[1mSources: Flo Health, 2024\033[0m")
               pass
            elif choice == '5':
               print("5. Pregnancy Milestones and Self-Care: Prenatal vitamins, morning sickness management,"+
               "weight control, and skin care (for stretch marks) are key aspects. Common milestones include"+
               "feeling fetal movement by weeks 18-20 and preparing a birth plan. After childbirth,"+
               "post-partum recovery focuses on sleep and regaining strength, which can include physical "+
               "and emotional support.")
               print("\033[1mSources: Nuffield Health, 2024 & Cleveland Clinic 2024\033[0m")
               pass
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

def show_mensPreg():
   pass

def show_mental_health():
   pass

def show_bibliography():
   pass


# Do not edit this
if __name__ == "__main__":
    main()