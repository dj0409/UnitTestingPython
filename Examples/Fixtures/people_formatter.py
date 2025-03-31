# people_formatter.py

def format_data_for_display(people):
    """
    Formats a list of people dictionaries into full-name and title strings.
    """
    return [f"{p['given_name']} {p['family_name']}: {p['title']}" for p in people]
