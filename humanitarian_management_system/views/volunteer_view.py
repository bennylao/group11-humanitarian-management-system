class VolunteerView:
    """
    This class contains all the messages that volunteer might see.
    """

    main_menu = (
        ("1", "Join/Change Camp"),
        ("2", "Camp Management"),
        ("3", "Edit Account Settings and Personal Information"),
        ("L", "Logout")
    )

    manage_camp_menu = (
        ("1", "Add refugee"),
        ("2", "Edit refugee"),
        ("3", "Remove refugee"),
        ("4", "Edit camp profile"),
        ("5", "Display all refugees"),
        ("6", "Display camp information"),
        ("7", "Display all available resources"),
        ("R", "Return to previous page"),
        ("L", "Logout")
    )

    manage_account_menu = (
        ("1", "Change Username"),
        ("2", "Change Password"),
        ("3", "Change Name"),
        ("4", "Change Email"),
        ("5", "Change Phone Number"),
        ("6", "Change Occupation"),
        ("R", "Return to previous page"),
        ("L", "Logout")
    )

    @staticmethod
    def login_message():
        print("\n========================================\n"
              "         Welcome back VOLUNTEER\n"
              "========================================\n"
              "Please select an option from the following.")

    @classmethod
    def display_main_menu(cls):
        print("")
        for key, value in cls.main_menu:
            print(f"[ {key} ] {value}")

    @classmethod
    def get_main_options(cls):
        return [options[0] for options in cls.main_menu]

    @classmethod
    def display_camp_menu(cls):
        print("")
        for key, value in cls.manage_camp_menu:
            print(f"[ {key} ] {value}")

    @classmethod
    def get_camp_options(cls):
        return [options[0] for options in cls.manage_camp_menu]

    @classmethod
    def display_account_menu(cls):
        print("")
        for key, value in cls.manage_account_menu:
            print(f"[ {key} ] {value}")

    @classmethod
    def get_account_options(cls):
        return [options[0] for options in cls.manage_account_menu]
