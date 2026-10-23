
# MY WORD - Phone Prison Break V2
# Your Future Self Is Talking
# A personal productivity and focus reminder app

import json
import os
import time
import sys

SETTINGS_FILE = "myword_settings.json"

DEFAULT_SETTINGS = {
    "app": "Facebook",
    "limit": 20,
    "message": (
        "Stop scrolling! Your future is waiting. "
        "Go learn, build your skills, and achieve your goals!"
    ),
    "username": "Friend"
}


def load_settings():
    """Load saved settings or create default settings."""
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
                settings = json.load(file)

            for key, value in DEFAULT_SETTINGS.items():
                if key not in settings:
                    settings[key] = value

            return settings

        except (json.JSONDecodeError, OSError):
            print("Could not read settings. Using defaults.")

    return DEFAULT_SETTINGS.copy()


def save_settings(settings):
    """Save the user's choices."""
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)
        print("\nSettings saved successfully!")
    except OSError as error:
        print(f"Could not save settings: {error}")


def change_settings(settings):
    """Allow the user to customise the app."""
    print("\n=== CUSTOMISE MY WORD ===")

    print("\nChoose the app you want to limit:")
    print("1. TikTok")
    print("2. Facebook")
    print("3. YouTube")
    print("4. Instagram")
    print("5. WhatsApp")
    print("6. Other")

    choices = {
        "1": "TikTok",
        "2": "Facebook",
        "3": "YouTube",
        "4": "Instagram",
        "5": "WhatsApp"
    }

    choice = input("Enter your choice (1-6): ").strip()

    if choice in choices:
        settings["app"] = choices[choice]
    elif choice == "6":
        custom_app = input("Enter the app name: ").strip()
        if custom_app:
            settings["app"] = custom_app
    else:
        print("Invalid choice. Keeping the current app.")

    print("\nChoose your time limit:")
    print("1. 15 minutes")
    print("2. 20 minutes")
    print("3. 30 minutes")
    print("4. 60 minutes")
    print("5. Enter a custom number")

    limits = {
        "1": 15,
        "2": 20,
        "3": 30,
        "4": 60
    }

    choice = input("Enter your choice (1-5): ").strip()

    if choice in limits:
        settings["limit"] = limits[choice]
    elif choice == "5":
        try:
            minutes = int(input("Enter minutes: "))
            if 1 <= minutes <= 1440:
                settings["limit"] = minutes
            else:
                print("Enter between 1 and 1440 minutes.")
        except ValueError:
            print("Invalid number. Keeping the current limit.")

    username = input(
        "\nEnter your name (or press Enter to keep the current name): "
    ).strip()

    if username:
        settings["username"] = username

    message = input(
        "\nWrite your personal reminder "
        "(or press Enter to keep the current message):\n"
    ).strip()

    if message:
        settings["message"] = message

    save_settings(settings)


def show_settings(settings):
    """Display the user's current choices."""
    print("\n========== YOUR MY WORD SETTINGS ==========")
    print(f"Name: {settings['username']}")
    print(f"Selected app: {settings['app']}")
    print(f"Time limit: {settings['limit']} minutes")
    print(f"Your reminder: {settings['message']}")
    print("===========================================")


def start_focus_timer(settings):
    """Run a countdown and display the user's message."""
    minutes = settings["limit"]
    total_seconds = minutes * 60

    print(f"\nFocus timer started for {settings['app']}.")
    print(f"You have {minutes} minutes.")
    print("Keep this Python program running.")
    print("Press Ctrl+C to cancel if your Python app supports it.")
    print("\nStay focused. Your future matters!")

    start_time = time.monotonic()

    try:
        while True:
            elapsed = time.monotonic() - start_time
            remaining = total_seconds - int(elapsed)

            if remaining <= 0:
                break

            mins, secs = divmod(remaining, 60)
            print(
                f"\rTime remaining: {mins:02d}:{secs:02d}",
                end="",
                flush=True
            )
            time.sleep(1)

        print("\n\n" + "=" * 42)
        print("          YOUR WORD HAS ARRIVED!")
        print("=" * 42)
        print(f"\n{settings['username']}, listen to yourself:\n")
        print(settings["message"])
        print("\n" + "=" * 42)
        print("You can do this. Take action now!")
        print("=" * 42)

        # Try to make a sound on systems that support it.
        try:
            print("\a", end="", flush=True)
        except Exception:
            pass

    except KeyboardInterrupt:
        print("\n\nTimer cancelled. You can try again later.")


def main():
    settings = load_settings()

    print("\n" + "=" * 42)
    print("       MY WORD - PHONE PRISON BREAK")
    print("         Your Future Self Is Talking")
    print("=" * 42)

    while True:
        print("\nMAIN MENU")
        print("1. Start focus timer")
        print("2. Customise my settings")
        print("3. View my settings")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            start_focus_timer(settings)

        elif choice == "2":
            change_settings(settings)

        elif choice == "3":
            show_settings(settings)

        elif choice == "4":
            print("\nRemember: your future is built by your actions.")
            print("Thank you for using JOVARA!")
            sys.exit(0)

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
