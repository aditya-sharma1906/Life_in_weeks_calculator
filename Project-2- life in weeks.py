age=input("what is your current age?")
age_in_years=int(age)
years_remaining=90-age_in_years
days_remaining=years_remaining*365
months_remaining=years_remaining*12
weeks_remaining=years_remaining*52
message=f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months"
print(message)