import expense

def get_response():
    response = input("What would you like to enter today? Enter Number\n1 : Expense\n2 : Income\n ")
    return response


def get_expense_name():
    userexpensename = input("Please enter Expense Name\n")
    return userexpensename


def get_expense_amount():
    userexpenseamount = input("Please enter Expense Amount\n")
    return userexpenseamount


def get_income_name():
    userincomename = input("Please enter Income Name\n")
    return userincomename


def get_income_amount():
    userincomeamount = input("Please enter Income Amount\n")
    return userincomeamount


def decide_action(response):
    if response == str(1):
        name = get_expense_name()
    else:
        name = get_income_name()
    return name

def create_class(name,category):
     exp1 = expense.Expense(name,category)
     return exp1

def main():
    name = decide_action(get_response())
    print(name)
    category = input()
    exp = create_class(name, category)
    print ("Your Expense Name is {} ".format(exp.name))
    print ("your Category Name is {} ".format(exp.category) )



if __name__ == "__main__":
    main()
