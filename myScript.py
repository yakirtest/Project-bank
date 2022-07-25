import sys
from Bank import *

if __name__ == '__main__':
    Accounts=Bank(Bank.load_and_parse_init_data(sys.argv[1]))
    # Accounts = Bank(Bank.load_and_parse_init_data())
    Basic_account = BankAccount(PersonalInfo("Moshe Cohen", "2453628123", "0563-263547", "Moshe_Cohen@gmail.com"), 0,3000)
    Student_account = StudentBankAccount("Shankar",PersonalInfo("Lihi Moshe", "1234325678", "0547-789654", "Lihi_Moshe@gmail.com"))
    Business_account = BusinessBankAccount(business_info("Thomas","Haifa","Herzl 58","07-8987654",7), PersonalInfo("Tomer Levy", "7694563457", "0558-654654","Tomer_Levy@gmail.com"),0,30000)
    print("~"*10,"Adding accounts","~"*40)
    Accounts.add_new_account(Basic_account)
    Accounts.add_new_account(Student_account)
    Accounts.add_new_account(Business_account)
    print(Accounts)#function Accounts.__str__()

    print("~"*10,"Delete account","~"*40)
    Accounts.delete_by_userID("2453628123")#Delete account Moshe Cohen
    print(Accounts)#function Accounts.__str__()

    print("~"*10,"Deposit account", "~" * 40)
    Accounts.Deposit("7694563457",10000)  # Deposit account Tomer Levy
    Accounts.print_id("7694563457")

    print("Withdraw", "~" * 40)
    Accounts.Withdraw("7694563457",500)  # Withdraw account Tomer Levy
    Accounts.print_id("7694563457")

    print("statistics", "~" * 40)
    avg, med, percent90, percent10=Accounts.calc_balance_statistics()
    print(f"average:{avg}\n")
    print(f"median:{med}\n")
    print(f"percent 90:{percent90}\n")
    print(f"percent10:{percent10}\n")







    # print(accs)

    # if len(sys.argv)==2:
    #     bank_branch=Bank(Bank.load_and_parse_init_data(sys.argv[1]))
    #     print(bank_branch)
    #
    # else:
    #     sys.exit(Red("Error You must submit two arguments"
    #                  "\n 2 arguments [-f] and path of a file .txt"))
    #
