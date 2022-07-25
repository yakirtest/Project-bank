import enum


class Business(enum.Enum):
    Restaurant = 1
    supermarket = 2
    clothing = 3
    Furniture = 4
    sport = 5
    electronics = 6
    Other = 7


class business_info:

    def __init__(self, business_name, city, address, landline , type_code):
        self.Business_name = business_name
        self.City = city
        self.Address = address
        self.Landline  = landline
        self.Type_code = Business(type_code)

    def __str__(self):
        """
        function: Return a string of personal information
        :return: str : business_info
        """
        return f"\nBusiness info:\nBusiness name: {self.Business_name}\nCity: {self.City}\nAddress: {self.Address}\nPhone: {self.Landline}\nType: {self.Type_code.name}"
