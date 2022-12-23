print("Please enter your student yearly budget ")
x = int(input())
print("Calculating Student Monthly expenses")

monthly_budget = x / 12
print("Your Student monthly budget is ", '\n', monthly_budget.__int__(),"$")

needs = monthly_budget * 0.5
print("Money that should be spent on needs per month is  ", '\n', needs.__int__(),"$")

wants = monthly_budget * 0.3
print("Money that should be spent on personal buyings per month is ", '\n', wants.__int__(),"$")

savings = monthly_budget * 0.2
print("Money that should be saved per month is ", '\n', savings.__int__(),"$")
