def daysinmonth(x):
   return (28 + (x + (x // 8)) % 2 + 2 % x + 2 * (1 // x))
