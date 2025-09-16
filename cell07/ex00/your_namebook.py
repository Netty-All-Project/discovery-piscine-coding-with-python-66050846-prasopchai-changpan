def array_of_names(persons):
    """
    Takes a dictionary associating first names with last names as a parameter.
    Builds an array with the full names of the people, with the first letter capitalized.
    Returns this array.
    """
    names = []
    for first_name, last_name in persons.items():
        full_name = f"{first_name} {last_name}"
        names.append(full_name.capitalize())
    return names

# Example usage:
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))