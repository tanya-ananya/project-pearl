print("Welcome to Project Pearl!")

'''---------------------------------------INTRODUCTIONS--------------------------------------------'''
# Edit the intros for each respective topic, make sure the text are similar to each other

def show_main_intro(): # The follow lines of code will introduce the user to the first page
    print('Good afternoon, [user]. My name is Pearl! I’m an interactive chatbot where you can learn more about your health. ')
    print()
    print()

def show_general_intro(): # The follow lines of code will introduce the user to the general page
    gen_intro = '''
It's vital for women to be aware of how to show love to their bodies! To show love, we must understand 
how our bodies function to care for them in the best way possible. The following will allow you to choose 
a topic in which you are interested to learn about how you may care for your body, learn about different 
diseases that affect many women, and how you could improve your lifestyle!
'''


def show_mensPregn_intro(): # The follow lines of code will introduce the user to the mesnstrual page
    mensPregn_intro = '''
Menstruation and pregnancy bring unique physiological changes for many individuals, each phase marked by specific 
symptoms, needs, and considerations. From hormonal shifts affecting mood and energy levels in the menstrual cycle 
to dietary and emotional care during pregnancy, understanding these cycles helps manage health and well-being more 
effectively.
'''
    pass

def show_mental_health_intro(): # The follow lines of code will introduce the user to the mental health program
    mental_intro = '''
Each year, 1 in 5 women in the US has a mental health problem like depression, post-traumatic syndrome disorder, or an eating disorder. 
Many women can know something wrong is going on in their body while some are unaware which can lead to struggling with a diagnosed mental disorder. 
This section will go over some information that can help women with their mental health and some resources they can use!
'''

'''---------------------------------------MENUS FOR NAVIGATION------------------------------------'''
# Edit the many branches for each topic with numbers

def show_main_menu(): # The following lines of code will give the user options to the main page
    print("Please choose an option: (1-3 or Q)")
    print("1. General Health")
    print("2. Menstruation and Pregnancy")
    print("3. Mental Health")
    print("Q. Quit")

def show_general_menu(): # The following lines of code will give the user options to the main page
    print("Please choose an option:")
    print("1. Health Issues")
    print("2. Maintaining Well-Being")
    print("3. Little Things for Health Improvement")
    print("Q. Quit")

def show_health_issues_menu(): # The following lines of code will give the user options to the main page
    print("Please choose an option:")
    print("1. Heart Disease")
    print("2. Strokes")
    print("3. Diabetes")
    print("4. Urinary Tract Infections (UTI)")
    print("5. Human Papillomavirus (HPV)")
    print("6. Breast Cancer")
    print("7. Osteoporosis")
    print("Q. Quit")

def show_wellness_menu():
    get_well_info = '''
Focusing on well-being is essential for women to thrive in their daily lives. 
Key aspects like hydration, nutrition, sexual health, and exercise play vital roles 
in maintaining overall health, empowering women to enhance their quality of life and prevent 
various health issues.
   '''
    print("Please choose an option:")
    print("1. Hydration")
    print("2. Nutrition")
    print("3. Sexual Health")
    print("4. Exercise")
    print("Q. Quit")

def show_little_improvements():
    print("Please choose an option:")
    print("1. Every half-hour")
    print("2. Every few hours")
    print("3. Once a day")
    print("Q. Quit")

def show_mensPregn_menu(): # The following lines of code will give the user options to the main page
    print("Please choose an option:")
    print("1. Menstruation")
    print("2. Pregnancy")
    print("Q. Quit")

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
    print("1. Conditions")
    print("2. Management")
    print("3. Support")
    print("Q. Quit")

'''-----------------------------------------NAVIGATION BACKEND---------------------------------------'''
# Edit the choices for each number

