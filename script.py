
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    """Input destination name, returns index.

    >>> get_destination_index("Los Angeles, USA")
    2
    """

    destination_index = destinations.index(destination)

    return destination_index

def get_traveler_location(traveler):
    """Input traveler information, returns index of traveler's destination."""

    traveler_destination = traveler[1]

    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

print(test_destination_index)

