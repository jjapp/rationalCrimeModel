from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation, BaseScheduler
from mesa.datacollection import DataCollector

import agent
from agent import House, Government

def get_total_savings(model):
    savings = [house.savings for house in model.schedule.agents]
    return sum(savings)

class BurglaryModel(Model):

    def __init__(self, width, height, income, savings_rate, n):
        self.width = width
        self.height = height
        self.income = income
        self.savings_rate = savings_rate
        self.n = n
        self.schedule = RandomActivation(self)
        self.gov_schedule = BaseScheduler(self)
        self.grid = MultiGrid(width, height, True)

        # place houses on grid.  One house per location
        for i in range(self.width):
            for j in range(self.height):
                num = str(i) + str(j)
                num = int(num)
                a = House(num, self, i, j, self.income, self.savings_rate, self.n)
                self.grid.place_agent(a, (a.x_point, a.y_point))
                self.schedule.add(a)

        # add government to schedule
        government = agent.Government(999, self)
        self.gov_schedule.add(government)

        # set up datacollection
        self.datacollector = DataCollector(
            model_reporters={"Total Savings" : get_total_savings}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()


if __name__=='__main__':
    model = BurglaryModel(10, 10, 100, 0.05, 1)
    for i in range(5):
        print (i)
        model.step()
    print (model.datacollector.get_model_vars_dataframe())
