import random
import statistics
import matplotlib.pyplot as plt

# Business
user = int(input('how manny days would you like to look at? '))
business_value = 0
x = []
y = []
for day in range(user):
    x.append(day + 1)
    class Business:
        # the value of the investment
        def __init__(self,amount_invested,invested_list):
            global business_value
            # you
            self.amount_invested = round(amount_invested,2)
            # Business
            self.portfolio = round(statistics.mean(invested_list) / 100,2)
            self.business_value = business_value + amount_invested
            business_value = self.business_value
            self.average_price = statistics.mean(invested_list)
            self.shares = round(random.uniform(0,1),7)
            # value
            self.value = self.business_value

    # Investor
    value_list = [0]
    def Investor():
        global value_list
        # chance of the Investor investing
        R_Investor_choise = random.betavariate(1,2)
        if R_Investor_choise <= 0.10:
            # if zero loss value
            take_away = Business(0, [0])
            take = round(random.uniform(-take_away.value, 0), 2)
            value_list = take
            investor = Business(take, [value_list])
            print('investor removed', take)
        else:
            # iif not zero gain value
            spend = round(random.uniform(0, 99), 2)
            value_list = spend
            investor = Business(spend, [value_list])
            # print('the value of the investment is ${:.2f}'.format(investor.value))
            print('amount invested ${:.2f}'.format(investor.amount_invested))
            # print('portfolio {}%'.format(investor.portfolio))
            # print('average price ${:.2f}'.format(investor.average_price))
            # print('shares {:.7f}'.format(investor.shares))

    Investor()
    # Business graph
    # name
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    name = ''
    for _ in range(3):
        name += random.choice(abc)
    # labels
    plt.title('Business name: ' + name.upper())
    plt.xlabel('day')
    # x and y
    x = x
    y_find = Business(0,[1])
    y.append(y_find.value)
    plt.plot(x, y)
#  show
plt.show()