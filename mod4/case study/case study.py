import numpy as np
import statistics


revenue = np.array([14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50])
expenses = np.array([12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96])
months = np.array(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])

""" Profit for each month """

profit = revenue - expenses
print('profit:', +profit)

""" Profit after tax for each month (the tax rate is 30%)"""
tax_profit = profit - (profit * 30.00/100.00)
print('profit after tax', +tax_profit)

""" Profit margin for each month – equals to profit after tax divided by revenue """
profit_margin = tax_profit / revenue
profitMargin = [round((i * 100)) for i in profit_margin]
print(f'profit margin{profitMargin}')

""" Good months – where the profit after tax was greater than the mean for the year
Bad months – where the profit after tax was less than the mean for the year
"""
good_months = []
bad_months = []
mean_year = statistics.mean(profit)
for i in list((zip(months, tax_profit))):
    if mean_year < i[1]:
        good_months.append(i[0])
    else:
        bad_months.append(i[0])
print(f'good months{good_months}')
print(f'bad months{bad_months}')

""" The best month – where the profit after tax was max for the year
7. The worst month – where the profit after tax was min for the year. """

best_months = []
worst_months = []
for i in list(zip(months, profit)):
    if i[1] == max(profit):
        best_months.append(i[0])
    elif i[1] == min(profit):
        worst_months.append(i[0])

print(f'good months{best_months}')
print(f'worst months{worst_months}')





