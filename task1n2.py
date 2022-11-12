class Technic(object):
    """Tech's params:
        -price_division : compares tech's price with rate
        -length_name : counts letters in tech's name
        -__cmp__ : compares tech's name length with another length
        -__del__ : deletes object
    """
    __slots__ = ['tech_name', 'price', 'availability']

    def __init__(self, tech_name, price, availability):
        """Constructor"""
        self.tech_name = str(tech_name)
        self.price = float(price)
        self.availability = bool(availability)

    def price_division(self, price_parameter=10000):
        """
        Sorts out the objects of class for expensive/affordable
        Added Price Parameter to determine the expensiveness for company - external parameter
        price_parameter set default at 10k
        """
        is_affordable = False  # expensive as default
        if self.price < price_parameter:
            is_affordable = True
        status = "Affordable" if is_affordable else "Expensive"
        return status

    def length_name(self):
        return len(self.tech_name)

    def __cmp__(self, other):
        return self.length_name() - other

    def __del__(self):
        del self


def decorator(func: object) -> object:
    def wrapper(*args, **kwargs):
        result_comparison = func(*args, **kwargs)
        if result_comparison > 0:
            print("The first name is longer then the second one")
            return 1
        else:
            if result_comparison < 0:
                print("The second name is longer then the second one")
                return -1
            else:
                print("The lengths of names are equal")
                return 0

    return wrapper


@decorator
def compare(first_name: Technic, second_name: Technic):
    return first_name.__cmp__(second_name.length_name())


TV = Technic("television", 10001, True)
personal_computer = Technic("computer", 9999, False)

# print(TV.price_division())
# print(personal_computer.length_name())

compare(TV, personal_computer)

