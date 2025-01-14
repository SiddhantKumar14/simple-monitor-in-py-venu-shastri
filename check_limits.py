def print_func(input):
  print(input)
  
def is_temp_ok(temperature):
  if temperature > 0 and temperature < 45:
    return True
  else:
    return False
def is_soc_ok(soc):
  if soc > 20 and soc < 80:
    return True
  else:
    return False
def is_charge_rate_ok(charge_rate):
  if charge_rate < 0.8 and charge_rate > 0:
    return True
  else:
    return False
  
def battery_is_ok(temperature, soc, charge_rate):
  return is_temp_ok(temperature) and is_soc_ok(soc) and is_charge_rate_ok(charge_rate)


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
