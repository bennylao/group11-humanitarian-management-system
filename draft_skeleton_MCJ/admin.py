class Admin:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def edit_volunteer_account(self, volunteer_name):
        pass

    def allocate_resource(self):
        # should this just call from resources class?
        pass

    def deactivate_user(self):
        pass

    def create_humanitarian_plan(self):
        pass

    def end_event(self):
        # where should this sit? In event class or here?
        # ben: think we can hv a func to end in event class,
        # and we call the func here
        pass

    def display_humanitarian_plan(self):
        # again, should this probably just be called from the event file?
        # ben: is it the func listing all the plan?
        # if so, in the event class, we can have func __str__ format the description for one plan
        # and use a for loop here to print info of all plans
        # alternatively, we can create a static method in the event class,
        # by calling that method, we read the csv file and print out the info (maybe
        pass