def general():
    show_general_intro()
    while True:
        show_general_intro()
        show_general_menu()
        main_choice = input("Enter your choice (1-3): ")
        if main_choice == '1':
            while True:
                show_health_issues_menu()
                choice = input("Enter your choice (1-7): ")
                if choice == '1':
                    get_heart_info = '''
Heart disease is the leading cause of death for women, affecting over 40% of women in the U.S. Risk factors,
such as high blood pressure and cholesterol, become more common after menopause. Symptoms can include nausea, 
fatigue, and chest pressure, with common types including coronary artery disease, arrhythmia, and heart failure.
Treatments often involve medications, surgery for blockages, and lifestyle changes like improved diet and exercise. '''
                elif choice =='2':
                    print("Strokes: Women are more likely to die of strokes than men. Symptoms of a stroke may include numbness\n " +
                          "of the arms and legs, difficulty speaking, and face drooping. There are different types of strokes,\n " +
                          "such as hemorrhagic, which is bleeding in the brain, and ischemic, the blockage of blood vessels due to blood clots.")
                elif choice == '3':
                    print("Diabetes: Diabetes is a disease in which a person has high levels of blood glucose due to problems in\n " +
                          "the creation or usage of insulin.  Women who have diabetes have a much higher risk for heart disease.\n " +
                          "Symptoms of diabetes in women may include high blood sugar levels, which trigger the growth of fungus-causing\n " +
                          "yeast infections. Other symptoms may include urinary tract infections, polycystic ovary syndrome, fatigue, " +
                          "weight loss/gain, and more. Treatment may include insulation therapy and lifestyle changes.")
                elif choice =='4':
                    print("Urinary Tract Infections (UTIs):  UTIs occur when bacteria such as E. coli enter the urethra and begin to multiply." +
                          " Typical symptoms of a UTI are pain during urination and cloudy urine. UTIs may be treated with antibiotics, or they " +
                          "can go away on their own without medication. UTIs may also be caused by sexual activity, age, menopause, etc. ")
                elif choice == '5':
                    print("Human Papillomavirus (HPV): HPV is one of the most common sexually transmitted infections (STIs). HPV, unfortunately, " +
                          "has no cure. However, it may be prevented through a vaccine. Most people with HPV don’t realize that they have the STI " +
                          "because it has no symptoms. This is why it is recommended for women to have regular pap smear tests to see if there have " +
                          "been any changes in their cervix. HPV can cause genital warts or cervical cancer. ")
                elif choice == '6':
                    print("Breast Cancer: Breast cancer is the most common cancer in women in the United States. Women have around a 13% chance of " +
                          "developing breast cancer during their lifetime. It is recommended for women to have yearly scheduled mammograms beginning " +
                          "at the age of 40. ")
                elif choice == '7':
                    print("Osteoporosis: This disease causes the weakening of the bones. Women are actually at a higher risk of developing osteoporosis " +
                          "and are at a much higher risk post-menopause. Treatment may include increasing calcium intake, physical activity, and " +
                          "avoiding the use of alcohol. ")
                elif choice == 'Q' or choice == 'q':
                    print("Thank you for using the tool! Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and #.")

        elif main_choice == '2':
            while True:
                show_wellness_menu()
                choice = input("Enter your choice (1-4): ")
                if choice == '1':
                    print("Hydration: Our bodies are made of 60% water. Not consuming enough water may lead to dehydration, causing dizziness, confusion, " +
                          "and seizures. The amount of water one needs depends on one’s size, how much daily activity a person receives, the weather, etc. " +
                          "It is suggested that women drink around 9 cups of water a day. Staying hydrated allows the removal of waste from your body through " +
                          "urine, stool, and sweat. It also keeps the body at a normal temperature, protects delicate tissues, keeps the joints cushioned and " +
                          "lubricated, and keeps the skin healthy and plump. ")
                elif choice == '2':
                    print("Nutrition: It is important to provide the body with the nutrients it needs. Receiving the proper nutrients needed impacts the " +
                          "body’s energy levels and immune system and prevents disease. It is recommended that everyone consumes a variety of foods from the " +
                          "5 food groups, which are grain foods, vegetables, fruit, protein, and dairy. Important nutrients women need are calcium, iron, " +
                          "protein, vitamin D, omega-3, etc. ")
                elif choice == '3':
                    print("Sexual Health: It is important to understand sexually transmitted diseases (STIs), contraceptives, and safe sex practices to " +
                          "maintain a healthy sex life. STIs may be prevented by the usage of vaccines or by practicing safe sexual activity. " +
                          "When practicing safe sex, people may use condoms and dental dams to prevent contact with bodily fluids. It is recommended " +
                          "that women begin receiving pap smears starting at the age of 21 in order to see if there are any changes in the cervix.")
                elif choice == '4':
                    print("Exercise: Maintaining a healthy lifestyle also includes being physically active. Different workout routines may be different " +
                          "for all ages. For example, a woman may need physical activity when often to prevent the weakening of muscles, heart disease, " +
                          "and pain of arthritis. For women with diabetes, it may be harder to stay active. However, benefits include lowering the risk of " +
                          "heart disease, huge build pressure, and reducing anxiety and depression.")
                elif choice == 'Q' or choice == 'q':
                    print("Thank you for using the tool! Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and #.")
        elif main_choice == '3':
            while True:
                show_little_improvements()
                choice = input("Enter your choice (1-3): ")
                if choice == '1':
                    print("Every half-hour: Every 30 minutes, it is recommended to have a short break and do the following: get up and move and drink water." +
                          " Sitting down for longer periods of time may lead to an increased risk of obesity, diabetes, cancer, heart disease, and early death." +
                          " So, dance, jump, stretch, or walk around your chair! To keep your body functioning, you must stay hydrated. It’s not necessary to " +
                          "drink a whole cup of water in one sitting. All you need is an ounce or two every 30 minutes. You don’t have to restrict yourself " +
                          "to these two options. There are many more things you can do! ")
                elif choice == '2':
                    print("Every few hours: Every few hours, you should relax! Schedule a break in between tasks so you can destress. During these breaks, " +
                          "take in the scenery around you. Practice mindfulness by focusing on your current environment. You may go outside on a walk and " +
                          "observe the sounds, the smells, and how everything may affect how you feel now. Another way to use your break is to remove yourself " +
                          "from the screens! While looking at our phones, computers, and TVs, we don’t blink as much because we stare at our screens. " +
                          "This causes dryness in the eyes, so close your eyes, read a book, or sit and listen to music!")
                elif choice == '3':
                    print("Once a day: Take the time out of your day to learn something new. When learning new things, our synapses (brain cell connections) " +
                          "strengthen and create new ones. In doing so, our minds stay sharp and running. We lose synapses as we age, so the more you learn, " +
                          "the better shape your brain will be! Another way to engage our brains is to create social connections. Whenever we have meaningful " +
                          "interactions with others, our synapses increase, moods are boosted, and loneliness is reduced. So, talk to a friend, a family " +
                          "member, or even a stranger! If you feel that you need to relax, you can always try meditation. Whenever our bodies are stressed, it " +
                          "triggers a multitude of physiological changes which prepare us for “fight or flight.” Being constantly stressed may cause high blood " +
                          "pressure, high blood sugar, and much more. To unwind, take some deep breaths, do yoga, or meditate.  ")
                elif choice == 'Q' or choice == 'q':
                    print("Thank you for using the tool! Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and #.")

        elif choice == 'Q' or choice == 'q':
            print("Thank you for using the tool! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and #.")

