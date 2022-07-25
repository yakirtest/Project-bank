

class BankAccount:
    """
    @Basic account
    """
    def __init__(self, personalinfo, balance: float = 0, line_of_credit:int = 0):
        self.Personalinfo = personalinfo
        self.Balance = balance
        self.line_of_credit = line_of_credit

    @property
    def Line_of_credit(self) -> int:
        """
        function: get line of credit
        :return: int: line_of_credit
        """
        return self.line_of_credit

    @Line_of_credit.setter
    def Line_of_credit(self, line_of_credit: int):
        """
        function : updating line of credit
        (*cannot be negative)
        :param line_of_credit: line_of_credit
        :return: None
        """
        if line_of_credit.__ge__(0):
            self.line_of_credit = line_of_credit
        else:
            print(f"Line of credit cannot be negative\n line_of_credit:{line_of_credit}")

    def __str__(self) -> str:
        """
        function: Return a string of  BankAccount
        :return:str : BankAccount
        """
        return f"{self.Personalinfo.__str__()}\nBalance: {self.Balance}\nLine_of_credit: {self.Line_of_credit}"

    @staticmethod
    def commission(sum: int, percent: float) -> float:
        """
         function static method: Return the Total commission
        :param sum:int: sum of money
        :param percent:float: Commission percentage
        :return: float : Total commission
        """
        return (percent / 100) * sum

    @staticmethod
    def percent_C_W(sum: int):
        """
        function static method: returns the Commission withdrawal percentage
        Depends on the amount of money
        :param sum:int:sum of money
        :return:float:Commission withdrawal percentage
        """
        commissions = {"1000": 1.5, "5000": 3, "10000": 4.5, "50000": 10, "100000": 13.5}
        for commission, percent in commissions.items():
            if sum.__le__(int(commission)):
                return percent
        return 13.5

    @staticmethod
    def percent_C_D(sum: int) -> float:
        """
        function static method: returns the Commission Deposit percentage
        Depends on the amount of money
        :param sum:int:sum of money
        :return:float:Commission Deposit percentage
        """
        commissions = {"1000": 0.5, "5000": 1, "10000": 1.5, "50000": 2.5, "100000": 3}
        for commission, percent in commissions.items():
            if sum.__le__(int(commission)):
                return percent
        return 3

    def Withdraw(self, sum: int):
        """
        function: withdraw money from the account
        (*sum must be greater than 0)
        :param sum:int :sum of money
        :return:None
        """
        if sum > 0:
            commis = self.commission(sum, self.percent_C_W(sum))
            if -abs(self.Line_of_credit) <= self.Balance - sum - commis:
                self.Balance -= (sum - commis)
            else:
                print(f"The requested amount cannot be withdrawn\nBalance: {self.Balance}")
        else:
            print(f"Invalid withdrawal amount\n Sum:{sum}")

    def Deposit(self, sum):
        """
        function: Deposit money into the account
        (*sum must be greater than 0)
        :param sum:int :sum of money
        :return:None
        """
        if sum > 0:
            self.Balance += sum - self.commission(sum, self.percent_C_D(sum))
        else:
            print(f"Invalid deposit amount\n Sum:{sum}")
