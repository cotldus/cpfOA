# cpfOA
Simple CPFOA calculator given salary and years

# Run
From command line run
```
python3 cpfOA.py
```

Or from Python3 REPL, for salary $2000 and 10 years saved:

```
from cpfOA import cpf as cpf
cpf(2000, 10)
```

# Assumptions
CPF OA 
- personal contribution of 20%
- employer contribution of 3%

CPF OA interest rate at 2.5%

30 days in a month.

# Note

Salary allows floating number.
Years take in whole number.
Salary is set to $6000 for amounts above $6000 to account for contribution limit.

