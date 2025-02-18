# python3 fractions_create_strings_long_denominator.py
import fractions

s = "1/" + ("2" * 80)
print(s)
f = fractions.Fraction(s)
print("{} = {}".format(s, f))
