#constants for integers
VOLUME_LIMIT :int = 1000000
DIMENSION_LIMIT :int = 150
MASS_LIMIT :int = 20

#constants for strings
STANDARD :str = "STANDARD"
SPECIAL :str = "SPECIAL"
REJECTED :str = "REJECTED"

def sort(width :float, height :float, length :float, mass :float) -> str:
    """Program to sort the packages into correct stack based on their volume and mass.
    Args:
    width (float): Package width in centimeters.
    height (float): Package height in centimeters.
    length (float): Package length in centimeters.
    mass (float): Package mass in kilograms.

    Returns:
    str: One of "STANDARD", "SPECIAL", or "REJECTED".
    """

    # validate all the inputs for quality checks
    for arg in (width, height, length, mass):
        if not isinstance(arg, (int,float)):
            raise ValueError("All inputs must be numbers")
        if arg <= 0:
            raise ValueError("All inputs must be greater than 0")

    total_volume = width * height * length
    bulky :bool = False
    heavy :bool = False

    if total_volume >= VOLUME_LIMIT or max(width, height, length) >= DIMENSION_LIMIT :
        bulky = True
    if mass >= MASS_LIMIT:
        heavy = True

    if bulky and heavy:
        return REJECTED
    if bulky or heavy:
        return SPECIAL
    return STANDARD

if __name__ == '__main__':
    print(sort(100, 200, 100, 10))
