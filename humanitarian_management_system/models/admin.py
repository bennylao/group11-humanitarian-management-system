from pathlib import Path
import pandas as pd
from .user import User
from humanitarian_management_system import helper
from ..views import ManagementView
import re


class Admin(User):
    def __init__(self, user_id, username, password, first_name, last_name, email, phone, occupation):
        super().__init__(user_id, username, password, first_name, last_name, email, phone, occupation)

    def show_account_info(self):
        user_csv_path = Path(__file__).parents[1].joinpath("data/user.csv")
        df = pd.read_csv(user_csv_path)
        sub_df = df.loc[df['userID'] == int(self.user_id), ['username', 'firstName', 'lastName', 'email',
                                                            'phone', 'occupation']]
        table_str = sub_df.to_markdown(index=False)
        print("\n" + table_str)
        try:
            input("\nPress Enter to return...")
        except SyntaxError:
            pass

    def remove_user(self):
        vol_id_arr = []
        vol_df = pd.read_csv(Path(__file__).parents[1].joinpath("data/user.csv"))

        print("A list of all volunteers and their corresponding information.")
        self.vol_table_display()

        for i in vol_df['userID'].tolist():
            vol_id_arr.append(str(i))

        while True:
            user_select = input("Please select a user ID whose account you would like to delete: ")

            if user_select not in vol_id_arr:
                print("Invalid user ID entered!")
                continue
            if user_select == 'RETURN':
                return

            vol_df = vol_df[vol_df['userID'] != int(user_select)]
            vol_df.reset_index(drop=True, inplace=True)
            vol_df.to_csv(Path(__file__).parents[1].joinpath("data/user.csv"), index=False)
            print(f"User with ID int{user_select} has been deleted.")

            return
        return

    def activate_user(self):
        vol_id_arr = []
        vol_df = pd.read_csv(Path(__file__).parents[1].joinpath("data/user.csv"))

        print("A list of all volunteers and their corresponding information.")
        self.vol_table_display()

        for i in vol_df['userID'].tolist():
            vol_id_arr.append(str(i))

        while True:
            user_select = input("Please select a user ID whose active status you would like to change: ")

            if user_select not in vol_id_arr:
                print("Invalid user ID entered!")
                continue
            else:
                status = vol_df.loc[vol_df['userID'] == int(user_select)]['isActive'].tolist()[0]

            if user_select == 'RETURN':
                return

            if status:
                while True:
                    user_input = input(f"Are you sure you want to deactivate user with ID {int(user_select)} "
                                       f"(yes or no)? ")
                    if user_input.lower() != 'yes' and user_input.lower() != 'no':
                        print("Must enter yes or no!")
                        continue
                    if user_input == 'yes':
                        helper.modify_csv_pandas("data/user.csv", 'userID', int(user_select),
                                                 'isActive', False)
                        print(f"User ID {int(user_select)} has been deactivated.")
                    return

            else:
                user_input = input(f"Are you sure you want to re-activate user with ID {int(user_select)} "
                                   f"(yes or no)? ")

                if user_input.lower() != 'yes' and user_input.lower() != 'no':
                    print("Must enter yes or no!")
                    continue
                if user_input == 'yes':
                    helper.modify_csv_pandas("data/user.csv", 'userID', int(user_select),
                                             'isActive', True)
                    print(f"User ID {int(user_select)} has been re-activated.")
                return
            return

    def display_vol(self):

        joined_df = self.vol_table_display()

        camp_df = pd.read_csv(Path(__file__).parents[1].joinpath("data/camp.csv"))
        event_df = pd.read_csv(Path(__file__).parents[1].joinpath("data/eventTesting.csv"))
        joined_camp = pd.merge(camp_df, event_df, on='eventID', how='inner')

        joined_camp.columns = ['Camp ID', 'Event ID', 'countryID', 'Refugee capacity', 'Health risk',
                               'Volunteer population',
                               'Refugee population', 'Average critical level', 'Camp status', 'ongoing', 'Event title',
                               'Location', 'Event description', 'no_camp', 'Start date', 'End date']

        joined_df_total = pd.merge(joined_df, joined_camp, on='Camp ID', how='inner')
        joined_df_total = joined_df_total.loc[:, ~joined_df_total.columns.isin(['Event ID_x', 'Event ID_y' 'countryID',
                                                                                'ongoing', 'no_camp',
                                                                                'Average critical level',
                                                                                'Is active?', 'Username', 'Password',
                                                                                'First name',
                                                                                'Last name', 'Email', 'Phone no.',
                                                                                'Occupation'])]

        while True:
            user_input = input("Would you like to access the camp & event profile for a particular volunteer "
                               "(yes or no)? ")

            if user_input.lower() == 'yes':
                self.display_camp(joined_df_total)

            if user_input.lower() != 'yes' and user_input.lower() != 'no':
                print("Must enter yes or no!")
                continue
            if user_input.lower() == 'no':
                return
            break

    def display_camp(self, joined_df_total):
        df = pd.read_csv(Path(__file__).parents[1].joinpath("data/user.csv"))
        vol_id_arr = []

        for i in df.loc[df['userType'] == 'volunteer']['userID'].tolist():
            vol_id_arr.append(str(i))

        while True:
            id_input = input("Please enter the volunteer ID whose camp & event profile you would like to see: ")
            if id_input not in vol_id_arr:
                print("Invalid volunteer ID entered!")
                continue

            joined_df_total = joined_df_total.loc[joined_df_total['User ID'] == int(id_input)]
            table_str = joined_df_total.to_markdown(index=False)
            print("\n" + table_str)

            while True:
                user_input = input("Would you like to exit (yes or no)? ")
                if user_input.lower() != 'yes' and user_input.lower() != 'no':
                    print("Must enter yes or no!")
                    continue
                if user_input.lower() == 'no':
                    self.display_vol()
                return
            return
        return

    @staticmethod
    def vol_table_display():
        vol_df = pd.read_csv(Path(__file__).parents[1].joinpath("data/user.csv"))
        vol_df = vol_df.loc[vol_df['userType'] == 'volunteer']
        role_df = pd.read_csv(Path(__file__).parents[1].joinpath("data/roleType.csv"))

        joined_df = pd.merge(vol_df, role_df, on='roleID', how='inner')
        joined_df = joined_df.loc[:, ~joined_df.columns.isin(['userType', 'roleID'])]
        joined_df.columns = ['User ID', 'Is verified?', 'Is active?', 'Username', 'Password', 'First name', 'Last name',
                             'Email',
                             'Phone no.', 'Occupation', 'Event ID', 'Camp ID', 'Camp role']

        table_str = joined_df.to_markdown(index=False)
        print("\n" + table_str)
        return joined_df

    def edit_volunteer(self, change_user):

        while True:
            ManagementView.display_account_menu()
            user_selection = helper.validate_user_selection(ManagementView.get_account_options())
            if user_selection == "1":
                # change username
                self.user_change_username(change_user)
            if user_selection == "2":
                # change password
                self.user_change_password(change_user)
            if user_selection == "3":
                # change name
                self.user_change_name(change_user)
            if user_selection == "4":
                # change email
                self.user_change_email(change_user)
            if user_selection == "5":
                # change phone
                self.user_change_phone(change_user)
            if user_selection == "6":
                # change occupation
                self.user_change_occupation(change_user)
            if user_selection == "R":
                break
            if user_selection == "L":
                break

    def user_change_username(self, change_user):
        existing_usernames = User.get_all_usernames()
        print(f"\nCurrent Username: '{change_user.username}'")
        while True:
            new_username = input("\nPlease enter your new username: ")
            if new_username == "RETURN":
                return
            elif new_username not in existing_usernames and new_username.isalnum():
                change_user.username = new_username
                # update csv file
                change_user.update_username()
                print("\nUsername changed successfully."
                      f"\nYour new username is '{change_user.username}'.")
                break
            elif new_username in existing_usernames:
                print("\nSorry, username already exists.")
                continue
            else:
                print("\nInvalid username entered. Only alphabet letter (Aa-Zz) and numbers (0-9) are allowed.")
                continue

    def user_change_password(self, change_user):
        # specify allowed characters for passwords
        allowed_chars = r"[!@#$%^&*\w]"
        while True:
            new_password = input("Please enter new password: ")
            if new_password == "RETURN":
                return
            elif new_password == change_user.password:
                print("\n The new password is the same as current password!"
                      "Please enter a new one.")
                continue
            elif re.match(allowed_chars, new_password):
                confirm_password = input("Please enter the new password again: ")
                if confirm_password == "RETURN":
                    return
                elif confirm_password == new_password:
                    change_user.password = new_password
                    # update csv file
                    change_user.update_password()
                    print("\nPassword changed successfully.")
                    break
                else:
                    print("The two passwords are not the same!")
            else:
                print("Invalid password entered.\n"
                      "Only alphabet, numbers and !@#$%^&* are allowed.")
                continue

    def user_change_name(self, change_user):
        print(f"\nCurrent Name: {change_user.first_name} {change_user.last_name}")
        while True:
            while True:
                new_first_name = input("\nPlease enter your new first name: ")
                if new_first_name == "RETURN":
                    return
                elif new_first_name.replace(" ", "").isalpha():
                    break
                else:
                    print("\nInvalid first name entered. Only alphabet letter (a-z) are allowed.")
            while True:
                new_last_name = input("\nPlease enter your new last name: ")
                if new_last_name == "RETURN":
                    return
                elif new_last_name.replace(" ", "").isalpha():
                    break
                else:
                    print("\nInvalid last name entered. Only alphabet letter (a-z) are allowed.")

            if new_first_name == change_user.first_name and new_last_name == change_user.last_name:
                print("\nYour new name is the same as your current name!"
                      "Please enter a new name, or enter 'RETURN' to discard the changes and go back")
            else:
                # remove extra whitespaces between words in first name
                change_user.first_name = ' '.join(new_first_name.split())
                # remove extra whitespaces between words in last name
                change_user.last_name = ' '.join(new_last_name.split())
                # update the csv file
                change_user.update_name()
                print("\nName changed successfully."
                      f"\nYour new name is '{change_user.first_name} {change_user.last_name}'.")
                break

    def user_change_email(self, change_user):
        # specify allowed characters for email
        email_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        all_emails = User.get_all_emails()
        print(f"\nCurrent Email: {change_user.email}")

        while True:
            new_email = input("Please enter new email: ")
            if new_email == "RETURN":
                return
            elif new_email == change_user.email:
                print("\n The new email is the same as current email!"
                      "Please enter a new one.")
                continue
            elif re.fullmatch(email_format, new_email) and new_email not in all_emails:
                change_user.email = new_email
                # update csv file
                change_user.update_email()
                print("\nEmail changed successfully."
                      f"\nYour new username is '{change_user.email}'.")
                break
            elif new_email in all_emails:
                print("\nSorry, email is already linked to other account.")
            else:
                print("Invalid password entered.\n"
                      "Only alphabet, numbers and !@#$%^&* are allowed.")
                continue

    def user_change_phone(self, change_user):
        print(f"\nCurrent Phone Number: {change_user.phone}")
        while True:
            new_phone = input("\nPlease enter new phone number: ")
            if new_phone == 'RETURN':
                return
            elif new_phone.isnumeric():
                break
            else:
                print("Invalid phone number entered. Only numbers are allowed.")
        change_user.phone = new_phone
        # update the csv file
        change_user.update_phone()
        print("\nPhone changed successfully."
              f"\nYour new phone is '{change_user.phone}")

    def user_change_occupation(self, change_user):
        print(f"\nCurrent Occupation: {change_user.occupation}")
        while True:
            new_occupation = input("\nPlease enter your new occupation: ")
            if new_occupation == "RETURN":
                return
            elif new_occupation.isalpha():
                change_user.occupation = new_occupation
                # update the csv file
                change_user.update_occupation()
                print("\nName changed successfully."
                      f"\nYour new occupation is '{change_user.occupation}'.")
                break
            else:
                print("\nInvalid first name entered. Only alphabet letter (a-z) are allowed.")
