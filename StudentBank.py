from BankAccount import *


class StudentBankAccount(BankAccount):
    """
    @Student account
    """

    def __init__(self, college_Name: str, personalinfo, balance: float = 0):
        super().__init__(personalinfo, balance)
        self.college_name = college_Name

    @property
    def Line_of_credit(self) -> int:
        """
        function: get line of credit
        :return: int: line_of_credit
        """
        return self.line_of_credit

    def __str__(self) -> str:
        """
        function: Return a string of  StudentBankAccount
        :return:str : StudentBankAccount
        """
        return f"{super().__str__()}\ncollege_name: {self.college_name}"
