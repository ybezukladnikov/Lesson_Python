# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

revenue, cost = map(int,(input("Input revenue and cost between space: ").split()))

if revenue>cost:
    profit = revenue-cost
    print("Profit = ", profit)
    profitability = profit/revenue
    print("Profitability = ", profitability)
    num_of_employ = int(input("Input number of employ: "))
    print("Profit on 1 employ = ", profit/num_of_employ)

else: print("Loss = ", cost-revenue)