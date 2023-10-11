def arithmetic_arranger(problems, solve=False):
 if len(problems)> 5:
  return "Error: Too many problems"
 
 arranged_problems=[]
 for problems in problems:
  num, operator, num2 = problems.split()
  if operator not in ('+','-'):
   return "Error: operator must be '+' or '-'"
  if not num.isdigit() or not num2.isdigit():
   return "Error: The numbers must only contain digits"
  if len(num) > 4 or len(num2) > 4:
   return "Error: The numbers cannto be more than four digits"
  
  width = max(len(num), len(num2)) + 2
  line  = f"{num:>{width}}"
  line2 = f"{operator} {num2:>{width-2}}"
  line3 = "-"*width
  
  if operator == "+":
   result = int(num) + int(num2)
  else:
   result = int(num) - int(num2)
  
  result_line = f"{result:>{width}}"
  
  arranged_problems.append((line,line2,line3,result_line))
  
 lines = ['    '.join(lines) for lines in zip(*arranged_problems)]
 
 return '\n'.join(lines)

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 4567"]
print(arithmetic_arranger(problems))
