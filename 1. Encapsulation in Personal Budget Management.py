
## Task 1: Define Budget Category Class
class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.__name = name 
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

## Task 2: Getters and setters for category name and budget
    def get_name(self):
        return self.__name
    def get_allocated_bugget(self):
        return self.__allocated_budget
    def get_remaining_buget(self):
        return self.__remaining_budget
    
    def set_name(self, name):
        if name:
            self.__name = name

    def set_allocated_budget(self, budget):
        if budget > 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget
        else:
            raise ValueError ("Budget must be positive")
        
## Task 3: Add Budget Functionality
        
    def add_expense(self, amount):
        if amount > 0 and amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
        else:
            raise ValueError (" Invalid expense amount")
## Task 4: Display Budget Details        

    def display_category_summary(self):
       print(f"Category: {self.__name}")
       print(f"Allocated Budget: {self.__allocated_budget}")
       print(f"Remaining Budget: {self.__remaining_budget}")
        

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()