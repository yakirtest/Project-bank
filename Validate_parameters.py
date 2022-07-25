import re


class validate_parameters:

    @staticmethod
    def Validation_PersonalInfo(name: str, id: str, phone_number: str, email: str) -> bool:
        """
        Validates a parameter PersonalInfo
        :param name: str:name
        :param id: str:id
        :param phone_number: str:phone_number
        :param email: str:email
        :return: bool
        """
        bo = True
        if not validate_parameters.Validation_name(name):
            print("PersonalInfo.name Not verified!")
            bo = False
        if not validate_parameters.Validation_id(id):
            print("PersonalInfo.id Not verified!")
            bo = False
        if not validate_parameters.Validation_phone(phone_number):
            print("PersonalInfo.Phone_number Not verified!")
            bo = False
        if not validate_parameters.Validation_email(email):
            print("PersonalInfo.email Not verified!")
            bo = False
        return bo

    @staticmethod
    def Validation_business_info(business_name: str, city: str, address: str, landline: str, type_code: int) -> bool:
        """
        Validates a parameter business_info
        :param business_name: str:business_name
        :param city: str:city
        :param address: str:address
        :param landline: str:landline
        :param type_code: int:name
        :return: bool
        """
        bo = True
        if not validate_parameters.Validation_businessName(business_name):
            print("business_info.business_name Not verified!")
            bo = False
        if not validate_parameters.Validation_city(city):
            print("business_info.city Not verified!")
            bo = False
        if not validate_parameters.Validation_address(address):
            print("business_info.address Not verified!")
            bo = False
        if not validate_parameters.Validation_landline(landline):
            print("business_info.type_code Not verified!")
            bo = False
            if not validate_parameters.Validation_typeCode(type_code):
                print("business_info.type_code Not verified!")
                bo = False
        return bo

    @staticmethod
    def Validation_name(name: str) -> bool:
        """
        Validates a parameter name
        :param name: str:name
        :return: bool
        """
        pattern = '^[a-zA-Z\s]{,30}$'
        if re.match(pattern, name):
            return True
        return False

    @staticmethod
    def Validation_id(id:str) -> bool:
        """
        Validates a parameter id
        :param id: str:id
        :return: bool
        """
        pattern = '^[0-9]{10}$'
        if re.match(pattern, id):
            return True
        return False

    @staticmethod
    def Validation_phone(phone: str) -> bool:
        """
        Validates a parameter phone
        :param phone: str:phone
        :return: bool
        """
        pattern = '^05\d\d-[\d]{6}$'
        if re.match(pattern, phone):
            return True
        return False

    @staticmethod
    def Validation_email(email: str) -> bool:
        """
        Validates a parameter email
        :param email: str:email
        :return: bool
        """
        pattern = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            return True
        return False

    @staticmethod
    def Validation_balance(balance: float) -> bool:
        """
        Validates a parameter balance
        :param balance: str:balance
        :return: bool
        """
        if type(balance) == float:
            return True
        return False

    @staticmethod
    def Validation_line_of_credit(line_of_credit: str) -> bool:
        """
        Validates a parameter line_of_credit
        :param line_of_credit: str:line_of_credit
        :return: bool
        """
        pattern = '^[0-9]+$'
        if re.match(pattern, line_of_credit):
            return True
        return False

    @staticmethod
    def Validation_college(college: str) -> bool:
        """
        Validates a parameter college
        :param college: str:college
        :return: bool
        """
        pattern = '^[a-zA-Z\s]{,30}$'
        if re.match(pattern, college):
            return True
        return False

    @staticmethod
    def Validation_businessName(businessName: str) -> bool:
        """
        Validates a parameter businessName
        :param businessName: str:businessName
        :return: bool
        """
        pattern = '^[a-zA-Z\s]{,30}$'
        if re.match(pattern, businessName):
            return True
        return False

    @staticmethod
    def Validation_city(city: str) -> bool:
        """
        Validates a parameter city
        :param city: str:city
        :return: bool
        """
        pattern = '^[a-zA-Z\s]{,30}'
        if re.match(pattern, city):
            return True
        return False

    @staticmethod
    def Validation_address(address: str) -> bool:
        """
        Validates a parameter address
        :param address: str:address
        :return: bool
        """
        pattern = '^[a-zA-Z\s]+\s+[0-9]+$'
        if re.match(pattern, address):
            return True
        return False

    @staticmethod
    def Validation_typeCode(typeCode: int) -> bool:
        """
        Validates a parameter typeCode
        :param typeCode: int:typeCode
        :return: bool
        """
        return typeCode > 0 and typeCode < 8

    @staticmethod
    def Validation_landline(landline: str) -> bool:
        """
        Validates a parameter landline
        :param landline: str:landline
        :return: bool
        """
        pattern = '^0\d-[\d]{7}$'
        if re.match(pattern, landline):
            return True
        return False
