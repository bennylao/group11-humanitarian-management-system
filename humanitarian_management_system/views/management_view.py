class ManagementView:
    """
    This class contains all the messages that user might see during management.
    """

    @staticmethod
    def event_creation_message():
        print("\n========================================\n"
              "            Event CREATION\n"
              "========================================\n"
              "Please fill in all the following information below.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def event_edit_message():
        print("\n========================================\n"
              "               Event EDIT\n"
              "========================================\n"
              "Please fill in all the following information below.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def event_close_message():
        print("\n========================================\n"
              "               Event CLOSE\n"
              "========================================\n"
              "Please fill in all the following information below.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def event_delete_message():
        print("\n========================================\n"
              "               Event DELETION\n"
              "========================================\n"
              "Please fill in all the following information below.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def camp_main_message():
        print("\n========================================\n"
              "           Camp MANAGEMENT\n"
              "========================================\n"
              "Please select an option from the following.")

    @staticmethod
    def camp_init_message():
        print("\n========================================\n"
              "            Event CREATION\n"
              "========================================\n"
              "Please select a plan by its index.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def camp_creation_message():
        print("\n========================================\n"
              "             Camp CREATION\n"
              "========================================\n"
              "Please fill in all the following information below.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def camp_modification_message():
        print("\n========================================\n"
              "             Camp MODIFICATION\n"
              "========================================\n"
              "Please fill in all the following information below.\n"
              "Or enter 'RETURN' to go back to admin menu page.")


    @staticmethod
    def camp_deletion_message():
        print("\n========================================\n"
              "             Camp DELETION\n"
              "========================================\n"
              "Please fill in all the following information below.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def vol_main_message():
        print("\n========================================\n"
              "      Volunteer account MANAGEMENT\n"
              "========================================\n"
              "Please select an option from the following.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def resource_alloc_main_message():
        print("\n========================================\n"
              "         Resources ALLOCATION\n"
              "========================================\n"
              "Please select 1 for manual allocation.\n"
              "Or 2 for auto allocation.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def man_resource_message():
        print("\n========================================\n"
              "         Allocating manually\n"
              "========================================\n"
              "Please select a camp by its index.\n"
              "Follow by the index of the resource type.\n"
              "And finally the amount you want.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def auto_resource_message():
        print("\n========================================\n"
              "       Allocating automatically\n"
              "========================================\n"
              "Please select a camp by its index.\n"
              "Or enter 'RETURN' to go back to admin menu page.")
        
    @staticmethod
    def resource_report_message():
        print("\n========================================\n"
              "       RESOURCE REPORTING \n"
              "========================================\n"
              "Please select the type of resource report: \n"
              "[1] view total stock levels of all resources; \n"
              "[2] view resource levels by assigned camp")

    @staticmethod
    def join_camp_message():
        print("\n========================================\n"
              "            Join/change CAMP\n"
              "========================================\n"
              "Please select a camp by its index to join\n"
              "Or to change your current camp to that instead.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def create_refugee_message():
        print("\n========================================\n"
              "            Refugee CREATION\n"
              "========================================\n"
              "Please fill in all the following information below.\n"
              "Or to change your current camp to that instead.\n"
              "Or enter 'RETURN' to go back to admin menu page.")

    @staticmethod
    def refugee_edit_message():
        print("\n========================================\n"
              "               Refugee EDIT\n"
              "========================================\n"
              "Please fill in all the following information below.\n"
              "Or enter 'RETURN' to go back to admin menu page.")
