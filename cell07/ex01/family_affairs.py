def find_the_redheads(family):
    """
    Takes a dictionary representing family members with their first name as the key
    and their hair color as the value.
    Returns a list of the first names of the red-haired individuals.
    """
    redheads = [name for name, hair_color in family.items() if hair_color == "red"]
    return redheads

# Example usage:
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))