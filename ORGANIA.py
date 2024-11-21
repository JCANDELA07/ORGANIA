from datetime import datetime, timedelta

# Define the UserProfile class
class UserProfile:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.body_weight_log = []  # Log to track body weight over time
        self.sleep_schedule = {}   # User's sleep schedule by day
        self.meal_prep_frequency = {}  # Frequency of meal prep

    def log_weight(self, weight, date=None):
        date = date or datetime.now().date()
        self.body_weight_log.append((date, weight))

    def set_sleep_schedule(self, day, start, end):
        """Define sleep schedule for a specific day."""
        self.sleep_schedule[day] = {"start": start, "end": end}

    def set_meal_prep_frequency(self, times_per_day=None, times_per_week=None):
        """Define meal prep frequency."""
        self.meal_prep_frequency = {
            "times_per_day": times_per_day,
            "times_per_week": times_per_week
        }

# Define the Schedule class
class Schedule:
    def __init__(self):
        self.work_hours = {}         # Work schedule by day
        self.school_hours = {}       # School schedule by day
        self.gym_schedule = []       # Gym schedule (optional)
        self.sports_schedule = []    # Sports schedule (optional)
        self.hobbies_schedule = []   # Hobbies schedule (optional)
        self.vacations = []          # Vacation plans

    def set_work_hours(self, day, start, end, location):
        self.work_hours[day] = {"start": start, "end": end, "location": location}

    def set_school_hours(self, day, start, end, location):
        self.school_hours[day] = {"start": start, "end": end, "location": location}

    def add_gym_schedule(self, day, time, location, frequency):
        self.gym_schedule.append({"day": day, "time": time, "location": location, "frequency": frequency})

    def add_sports_schedule(self, day, time, location, frequency):
        self.sports_schedule.append({"day": day, "time": time, "location": location, "frequency": frequency})

    def add_hobbies_schedule(self, day, time, location, frequency):
        self.hobbies_schedule.append({"day": day, "time": time, "location": location, "frequency": frequency})

    def add_vacation(self, start_date, end_date, location, preference):
        """Vacation preference can be 'budget' or 'luxury'."""
        self.vacations.append({
            "start_date": start_date,
            "end_date": end_date,
            "location": location,
            "preference": preference
        })

# Define the Task class
class Task:
    def __init__(self, name, location, materials, duration, due_date=None):
        self.name = name
        self.location = location
        self.materials = materials    # Materials needed for the task
        self.duration = duration      # Duration in minutes
        self.due_date = due_date      # Optional due date

    def __repr__(self):
        return f"{self.name} - {self.duration} mins at {self.location} [Due: {self.due_date or 'N/A'}]"

# Define the Appointment class
class Appointment:
    def __init__(self, name, date, time, location):
        self.name = name
        self.date = date
        self.time = time
        self.location = location

    def __repr__(self):
        return f"{self.name} on {self.date} at {self.time}, Location: {self.location}"

# Define the TaskOrganizer class
class TaskOrganizer:
    def __init__(self, user_profile, schedule):
        self.user_profile = user_profile
        self.schedule = schedule
        self.tasks = []
        self.appointments = []

    def add_task(self, task):
        """Add a task and suggest the best days based on the user's schedule."""
        best_days = self.find_best_days(task)
        task.suggested_days = best_days  # Store suggested days in the task
        self.tasks.append(task)

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def find_best_days(self, task):
        """Suggest optimal days for a task based on work, school, and other activities."""
        available_days = []
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            if not self.schedule.work_hours.get(day) and not self.schedule.school_hours.get(day):
                available_days.append(day)
        return available_days

    def view_schedule(self):
        """Display a summary of the user's tasks, appointments, and weekly schedule."""
        print("\n--- User Schedule ---")
        print(f"Name: {self.user_profile.name}, Age: {self.user_profile.age}")
        print("Body Weight Log:", self.user_profile.body_weight_log)
        print("Meal Prep Frequency:", self.user_profile.meal_prep_frequency)

        print("\n--- Tasks ---")
        for task in self.tasks:
            print(f"  - {task}")

        print("\n--- Appointments ---")
        for appt in self.appointments:
            print(f"  - {appt}")

        print("\n--- Work Schedule ---")
        for day, hours in self.schedule.work_hours.items():
            print(f"  - {day}: {hours}")

        print("\n--- School Schedule ---")
        for day, hours in self.schedule.school_hours.items():
            print(f"  - {day}: {hours}")

        print("\n--- Gym Schedule ---")
        for gym in self.schedule.gym_schedule:
            print(f"  - {gym}")

        print("\n--- Sports Schedule ---")
        for sport in self.schedule.sports_schedule:
            print(f"  - {sport}")

        print("\n--- Hobbies Schedule ---")
        for hobby in self.schedule.hobbies_schedule:
            print(f"  - {hobby}")

        print("\n--- Vacations ---")
        for vacation in self.schedule.vacations:
            print(f"  - {vacation}")

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox, QTextEdit
import sys

