# =====================================================
# PROJECT: Rule-Based Interactive Terminal Assistant
# INTERNSHIP: Datheon Python Programming Internship
# DEVELOPER: Auwal Mohammed Bello
# LANGUAGE: Python
# =====================================================

import re
from datetime import datetime


def get_response(user_input):
    """Generate a response based on keywords and patterns."""

    message = user_input.lower().strip()

    # Greetings
    if re.search(r"\b(hello|hi|hey|sannu)\b", message):
        return "Hello! Welcome to Auwal's Python Assistant."

    # Assistant identity
    elif re.search(r"\b(your name|who are you)\b", message):
        return "I am Auwal's Python Assistant."

    # Business hours
    elif re.search(
        r"\b(hours|opening time|working hours)\b", message
    ):
        return (
            "Our working hours are Monday to Friday, "
            "9 AM to 5 PM."
        )

    # Services
    elif re.search(
        r"\b(services|what do you offer)\b", message
    ):
        return (
            "We provide Python programming, web development, "
            "IT support, and cybersecurity learning."
        )

    # Frequently asked question: contact
    elif re.search(r"\b(contact|email|reach you)\b", message):
        return (
            "Please use the official contact details "
            "provided by the organization."
        )

    # Help commands
    elif re.search(r"\b(help|commands)\b", message):
        return (
            "You can ask about services, working hours, or contact. "
            "Type 'time' to check the current time, "
            "or 'bye' to exit."
        )

    # Current time
    elif re.search(r"\b(time|current time)\b", message):
        now = datetime.now().strftime("%I:%M %p")
        return "The current time is " + now

    # Thanks
    elif re.search(r"\b(thank you|thanks)\b", message):
        return "You're welcome! Happy to help."

    # Exit
    elif re.fullmatch(r"(bye|goodbye|exit|quit)", message):
        return "Goodbye! Thank you for chatting."

    # Fallback response
    else:
        return (
            "Sorry, I don't understand that yet. "
            "Type 'help' to see available commands."
        )


def run_assistant():
    """Run the interactive terminal assistant."""

    print("=" * 45)
    print("      AUWAL'S PYTHON ASSISTANT")
    print("=" * 45)
    print("Hello! I am your interactive assistant.")
    print("Type 'help' for commands.")
    print("Type 'bye' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAssistant: Goodbye!")
            break

        response = get_response(user_input)
        print("Assistant:", response)

        if re.fullmatch(
            r"(bye|goodbye|exit|quit)",
            user_input,
            re.IGNORECASE
        ):
            break


if __name__ == "__main__":
    run_assistant()
