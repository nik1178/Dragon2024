import flet as ft
from flet import *
from flet_core.control_event import ControlEvent
import json

def append_data_to_json(file_path, new_data):
    # Try to load existing data
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            assert isinstance(data, list)  # Ensure it is a list as expected
    except FileNotFoundError:
        data = []  # If not found, start with an empty list
    except json.JSONDecodeError:
        raise Exception("File is not in valid JSON format")
    
    # Append new data to the list
    data.append(new_data)

    # Write updated data back to the file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def checkjson(new_data):
    filename = 'login.json'  # Path to the JSON file containing the user data

    # Load JSON data from the file
    try:
        with open(filename, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return

       # Iterate through each user in the list
    for user in users:
        # Retrieve 'username' or 'name' based on available keys
        username = user.get('name') or user.get('username')  # Handle variations in key naming
        password = user['password']  # It is assumed that every entry will have a 'password' key

        print(f"Username: {username}, Password: {password}")
        if username == new_data['username'] and password == new_data['password']:
            return 0
        elif username == new_data['username']:
            return 1
    
    return 2

def main(page: ft.Page) -> None:
    page.title = "Signup"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    #json setup
    filename = 'login.json'

    text_username: TextField = TextField(label="Username", text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label="Password", text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label="I agree to stuff", value=False)
    button_submit: ElevatedButton = ElevatedButton("Sign up", width=200, bgcolor="blue", color="white", disabled=True)

    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        page.update()

    def submit(e: ControlEvent) -> None:
        print("Username:", text_username.value)
        print("Password:", text_password.value)
        new_user = {"username": text_username.value, "password": text_password.value}
        
        if (checkjson(new_user) == 0):
            #slay
            print("welcome")
            page.clean()

            page.add(
                Row(
                    controls=[Text(value=f"Welcome: {text_username.value}", size=20)],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
        elif (checkjson(new_user) == 1):
            #wrong password
            print("wrong password")
            page.clean()

            page.add(
                Row(
                    controls=[Text(value=f"Wrong password")],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
        else:
            #create new user
            append_data_to_json(filename, new_user)

            print("welcome")
            page.clean()

            page.add(
                Row(
                    controls=[Text(value=f"Welcome: {text_username.value}", size=20)],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
    
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    page.add(
        Row(
            controls=[
                Column(
                    [text_username,
                     text_password,
                     checkbox_signup,
                     button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)

        