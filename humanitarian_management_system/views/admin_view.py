class AdminView:
    """
    This class contains all the messages that admin might see.
    """

    main_menu = (
        ("1", "Humanitarian Plan (Event) Management"),
        ("2", "Camp Management"),
        ("3", "Volunteer Account Management"),
        ("4", "Resource Management"),
        ("5", "Display Summary/Statistics"),
        ("6", "Edit Account Information"),
        ("7", "View Account Information"),
        ("L", "Logout")
    )

    manage_event_menu = (
        ("1", "Create new event"),
        ("2", "Edit event"),
        ("3", "Close event"),
        ("4", "Delete event"),
        ("5", "Display all events"),
        ("R", "Return to previous page"),
        ("L", "Logout")
    )

    manage_camp_menu = (
        ("1", "Add new camp"),
        ("2", "Edit camp"),
        ("3", "Remove/close camp"),
        ("4", "Add refugees"),
        ("5", "Edit refugees"),
        ("6", "Move/remove refugee(s)"),
        ("7", "Display all refugees information"),
        ("8", "Display all camps information"),
        ("9", "Export a CSV report for all refugees in system"),
        ("10", "Camp data visualization"),
        ("R", "Return to previous page"),
        ("L", "Logout")
    )

    manage_volunteer_menu = (
        ("1", "Edit volunteer profile"),
        ("2", "Display all volunteer information"),
        ("3", "Verify newly registered volunteer"),
        ("4", "Deactivate/reactivate volunteer"),
        ("5", "Remove volunteer"),
        ("R", "Return to previous page"),
        ("L", "Logout")
    )

    manage_resource_menu = (
        ("1", "Allocate resources"),
        ("2", "Purchase from shop"),
        ("3", "View resource statistics"),
        ("R", "Return to previous page"),
        ("L", "Logout")
    )

    @staticmethod
    def display_login_message(username):
        print("\n========================================\n"
              f"           Welcome back {username}\n"
              "========================================\n")

    @classmethod
    def display_menu(cls):
        print("")
        for key, value in cls.main_menu:
            print(f"[ {key} ] {value}")

    @classmethod
    def get_main_options(cls):
        return [options[0] for options in cls.main_menu]

    @classmethod
    def display_event_menu(cls):
        print("")
        for key, value in cls.manage_event_menu:
            print(f"[ {key} ] {value}")

    @classmethod
    def get_event_options(cls):
        return [options[0] for options in cls.manage_event_menu]

    @classmethod
    def display_camp_menu(cls):
        print("")
        for key, value in cls.manage_camp_menu:
            print(f"[ {key} ] {value}")

    @classmethod
    def get_camp_options(cls):
        return [options[0] for options in cls.manage_camp_menu]

    @classmethod
    def display_volunteer_menu(cls):
        print("")
        for key, value in cls.manage_volunteer_menu:
            print(f"[ {key} ] {value}")

    @classmethod
    def get_volunteer_options(cls):
        return [options[0] for options in cls.manage_volunteer_menu]

    @classmethod
    def display_resource_menu(cls):
        print("")
        print(f"""===============================================\n
✩°｡⋆⸜ ✮✩°｡⋆⸜ ✮ RESOURCE MGMT MENU ✩°｡⋆⸜ ✮✩°｡⋆⸜ ✮\n
===============================================\n""")
        for key, value in cls.manage_resource_menu:
            print(f"[ {key} ] {value}")

    @classmethod
    def get_resource_options(cls):
        return [options[0] for options in cls.manage_resource_menu]