class UserProfile:
    def __init__(self, name):
        self.name = name
        self.weight = "150 lbs"
        self.sleep_schedule = "10:00 PM - 6:00 AM"
        self.eating_schedule = "8:00 AM, 12:00 PM, 6:00 PM"
        self.meal_prep = "Once per day"
        self.pet_time = "30 minutes per day"
        self.work_schedule = "9:00 AM - 5:00 PM, Location: Office"
        self.school_schedule = "8:00 AM - 3:00 PM, Location: University"
        self.gym_schedule = "5:30 PM, Location: Local Gym"
        self.sports_schedule = "2 times per week, Location: Soccer Field"
        self.hobbies_schedule = "Weekend Mornings, Location: Park"

class TaskOrganizerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Organizer App")
        self.setGeometry(100, 100, 600, 800)
        self.user_profile = None
        self.init_ui()

    def init_ui(self):
        # Stack for different screens
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # Create screens
        self.login_screen = self.create_login_screen()
        self.schedule_screen = self.create_schedule_screen()
        self.main_app_screen = self.create_main_app_screen()
        self.new_task_screen = self.create_new_task_screen()

        # Add screens to the stack
        self.stack.addWidget(self.login_screen)
        self.stack.addWidget(self.schedule_screen)
        self.stack.addWidget(self.main_app_screen)
        self.stack.addWidget(self.new_task_screen)

    def create_login_screen(self):
        login_widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Username:"))
        self.username_input = QLineEdit()
        layout.addWidget(self.username_input)

        layout.addWidget(QLabel("Password:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        login_widget.setLayout(layout)
        return login_widget

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "user" and password == "password":
            self.user_profile = UserProfile(username)
            self.stack.setCurrentWidget(self.schedule_screen)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid username or password.")

    def create_schedule_screen(self):
        schedule_widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Weight (lbs):"))
        self.weight_input = QLineEdit(self.user_profile.weight if self.user_profile else "150 lbs")
        layout.addWidget(self.weight_input)

        layout.addWidget(QLabel("Sleep Schedule:"))
        self.sleep_schedule_input = QLineEdit(self.user_profile.sleep_schedule if self.user_profile else "10:00 PM - 6:00 AM")
        layout.addWidget(self.sleep_schedule_input)

        layout.addWidget(QLabel("Eating Schedule:"))
        self.eating_schedule_input = QLineEdit(self.user_profile.eating_schedule if self.user_profile else "8:00 AM, 12:00 PM, 6:00 PM")
        layout.addWidget(self.eating_schedule_input)

        layout.addWidget(QLabel("Meal Prep (times per day):"))
        self.meal_prep_input = QLineEdit(self.user_profile.meal_prep if self.user_profile else "Once per day")
        layout.addWidget(self.meal_prep_input)

        layout.addWidget(QLabel("Pet Time:"))
        self.pet_time_input = QLineEdit(self.user_profile.pet_time if self.user_profile else "30 minutes per day")
        layout.addWidget(self.pet_time_input)

        layout.addWidget(QLabel("Work Schedule:"))
        self.work_schedule_input = QLineEdit(self.user_profile.work_schedule if self.user_profile else "9:00 AM - 5:00 PM, Location: Office")
        layout.addWidget(self.work_schedule_input)

        layout.addWidget(QLabel("School Schedule:"))
        self.school_schedule_input = QLineEdit(self.user_profile.school_schedule if self.user_profile else "8:00 AM - 3:00 PM, Location: University")
        layout.addWidget(self.school_schedule_input)

        layout.addWidget(QLabel("Gym Schedule:"))
        self.gym_schedule_input = QLineEdit(self.user_profile.gym_schedule if self.user_profile else "5:30 PM, Location: Local Gym")
        layout.addWidget(self.gym_schedule_input)

        layout.addWidget(QLabel("Sports Schedule:"))
        self.sports_schedule_input = QLineEdit(self.user_profile.sports_schedule if self.user_profile else "2 times per week, Location: Soccer Field")
        layout.addWidget(self.sports_schedule_input)

        layout.addWidget(QLabel("Hobbies Schedule:"))
        self.hobbies_schedule_input = QLineEdit(self.user_profile.hobbies_schedule if self.user_profile else "Weekend Mornings, Location: Park")
        layout.addWidget(self.hobbies_schedule_input)

        set_schedule_button = QPushButton("Set Schedule")
        set_schedule_button.clicked.connect(self.set_schedule)
        layout.addWidget(set_schedule_button)

        schedule_widget.setLayout(layout)
        return schedule_widget

    def set_schedule(self):
        self.user_profile.weight = self.weight_input.text()
        self.user_profile.sleep_schedule = self.sleep_schedule_input.text()
        self.user_profile.eating_schedule = self.eating_schedule_input.text()
        self.user_profile.meal_prep = self.meal_prep_input.text()
        self.user_profile.pet_time = self.pet_time_input.text()
        self.user_profile.work_schedule = self.work_schedule_input.text()
        self.user_profile.school_schedule = self.school_schedule_input.text()
        self.user_profile.gym_schedule = self.gym_schedule_input.text()
        self.user_profile.sports_schedule = self.sports_schedule_input.text()
        self.user_profile.hobbies_schedule = self.hobbies_schedule_input.text()

        self.stack.setCurrentWidget(self.main_app_screen)
        self.update_schedule_display()

    def create_main_app_screen(self):
        main_widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Weekly Schedule:"))
        self.schedule_display = QTextEdit()
        self.schedule_display.setReadOnly(True)
        layout.addWidget(self.schedule_display)

        self.update_schedule_display()

        new_task_button = QPushButton("New Task")
        new_task_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.new_task_screen))
        layout.addWidget(new_task_button)

        main_widget.setLayout(layout)
        return main_widget

    def update_schedule_display(self):
        self.schedule_display.clear()
        self.schedule_display.append(f"Weight: {self.user_profile.weight}")
        self.schedule_display.append(f"Sleep Schedule: {self.user_profile.sleep_schedule}")
        self.schedule_display.append(f"Eating Schedule: {self.user_profile.eating_schedule}")
        self.schedule_display.append(f"Meal Prep: {self.user_profile.meal_prep}")
        self.schedule_display.append(f"Pet Time: {self.user_profile.pet_time}")
        self.schedule_display.append(f"Work Schedule: {self.user_profile.work_schedule}")
        self.schedule_display.append(f"School Schedule: {self.user_profile.school_schedule}")
        self.schedule_display.append(f"Gym Schedule: {self.user_profile.gym_schedule}")
        self.schedule_display.append(f"Sports Schedule: {self.user_profile.sports_schedule}")
        self.schedule_display.append(f"Hobbies Schedule: {self.user_profile.hobbies_schedule}")

    def create_new_task_screen(self):
        task_widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Task Type:"))
        self.task_type_input = QComboBox()
        self.task_type_input.addItems(["Task", "Appointment", "Vacation"])
        layout.addWidget(self.task_type_input)

        layout.addWidget(QLabel("Location:"))
        self.task_location_input = QLineEdit()
        layout.addWidget(self.task_location_input)

        layout.addWidget(QLabel("Materials (if any):"))
        self.task_material_input = QLineEdit()
        layout.addWidget(self.task_material_input)

        layout.addWidget(QLabel("Time:"))
        self.task_time_input = QLineEdit()
        layout.addWidget(self.task_time_input)

        layout.addWidget(QLabel("Due Date (YYYY-MM-DD):"))
        self.task_due_date_input = QLineEdit()
        layout.addWidget(self.task_due_date_input)

        submit_task_button = QPushButton("Submit Task")
        submit_task_button.clicked.connect(self.add_task)
        layout.addWidget(submit_task_button)

        task_widget.setLayout(layout)
        return task_widget

    def add_task(self):
        task_type = self.task_type_input.currentText()
        location = self.task_location_input.text()
        materials = self.task_material_input.text()
        time = self.task_time_input.text()
        due_date = self.task_due_date_input.text()

        self.schedule_display.append(f"{task_type} at {location} on {time}. Due: {due_date}. Materials: {materials}")
        QtWidgets.QMessageBox.information(self, "Task Added",)
