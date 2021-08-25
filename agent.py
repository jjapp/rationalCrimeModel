from mesa import Agent


class House(Agent):
    """An agent representing a home in the crime model grid
    x_point gives the x coordinate for the home
    y_point gives the y coordinate for the home
    savings rate determines how much of each period's income is saved
    n is used to determine the shape of the utility function.  The model assumes an iso-elastic utility model.
        -n must be greater than or equal to zero
        -n mus be less than or equal to 1
        -if n is one the model uses a log utility function
    savings: default is none.  Gives total savings level for home"""

    def __init__(self, unique_id, model, x_point, y_point, income, savings_rate, n, savings=0):
        super().__init__(unique_id, model)
        self.x_point = x_point
        self.y_point = y_point
        self.income = income
        self.savings_rate = savings_rate
        self.n = n
        self.savings = savings

    def step(self):
        self.savings = self.savings + self.income * self.savings_rate


class Government(Agent):
    def __init__(self, unique_id, model, police=None, fine=None):
        super().__init__(unique_id, model)
        self.police = police
        self.fine = fine




