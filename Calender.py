#CALENDER APPLICATION

from datetime import datetime

class Event:
    def __init__(self, title, date, description):
        self.title = title
        self.date = date
        self.description = description

    def __str__(self):
        return f"Title: {self.title}, Date: {self.date}, Description: {self.description}"


class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        print("Event", event.title, "added to the calendar.")

    def view_events(self):
        if not self.events:
            print("No events in the calendar.")
        else:
            for event in self.events:
                print(event)

    def delete_event(self, title):
        event_to_delete = None
        for event in self.events:
            if event.title == title:
                event_to_delete = event
                break
        if event_to_delete:
            self.events.remove(event_to_delete)
            print("Event", title, "deleted from the calendar.")
        else:
            print("Event not found in the calendar.")


def main():
    calendar = Calendar()
    while True:
        print("\nCalendar Menu")
        print("1. Add Event")
        print("2. View Events")
        print("3. Delete Event")
        print("4. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            title = input("Enter the event title: ")
            date_input = input("Enter event date (YYYY-MM-DD): ")
            description = input("Enter event description (optional): ")
            try:
                date = datetime.strptime(date_input, "%Y-%m-%d").date()
                event = Event(title, date, description)
                calendar.add_event(event)
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

        elif ch == 2:
            calendar.view_events()

        elif ch == 3:
            title = input("Enter the title of the event to delete: ")
            calendar.delete_event(title)

        elif ch == 4:
            print("Exiting the calendar application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
