# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

revenue, cost = map(int,(input("Input revenue and cost between space: ").split()))

if revenue>cost: print("Profit = ", revenue-cost)
else: print("Loss = ", cost-revenue)