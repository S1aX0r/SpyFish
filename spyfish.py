#SpyFish.py made by Sl4x0r
#A osint & phishing tool written in python

def print_logo():
    logo = '''
 SSSS  PPPP   Y   Y  FFFFF  III  SSSS  H   H
 S     P   P   Y Y   F      I   S     H   H
  SSS  PPPP     Y    FFFF   I   SSS   HHHHH
     S P        Y    F      I     S  H   H
 SSSS  P        Y    F     III  SSSS  H   H
    '''
    print(logo)


# Call the function to display the logo

def google_dork_suggestions(name, email, phone, address):
    # Google Dork query suggestions based on provided information

    suggestions = []

    # Search suggestions for person
    if name:
        suggestions.append(f'Find "intitle:{name}"')
    if email:
        suggestions.append(f'Find "intext:{email}"')
    if phone:
        suggestions.append(f'Find "intext:{phone}"')
    if address:
        suggestions.append(f'Find "intext:{address}"')

    # More advanced dork suggestions
    suggestions.append(f'Search for exposed files with filetype:xls "password" site:dropbox.com')
    suggestions.append(f'Look for login pages with "intitle:login inurl:admin"')

    # Combine all suggestions into a list for user display
    print("\nInsert into Google search engine")
    return suggestions

def main():
    print_logo()

    # Awaiting hacker name (username)
    hacker_name = input('Welcome to SpyFish! \nWho will be using this program today? \n')

    print(f"\nWelcome {hacker_name}\n")
    options = input(f"\nIt's good to see you {hacker_name}. What will we be doing today?\nrecon, phishing? \n")
    if options == "recon":
        osint_options = input("\nAre you targeting a person or corporation? \n")
        if osint_options == "person" or osint_options == "corporation":
            print("\nPlease supply the following separated by a comma then a space:\nName\nEmail\nAddress\nPhone Number\n")
            info = input("")
            
            name, email, phone, address = [item.strip() for item in info.split(",")]

            # Generate and print Google Dork suggestions
            suggestions = google_dork_suggestions(name, email, phone, address)
            
            print("\nSuggested Google Dork Queries:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
    #Creating phishing option
    elif options == "phishing":
            phishing_options = input("\nWill you be targeting a corporation or a person?\n")
            if phishing_options == "person" or phishing_options == "corporation":
                print("\nType 'more options' for available platforms to attack\n")
                options = input("")
                if options == ("more options"):
                    print("\nAvailable platforms are: Instagram, FaceBook, PayPal, Venmo, or Gmail\n")
                    print("\nWhich would you like to target?\n")
                    choice = input("")
                    if choice == "instagram" or choice == "Instagram" or choice == "facebook" or choice == "FaceBook" or choice == "paypal" or choice == "PayPal" or choice == "venmo" or choice == "Venmo" or choice == "gmail" or choice == "Gmail":
                        print("\nCreating phishing template....\n")
                        print("Hi (customer name),\n \nWe detected suspicious activity on your account with (company name). To ensure your account is secure, we need you to sign in and verify your account.\n\nWhat Happened:\n\nWe noticed a login attempt from an unfamiliar location/device. For your protection, we have temporarily locked your account until we can confirm that it was you.\n\nWhat You Need to Do:\n\nPlease sign in to your account and review the recent activity using the link below. If the activity was not authorized by you, please follow the steps to secure your account.\n\nSign In to Your Account:\n\n(phishing link)\n\nIf you did not attempt to log in or if you don’t recognize the recent activity, we strongly recommend changing your password and reviewing your account for any unauthorized changes.\n\nBest regards,\nThe (security group) Team")
    else:
        print("\nInvalid option. The program will terminate. Did you mistype a command?")

if __name__ == '__main__':
    main()
