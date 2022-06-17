principal = int(input("Enter the principal: "))
time_period = int(input("Enter the time_period in years): "))
rate_of_interest = int(input("Enter the rate of interest (in %): "))

simple_interest = (principal * time_period * rate_of_interest) / 100
print(simple_interest)