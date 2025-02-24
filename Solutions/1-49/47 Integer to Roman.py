def unit(d):
  if d == '1':
    return "I"
  elif d == '2':
    return "II"
  elif d == '3':
    return "III"
  elif d == '4':
    return "IV"
  elif d == '5':
    return "V"
  elif d == '6':
    return "VI"
  elif d == '7':
    return "VII"
  elif d == '8':
    return "VIII"
  elif d == '9':
    return "IX"
  else:
    return ""

def ten(d):
  if d == '1':
    return "X"
  elif d == '2':
    return "XX"
  elif d == '3':
    return "XXX"
  elif d == '4':
    return "XL"
  elif d == '5':
    return "L"
  elif d == '6':
    return "LX"
  elif d == '7':
    return "LXX"
  elif d == '8':
    return "LXXX"
  elif d == '9':
    return "XC"
  else:
    return ""

def hundred(d):
  if d == '1':
    return "C"
  elif d == '2':
    return "CC"
  elif d == '3':
    return "CCC"
  elif d == '4':
    return "CD"
  elif d == '5':
    return "D"
  elif d == '6':
    return "DC"
  elif d == '7':
    return "DCC"
  elif d == '8':
    return "DCCC"
  elif d == '9':
    return "CM"
  else:
    return ""

def thousand(d):
  if d == '1':
    return "M"
  elif d == '2':
    return "MM"
  elif d == '3':
    return "MMM"
  else:
    return ""

def solve(num):
  digits = str(num)
  roman = ""
  if len(digits) - 1 >= 0:
    roman = unit(digits[len(digits) - 1]) + roman
  if len(digits) - 2 >= 0:
    roman = ten(digits[len(digits) - 2]) + roman
  if len(digits) - 3 >= 0:
    roman = hundred(digits[len(digits) - 3]) + roman
  if len(digits) - 4 >= 0:
    roman = thousand(digits[len(digits) - 4]) + roman
  return roman