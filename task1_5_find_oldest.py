def find_oldest(people: list) -> tuple:
    """
    Find the oldest person from a list of tuples (name, age).
    Args:
        people (list): List of tuples containing (name, age) pairs
    Returns:
        tuple: A tuple containing (name, age) of the oldest person
    """
    a=people[0]
    for i in people:
        if i[1]>a[1]:
            a=i
            
    return a
print(find_oldest([("Ali", 20), ("Sara", 25), ("John", 28)]))
    