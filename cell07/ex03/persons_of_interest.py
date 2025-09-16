def famous_births(persons):
    """
    Takes a dictionary representing historical figures as a parameter.
    Each entry in the dictionary is itself a dictionary with the keys: name and date_of_birth.
    The method will sort the dictionary passed as a parameter in order of birth dates,
    and then display each entry.
    """
    sorted_persons = sorted(persons.items(), key=lambda item: item[1]["date_of_birth"])

    for person, details in sorted_persons:
        print(f"{details['name']} is a great scientist born in {details['date_of_birth']}.")

# Example usage:
women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)