def mensPregn():
    show_mensPregn_intro()
    while True:
        show_mensPregn_menu()
        main_choice = input("Enter your choice (1-2): ")
        if main_choice == '1':
            while True:
                show_menstrual_menu()
                choice = input("Enter your choice (1-4): ")
                if choice == '1':
                    print("\033[1mCycle and Timing:\033[0m")
                    print("A typical menstrual cycle lasts between 21 to 35 days with\n"+
                          "menstruation itself (the period) typically spanning 3 to 7 days.\n"+
                          "This cycle includes four stages: menstruation, follicular phase, ovulation,\n"+
                          "and luteal phase, each governed by hormones that prepare the body for a potential\n"
                          "pregnancy. The cycle can change with age and factors like stress and lifestyle.")
                    print("\033[1mSources: Cleveland Clinic, 2024  & Nuffield Health 2024\033[0m")
                    pass
                elif choice == '2':
                    print("\033[1mSymptoms:\033[0m")
                    print("Common symptoms during menstruation include cramps, mood changes, and bloating. Some\n"
                          "people also experience headaches or fatigue due to hormonal shifts.Period symptoms and\n"
                          "severity can vary, especially for teens and those nearing menopause, when cycles may \n"
                          "become less predictable.")
                    print("\033[1mSources: Flo Health, 2024 &  mindbodygreen 2024\033[0m")
                    pass
                elif choice == '3':
                    print("\033[1mNutrition and Exercises:\033[0m")
                    print("Diet and exercise impact the menstrual cycle. Foods rich in iron and nutrients, along\n"
                          "with light activities like yoga, can help alleviate discomfort. High-intensity exercise\n"
                          "may be better timed during specific phases, such as the follicular phase when energy levels\n"
                          "are higher.")
                    print("\033[1mSources: mindbodygreen, 2024 & Cleveland Clinic 2024\033[0m")
                    pass
                elif choice == '4':
                    print("\033[1mSex Life:\033[0m")
                    print("Hormonal changes throughout the cycle influence libido, often increasing\n"+
                          "during ovulation. Communication with healthcare providers can be helpful if there are\n"+
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
                    print("\033[1mBirth Control and Pregnancy Planning:\033[0m")
                    print("Birth control helps prevent pregnancy, with different options like hormonal pills and\n"
                          "IUDs. When stopping birth control, it may take some time for regular cycles to resume,\n"
                          "depending on the type.")
                    print("\033[1mSources: Flo Health, 2024\033[0m")
                    pass
                elif choice == '2':
                    print("\033[1mNutrition and Food Aversions:\033[0m")
                    print("Eating a balanced diet is essential during pregnancy,with special emphasis on folate,\n"
                          "iron, and protein. Many experience food aversions due to heightened senses, particularly\n"
                          "in early pregnancy.")
                    print("\033[1mSources: Nuffield Health, 2024\033[0m")
                    pass
                elif choice == '3':
                    print("\033[1mExercise and Health:\033[0m")
                    print("Exercises such as walking, swimming, and prenatal yoga can improve mental health and ease\n"
                          "labor preparation. However, high-impact activities are often discouraged. Always consult \n"
                          "with a healthcare provider for personalized recommendations.")
                    print("\033[1mSources: Cleveland Clinic, 2024\033[0m")
                    pass
                elif choice == '4':
                    print("\033[1mAnxiety and Emotional Health:\033[0m")
                    print("Hormonal changes can heighten anxiety, making support systems and mindfulness practices\n"
                          "beneficial. Severe anxiety should be discussed with a healthcare provider to explore\n"
                          "options that are safe for both parent and child.")
                    print("\033[1mSources: Flo Health, 2024\033[0m")
                    pass
                elif choice == '5':
                    print("\033[1mPregnancy Milestones and Self-Care:\033[0m")
                    print("Prenatal vitamins, morning sickness management, weight control, and skin care (for stretch marks)\n"
                          "are key aspects. Common milestones include feeling fetal movement by weeks 18-20 and preparing a \n"
                          "birth plan. After childbirth, post-partum recovery focuses on sleep and regaining strength, which \n"
                          "can include physical and emotional support.")
                    print("\033[1mSources: Nuffield Health, 2024 & Cleveland Clinic 2024\033[0m")
                    pass
                elif choice == 'Q' or choice == 'q':
                    print("Thank you for using the tool! Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and #.")
        elif main_choice == 'Q' or main_choice == 'q':
            print("Thank you for using the tool! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and #.")

def mental_health():
    show_mental_health_intro()
    while True:
        show_mental_health_menu()
        choice = input("Enter your choice (1-3 or Q to quit): ")

        if choice == '1':
            display_mental_conditions()
        elif choice == '2':
            display_management_tips()
        elif choice == '3':
            display_support_resources()
        elif choice.lower() == 'q':
            print("Thank you for using the tool! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3 or Q to quit.")

# Separate function for mental health conditions
def display_mental_conditions():
    print('''\nConditions: In the past year, women were almost twice as likely than men to have symptoms of depression.
They are more likely to have an anxiety disorder, including post-traumatic stress disorder (PTSD), panic disorder, or 
obsessive-compulsive disorder (OCD). When women experience significant stress, their bodies increase the release of a hormone 
called cortisol, which can lead to overeating and encourage the body to store fat. Mental health issues such as anxiety, stress, 
and depression can impact women's health, affecting heart conditions, headaches and migraines, menstrual cycle disruption, 
increased levels of obesity, and decreased sex drive.\n''')

# Separate function for management tips
def display_management_tips():
    print('''\nManagement: Improving mental health can often start with sleep and diet. Insomnia linked to depression 
can negatively affect mood and energy levels. Establishing a regular sleep schedule can help alleviate symptoms of anxiety 
and depression while allowing the body to rest, regulate, and maintain a strong immune system. Physical activity, like walking 
or dancing, can boost mood, reduce depression symptoms, build strength, and improve endurance. A balanced diet can also help 
stabilize mood. Processed foods, caffeine, and alcohol may disrupt sleep and irritate mood. Specifically, processed foods can 
cause inflammation throughout the body and brain, potentially contributing to mood disorders like anxiety and depression. Aim 
to include fruits, vegetables, and omega-3 fatty acids (from sources like salmon, walnuts, and kidney beans).

Other stress management tips:
    - Write your thoughts down
    - Meditate
    - Take deep breaths
    - Stretch
    - Dedicate time for self-care
    - Seek professional help (listed in the support section)\n''')

# Separate function for support resources
def display_support_resources():
    print('''\nSupport: Here are professional support numbers that may be helpful to women and others:

In Georgia:
- Emory's Women's Mental Health Program
- Georgia Crisis & Access Line: 1(800) 715-4225

Nationwide Hotlines:
- National Domestic Violence: 1(800) 799-SAFE
- National Sexual Assault: 1(800) 656-HOPE
- Disaster Distress Helpline: 1(800) 985-5990 or text “TalkWithUs” to 66746
- Depression and Bipolar Support Alliance: 1-800-826-3632
- National Suicide Prevention Lifeline: Call or Text 988
- Postpartum Support International: 1-800-944-4PPD (4773)
- PPD Moms: 1-800-PPD-MOMS (800-773-6667)
- S.A.F.E. ALTERNATIVES®: 1-800-DONTCUT (800-366-8288)\n''')



def main():
    show_main_intro()
    show_main_menu()
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            general()
        elif choice == '2':
            mensPregn()
        elif choice == '3':
            mental_health()
        elif choice == 'Q' or choice == 'q':
            print("Thank you for using the tool! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

'''------------------------------------------MAIN CONTENT------------------------------------------'''
# Type the main content of your topic using print statements

def show_general():
    pass

def show_mensPreg():
    pass

def show_mental_health():
    pass


# Do not edit this
if __name__ == "__main__":
    main()