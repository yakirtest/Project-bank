from BankAccount import *


class BusinessBankAccount(BankAccount):
    """
     @Business account
    """

    def __init__(self, business_info, personalinfo, balance: float = 0, line_of_credit: int = 0):
        super().__init__(personalinfo, balance, line_of_credit)
        self.business_info = business_info

    def __str__(self) -> str:
        """
        function: Return a string of  BusinessBankAccount
        :return:str : BusinessBankAccount
        """
        return f"{super().__str__()}{self.business_info.__str__()}"

    @staticmethod
    def commission(sum: int, percent: float) -> float:
        """
        function static method: Return the Total commission for a business account
        (150% more than the commission in the basic account)
        :param sum:int: sum of money
        :param percent:float: Commission percentage
        :return:float : Total commission
        """
        percent = (150 * percent) / 100
        return (percent / 100) * sum
