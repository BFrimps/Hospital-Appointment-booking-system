import datetime
from appbooking import AppBooking

class HospitalBookingSystem:
    def __init__(self):
        self.appbookings = []

    def schedule_appbooking(self):
        pat_name = input("Enter patient's name: ")
        doc_name = input("Enter doctor's name: ")
        date_str = input("Enter date (YYYY-MM-DD): ")
        time_str = input("Enter time (HH:MM): ")

        if self.is_valid_datetime(date_str, time_str):
            date = datetime.datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            
            
            if self.is_time_slot_available(doc_name, date.date(), date.time()):
                appbooking = AppBooking(pat_name, doc_name, date.date(), date.time())
                self.appbookings.append(appbooking)
                print("Booking scheduled successfully!")
            else:
                print(" Please choose another time. Time already booked")
        else:
            print("Incorrect date or time format. Please enter again.")

    def is_valid_datetime(self, date_str, time_str):
        if datetime.datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M"):
            return True
        else:
            return False

    def is_time_slot_available(self, doc_name, date, time):
        for booking in self.appbookings:
            if (booking.doc_name == doc_name and 
                booking.date == date and 
                booking.time == time):
                return False
        return True

    def view_appbookings(self):
        if not self.appbookings:
            print("No appointments scheduled.")
        else:
            for i, appbooking in enumerate(self.appbookings, 1):
                print(f"{i}. Patient: {appbooking.pat_name}, Doctor: {appbooking.doc_name}, "
                      f"Date: {appbooking.date.strftime('%Y-%m-%d')}, "
                      f"Time: {appbooking.time.strftime('%H:%M')}")

    def cancel_appbookings(self):
        self.view_appbookings()
        if self.appbookings:
            index_str = input("Enter the number of the appointment to cancel: ")
            if index_str.isdigit():
                index = int(index_str) - 1
                if 0 <= index < len(self.appbookings):
                    cancelled = self.appbookings.pop(index)
                    print(f"Booking for {cancelled.pat_name} on "
                          f"{cancelled.date.strftime('%Y-%m-%d')} at "
                          f"{cancelled.time.strftime('%H:%M')} cancelled.")
                else:
                    print("Invalid booking number.")
            else:
                print("Invalid input. Please enter a number.")
        else:
            print("No bookings to cancel.")