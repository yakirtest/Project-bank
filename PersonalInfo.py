

class PersonalInfo:
    def __init__(self,name,id,phone_number,email):
        self.Name=name
        self.ID=id
        self.Phone_number=phone_number
        self.Email=email

    def __str__(self)->str:
        """
        function: Return a string of personal information
        :return:str : PersonalInfo
        """
        return f"PersonalInfo:\nname: {self.Name}\nID: {self.ID}\nphone number: {self.Phone_number}\nemail: {self.Email}"


