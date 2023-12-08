from pathlib import Path
from humanitarian_management_system import helper
import datetime
import pandas as pd
import logging


class Event:
    """Essentially creating a humanitarian plan. An 'event' is where
    we add a description etc of where the disaster has happened."""

    def __init__(self, title, location, description, no_camp, start_date, end_date, ongoing=True):
        self.title = title
        self.location = location
        self.description = description
        self.no_camp = no_camp
        self.start_date = start_date
        self.end_date = end_date
        self.ongoing = ongoing

    # Access user input info from helper function and pass them into .csv file(s)
    @staticmethod
    def create_new_record(event_info):
        """
        This is the function to create a new event and write new record into csv file.
        """
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            if pd.read_csv(event_csv_path).empty:
                last_event_id = 0
            else:
                last_event_id = pd.read_csv(event_csv_path)['eventID'].max()

            max_eid_csv_path = Path(__file__).parents[1].joinpath("data/maxUsedEid.csv")
            max_used_eid = pd.read_csv(max_eid_csv_path)['max_used_eid'].max()
            event_id = max(last_event_id, max_used_eid) + 1
            # insert user id into registration_info
            event_info.insert(0, event_id)
            event_df = pd.DataFrame(data=[event_info],
                                    columns=['eventID', 'ongoing', 'title', 'location', 'description', 'no_camp',
                                             'startDate', 'endDate'])
            event_df.to_csv(event_csv_path, mode='a', index=False, header=False)

            max_used_eid = event_id
            helper.modify_csv_value(max_eid_csv_path, 0, 'max_used_eid', max_used_eid)
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")

    @staticmethod
    def get_all_active_events():
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            df = pd.read_csv(event_csv_path)
            print(df)
            active_events_df = df[(df['ongoing'] == True) & ((pd.to_datetime(df['endDate']).dt.date >
                                                              datetime.date.today()) | (pd.isna(df['endDate'])))]
            return active_events_df
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")

    @staticmethod
    def edit_event_info():
        """
        To edit event information except eid.
        Recognize which event and which column need to be edited,
        then edit by calling each corresponding private function.
        """
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            df = pd.read_csv(event_csv_path)
            if df.empty:
                print("\nNo events to edit.")
                return
            filtered_df = df[(df['ongoing'] == 'True') | (df['ongoing'] == 'Yet')]
            if filtered_df.empty:
                print("\nAll the events are closed and cannot be edited.")
                return

            row = -1
            while True:
                try:
                    Event.display_events(filtered_df)
                    eid_to_edit = input('\n--> Enter the event ID to update:')
                    if eid_to_edit == 'RETURN':
                        return
                    elif int(eid_to_edit) not in filtered_df['eventID'].values:
                        print(
                            f"\nInvalid input! Please enter an integer from {filtered_df['eventID'].values} for Event ID.")
                        continue
                    else:
                        row = df[df['eventID'] == int(eid_to_edit)].index[0]
                        break
                except IndexError:
                    print("\nInvalid event ID entered.")
                    continue
                except ValueError:
                    print("\nInvalid event ID entered.")
                    continue

            while True:
                try:
                    what_to_edit = input('\n--> Choose one to edit (title/ location/ description/ startDate/ endDate):')
                    if what_to_edit == 'RETURN':
                        return
                    else:
                        df[what_to_edit]
                        break
                except KeyError:
                    print("\nInvalid option name entered.")
                    continue

            if what_to_edit == 'title':
                Event.__change_title(row)
            elif what_to_edit == 'location':
                Event.__change_location(row)
            elif what_to_edit == 'description':
                Event.__change_description(row)
            elif what_to_edit == 'startDate':
                Event.__change_start_date(row)
            else:
                Event.__change_end_date(row)
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")

    @staticmethod
    def __change_title(row):
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            title = input("\n--> Plan title: ")
            if title == 'RETURN':
                return
            helper.modify_csv_value(event_csv_path, row, 'title', title)
            print("\nPlan title updated.")
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")

    @staticmethod
    def __change_location(row):
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            country = []
            country_data = pd.read_csv(event_csv_path)['location']
            for ele in country_data:
                country.append(ele.lower())
            location = ''
            for ele in country_data:
                country.append(ele.lower())
            while len(location) == 0 and location not in country:
                location = input("\n--> Location(country): ").lower()
                if location.upper() == 'RETURN':
                    return
                if location not in country:
                    print("\nInvalid country name entered")
                    location = ''
                    continue
            helper.modify_csv_value(event_csv_path, row, 'location', location)
            print("\nLocation updated.")
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")

    @staticmethod
    def __change_description(row):
        """Option for users to change the description of the event
        in case they made a mistake or the situation escalates etc"""
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            description = input("\n--> Description: ")
            if description == 'RETURN':
                return
            helper.modify_csv_value(event_csv_path, row, 'description', description)
            print("\nDescription updated.")
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")

    @staticmethod
    def __change_start_date(row):
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            df = pd.read_csv(event_csv_path)
            date_format = '%d/%m/%Y'
            while True:
                if df.loc[row]['ongoing'] == 'True':
                    print("\nThis event has started, the start date cannot be changed.")
                    break
                try:
                    start_date = input("\n--> Start date (format dd/mm/yy): ")
                    if start_date == 'RETURN':
                        return
                    else:
                        start_date = datetime.datetime.strptime(start_date, date_format)
                        formatted_start_date = start_date.strftime('%Y-%m-%d')
                        helper.modify_csv_value(event_csv_path, row, 'startDate', formatted_start_date)
                        Event.update_ongoing()
                        print("\nStart date updated.")
                        break
                except ValueError:
                    print("\nInvalid date format entered.")
                    continue
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")

    @staticmethod
    def __change_end_date(row):
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            df = pd.read_csv(event_csv_path)
            date_format = '%d/%m/%Y'
            while True:
                try:
                    end_date = input("\n--> End date (format dd/mm/yy): ")
                    if end_date == 'RETURN':
                        return
                    if end_date == 'NONE':
                        helper.modify_csv_value(event_csv_path, row, 'endDate', None)
                        print("\nEnd date updated.")
                        break
                    else:
                        end_date = datetime.datetime.strptime(end_date, date_format)
                        if end_date <= datetime.datetime.strptime(df['startDate'].loc[row], '%Y-%m-%d'):
                            print("\nEnd date has to be later than start date.")
                            continue
                        break
                except ValueError:
                    print("\nInvalid date format entered.")
                    continue
            if end_date == 'NONE':
                return
            elif end_date.date() > datetime.date.today():
                formatted_end_date = end_date.strftime('%Y-%m-%d')
                helper.modify_csv_value(event_csv_path, row, 'endDate', formatted_end_date)
                print("\nEnd date updated.")
            else:
                camp_csv_path = Path(__file__).parents[1].joinpath("data/camp.csv")
                df_camp = pd.read_csv(camp_csv_path)
                row_camp_list = df_camp[
                    (df_camp['eventID'] == df.loc[row, 'eventID']) & (df_camp['status'] == 'open')].index.tolist()
                while True:
                    result = input("\nAre you sure you want to close the event? You'll also close the camps in that event. (yes/no)")
                    if result == "yes":
                        ongoing = 'False'
                        if df['ongoing'].loc[row] == 'Yet':
                            ongoing = 'Yet'
                        elif df['ongoing'].loc[row] == 'True':
                            ongoing = False
                        formatted_end_date = end_date.strftime('%Y-%m-%d')
                        helper.modify_csv_value(event_csv_path, row, 'endDate', formatted_end_date)
                        helper.modify_csv_value(event_csv_path, row, 'ongoing', ongoing)
                        if row_camp_list:
                            for row_camp in row_camp_list:
                                helper.modify_csv_value(camp_csv_path, row_camp, 'status', 'closed')
                        print("\n***  The event has been successfully closed.  ***")
                        break
                    elif result == "no":
                        print("\n***  The operation to close the event was canceled.  ***")
                        break
                    else:
                        print("\nYou need to choose between 'yes/no'")
                        continue
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")

    @staticmethod
    def display_events(df):
        table_str = df.to_markdown(index=False)
        print("\n" + table_str)

    @staticmethod
    def update_ongoing():
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            df = pd.read_csv(event_csv_path)
            camp_csv_path = Path(__file__).parents[1].joinpath("data/camp.csv")
            df_camp = pd.read_csv(camp_csv_path)
            for index, series in df.iterrows():
                try:
                    start_date = datetime.datetime.strptime(str(series['startDate']), '%Y-%m-%d')
                except ValueError:
                    start_date = None
                try:
                    end_date = datetime.datetime.strptime(str(series['endDate']), '%Y-%m-%d')
                except ValueError:
                    end_date = None

                if ((end_date == None and start_date.date() <= datetime.date.today()) or
                        (start_date.date() <= datetime.date.today() and end_date.date() > datetime.date.today())):
                    helper.modify_csv_value(event_csv_path, index, 'ongoing', True)
                elif start_date.date() > datetime.date.today():
                    helper.modify_csv_value(event_csv_path, index, 'ongoing', 'Yet')
                else:
                    helper.modify_csv_value(event_csv_path, index, 'ongoing', False)
                    row_camp_list = df_camp[
                        (df_camp['eventID'] == df.loc[index, 'eventID']) & (df_camp['status'] == 'open')].index.tolist()
                    if row_camp_list:
                        for row_camp in row_camp_list:
                            helper.modify_csv_value(camp_csv_path, row_camp, 'status', 'closed')
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")

    @staticmethod
    def disable_ongoing_event():
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            df = pd.read_csv(event_csv_path)
            camp_csv_path = Path(__file__).parents[1].joinpath("data/camp.csv")
            df_camp = pd.read_csv(camp_csv_path)
            filtered_df = df[(df['ongoing'] == 'True')]

            print("\n*The following shows the info of all available events*")
            Event.display_events(filtered_df)

            eid_to_close = -1
            while True:
                try:
                    eid_to_close = input('\n--> Enter the event ID to close:')
                    if eid_to_close == 'RETURN':
                        return
                    elif int(eid_to_close) not in filtered_df['eventID'].values:
                        print(f"\nInvalid input! Please enter an integer from {filtered_df['eid'].values} for Event ID.")
                        continue
                    else:
                        break
                except IndexError:
                    print("\nInvalid event ID entered.")
                    continue
                except ValueError:
                    print("\nInvalid event ID entered.")
                    continue

            row = df[df['eventID'] == int(eid_to_close)].index[0]
            row_camp_list = df_camp[
                (df_camp['eventID'] == int(eid_to_close)) & (df_camp['status'] == 'open')].index.tolist()
            while True:
                result = input("\nAre you sure you want to close the event? You'll also close the camps in that event. (yes/no)")
                if result == "yes":
                    ongoing = False
                    helper.modify_csv_value(event_csv_path, row, 'endDate', datetime.date.today())
                    helper.modify_csv_value(event_csv_path, row, 'ongoing', ongoing)
                    if row_camp_list:
                        for row_camp in row_camp_list:
                            helper.modify_csv_value(camp_csv_path, row_camp, 'status', 'closed')
                    print("\n***  The event has been successfully closed.  ***")
                    break
                elif result == "no":
                    print("\n***  The operation to close the event was canceled.  ***")
                    break
                else:
                    print("\nYou need to choose between 'yes/no'")
                    continue
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")

    @staticmethod
    def delete_event():
        try:
            event_csv_path = Path(__file__).parents[1].joinpath("data/event.csv")
            df = pd.read_csv(event_csv_path)

            print("\n*The following shows the info of all available events*")
            Event.display_events(df)

            eid_to_delete = -1
            while True:
                try:
                    eid_to_delete = input('\n--> Enter the event ID to delete:')
                    if eid_to_delete == 'RETURN':
                        return
                    elif int(eid_to_delete) not in df['eventID'].values:
                        print(f"\nInvalid input! Please enter an integer from {df['eventID'].values} for Event ID.")
                        continue
                    else:
                        break
                except IndexError:
                    print("\nInvalid event ID entered.")
                    continue
                except ValueError:
                    print("\nInvalid event ID entered.")
                    continue
            while True:
                result = input("Are you sure you want to delete the event? "
                               "You'll also close the camps and lose all the information about the refugees in that event. (yes/no)")
                if result == "yes":
                    df.drop(df[df['eventID'] == int(eid_to_delete)].index, inplace=True)
                    df.to_csv(event_csv_path, index=False)
                    # --------- added logic to delete refugees in this event -----------------
                    refugee_csv_path = Path(__file__).parents[1].joinpath("data/refugee.csv")
                    ref_df = pd.read_csv(refugee_csv_path)
                    camp_csv_path = Path(__file__).parents[1].joinpath("data/camp.csv")
                    camp_df = pd.read_csv(camp_csv_path)
                    camps_in_event = camp_df.loc[camp_df['eventID'] == eid_to_delete, 'campID'].tolist()
                    refugees_in_camps_in_event = ref_df[(ref_df['campID'].isin(camps_in_event))]
                    ref_df.drop(refugees_in_camps_in_event.index, inplace=True)
                    ref_df.reset_index(drop=True, inplace=True)
                    ref_df.to_csv(refugee_csv_path, index=False)

                    # reset volunteer camp, role and event info after event is deleted
                    vol_csv_path = Path(__file__).parents[1].joinpath("data/user.csv")
                    vol_df = pd.read_csv(vol_csv_path)
                    vol_id_arr = vol_df.loc[vol_df['campID'] == int(eid_to_delete)]['userID'].tolist()

                    for i in vol_id_arr:
                        helper.modify_csv_pandas("data/user.csv", 'userID', int(i), 'eventID',
                                                 0)
                        helper.modify_csv_pandas("data/user.csv", 'userID', int(i), 'campID',
                                                 0)
                        helper.modify_csv_pandas("data/user.csv", 'userID', int(i), 'roleID',
                                                 0)
                    row_camp_list = camp_df[
                        (camp_df['eventID'] == int(eid_to_delete)) & (camp_df['status'] == 'open')].index.tolist()
                    if row_camp_list:
                        for row_camp in row_camp_list:
                            helper.modify_csv_value(camp_csv_path, row_camp, 'status', 'closed')
                    print("\n***  The event has been successfully deleted.  ***")
                    break
                elif result == "no":
                    print("\n***  The operation to delete the event was canceled.  ***")
                    break
                else:
                    print("\nYou need to choose between 'yes/no'")
                    continue
        except FileNotFoundError as e:
            print(f"\nFile not found."
                  f"\nPlease contact admin for further assistance."
                  f"\n[Error] {e}")
            logging.critical(f"{e}")