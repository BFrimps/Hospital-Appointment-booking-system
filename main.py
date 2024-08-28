from hospsyst import HospitalBookingSystem

def main():
    hospital_booking = HospitalBookingSystem()

    while True:
        print("\nHospital Booking System")
        print("1. Book an appointment")
        print("2. View bookings")
        print("3. Cancel a booking")
        print("4. Exit")

        choice = input("Input your choice (1-4): ")

        if choice == '1':
            hospital_booking.schedule_appbooking()
        elif choice == '2':
            hospital_booking.view_appbookings()
        elif choice == '3':
            hospital_booking.cancel_appbookings()
        elif choice == '4':
            print("Thank you for booking with Us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()