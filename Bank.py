import xml.etree.ElementTree as et
import statistics
from PersonalInfo import *
from StudentBank import *
from business_info import *
from BusinessBankAccount import *
from Validate_parameters import *


class Bank:
    """
    @Bank Branch
    """

    def __init__(self, customers: dict):
        self.Customers = customers

    @staticmethod
    def Creat_PersonalInfo(p_Info) -> (bool,PersonalInfo):
        """
        function static method:generates a Personal Info
        :param p_Info : xml.etree.ElementTree.Element
        :return:PersonalInfo:Personal Info
        """
        if validate_parameters.Validation_PersonalInfo(p_Info[0].text, p_Info[1].text, p_Info[2].text, p_Info[3].text):
            return True, PersonalInfo(p_Info[0].text, p_Info[1].text, p_Info[2].text, p_Info[3].text)
        else:
            print("PersonalInfo Not verified!")

    @staticmethod
    def Creat_acc_student(students: list) -> dict:
        """
        function static method:generates a dictionary of Student account
        (Key:ID, value:student account object )
        :param students:list:'xml.etree.ElementTree.Element'
        :return:dict: (Key:ID, value:student account object )
        """
        lis_stu = dict()
        for stu in students:
            Vp_i, p_i = Bank.Creat_PersonalInfo(stu[0])
            coll=validate_parameters.Validation_college(stu[3].text)
            bla = validate_parameters.Validation_balance(float(stu[1].text))
            if Vp_i and coll and bla:
                lis_stu[stu[0][1].text] = StudentBankAccount(stu[3].text, p_i,float(stu[1].text))
        return lis_stu

    @staticmethod
    def Creat_business_info(b_Info) ->(bool, business_info):
        """
        function static method:generates a Business  Info
        :param b_Info : xml.etree.ElementTree.Element
        :return:business_info:business_info
        """
        if validate_parameters.Validation_business_info(b_Info[0].text, b_Info[1].text, b_Info[2].text, b_Info[3].text,
                                                        int(b_Info[4].text)):
            return True,business_info(b_Info[0].text, b_Info[1].text, b_Info[2].text, b_Info[3].text, int(b_Info[4].text))
        else:
            print("business info Not verified!")

    @staticmethod
    def Creat_acc_business(business: list) -> dict:
        """
        function static method:generates a dictionary of Business account
        (Key:ID, value:Business account object )
        :param business:list:'xml.etree.ElementTree.Element'
        :return:dict: (Key:ID, value:Business account object )
        """
        lis_bus = dict()
        for bus in business:
            V_b_i,b_i = Bank.Creat_business_info(bus[3])
            Vp_i,p_i = Bank.Creat_PersonalInfo(bus[0])
            bla = validate_parameters.Validation_balance(float(bus[1].text))
            l_o_c = validate_parameters.Validation_line_of_credit(bus[2].text)
            if V_b_i and Vp_i and bla and l_o_c:
                lis_bus[bus[0][1].text] = BusinessBankAccount(b_i, p_i, float(bus[1].text), int(bus[2].text))
        return lis_bus

    @staticmethod
    def Creat_account(accounts: list) -> dict:
        """
        function static method:generates a dictionary of basic account
        (Key:ID, value: basic account object )
        :param accounts:list:'xml.etree.ElementTree.Element'
        :return:dict: (Key:ID, value:basic account object )
        """
        lis_acc = dict()
        for acc in accounts:
            Vp_i, p_i = Bank.Creat_PersonalInfo(acc[0])
            bla = validate_parameters.Validation_balance(float(acc[1].text))
            l_o_c = validate_parameters.Validation_line_of_credit(acc[2].text)
            if Vp_i and bla and l_o_c:
                lis_acc[acc[0][1].text] = BankAccount(p_i, float(acc[1].text), int(acc[2].text))
        return lis_acc

    @staticmethod
    def load_and_parse_init_data(argument: str) -> dict:
        """
        function: Reads bills from an XML file
        :param argument:
        :return:dict: (Key:ID, value:basic account object )
        """
        listbank = dict()
        xml = et.parse("init.xml")
        accounts = xml.getroot()
        account = accounts.findall('account[@type="BankAccount"]')
        listbank.update(Bank.Creat_account(account))
        acc_students = accounts.findall('account[@type="StudentBankAccount"]')
        listbank.update(Bank.Creat_acc_student(acc_students))
        acc_business = accounts.findall('account[@type="BusinessBankAccount"]')
        listbank.update(Bank.Creat_acc_business(acc_business))
        return listbank

    def add_new_account(self, new_account) -> None:
        """
        function: Add a new account
        :param new_account:BankAccount/StudentBankAccount/BusinessBankAccount: account
        :return:None
        """
        self.Customers.update({new_account.Personalinfo.ID: new_account})

    def delete_by_userID(self, id: str) -> None:
        """
        function: Account deletion by ID
        :param id: str:Customer id
        :return:None
        """
        try:
            del self.Customers[id]
        except:
            print(f"ID {id} is Not found in Accounts.")

    def Withdraw(self, id: str, sum: int) -> None:
        """
        function:Withdrawal from account by ID
        :param id:str:Customer id
        :param sum: int:  sum of money
        :return:None
        """
        try:
            self.Customers.get(id).Withdraw(sum)
        except:
            print(f"ID {id} is Not found in Accounts.")

    def Deposit(self, id: str, sum: int) -> None:
        """
        function:Deposit to account by ID
        :param id: str:Customer id
        :param sum: int:  sum of money
        :return:None
        """
        try:
            self.Customers.get(id).Deposit(sum)
        except:
            print(f"ID {id} is Not found in Accounts.")

    def calc_balance_statistics(self) -> tuple:
        """
        function : Returns the average, median, 90th percentile, 10th percentile
        of the balances of all customers
        :return:tuple: (float:avg, float: med, flot:percent90,float: percent10)
        """
        list_bal = list(map(lambda x: x.Balance, self.Customers.values()))
        sum1 = sum(list_bal)
        avg = statistics.mean(list_bal)
        med = statistics.median(list_bal)
        percent90 = (90 * sum1) / 100
        percent10 = (10 * sum1) / 100
        return avg, med, percent90, percent10

    @staticmethod
    def format(acc, typeacc: str) -> str:
        """
        function static method: Returns an account in row format
        :param acc:BankAccount/StudentBankAccount/BusinessBankAccount: Account
        :param typeacc:str: account type
        :return:str: account in row format
        """
        return f"{typeacc} " + " |".join(acc.__str__().split("\n")) + "\n" + "-" * 150 + "\n"

    def __str__(self):
        """
        function: Return a string of  all Accounts
        :return:str : all Accounts
        """
        list_accounts = list(map(lambda x: x, self.Customers.values()))
        grid = "A list of all customers:" + "\n" + "-" * 150 + "\n"
        for acc in list_accounts:
            if isinstance(acc, StudentBankAccount):
                grid += self.format(acc, "StudentAccount:")
            elif isinstance(acc, BusinessBankAccount):
                grid += self.format(acc, "BusinessAccount:")
            else:
                grid += self.format(acc, "BasicAccount:")
        return grid

    def print_id(self,id:str)->None:
        """
        printing Bank Account  with ID
        :param id:
        :return:
        """
        try:
            print(self.Customers.get(id))
        except:
            print(f"ID {id} is Not found in Accounts.")

