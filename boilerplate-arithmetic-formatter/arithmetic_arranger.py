def arithmetic_arranger(problems, calculate=False):
  if len(problems) > 5:
    return "Error: Too many problems."
    
  arranged_problems = ""
  
  incorrect_operator = ["/", "*"]

  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  
  for problem in problems:
    parts = problem.split(" ")

    # After split, naming variables for better logic
    operand1 = parts[0]
    operator = parts[1]
    operand2 = parts[2]

    # Checks for incorrect operator
    if operator in incorrect_operator:
      return "Error: Operator must be '+' or '-'."

    # Checks for numbers only
    if not operand1.isdecimal() or not operand2.isdecimal():  
      return "Error: Numbers must only contain digits."

    # Checks for maximum 
    if len(parts[0]) > 4 or len(parts[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Adding four spaces only when needed
    if line1 != "":
      line1 += "    "
      line2 += "    "
      line3 += "    "
      line4 += "    "

    # When the first operand is the longest string
    if len(operand1) > len(operand2):
      line_length = len(operand1) + 2 
      line1 += "  " + operand1
      line2 += operator + " " * (line_length - len(operand2) - 1) + operand2
      line3 += "-" * line_length

      # Only run when calculate is true
      if calculate:
        if operator == "+":
          sum = int(operand1) + int(operand2)
          sum_text = str(sum)
          line4 += " " * (line_length - len(sum_text)) + sum_text
        else:
          sum = int(operand1) - int(operand2)
          sum_text = str(sum)
          line4 += " " * (line_length - len(sum_text)) + sum_text

    # When operands are equal or second one is longer
    else:
      line_length = len(operand2) + 2 
      line1 += (" " * (line_length - len(operand1))) + operand1
      line2 += operator + (" " * (line_length - len(operand2) - 1)) + operand2
      line3 += "-" * line_length

      # Only run when calculate is true
      if calculate:
        if operator == "+":
          sum = int(operand1) + int(operand2)
          sum_text = str(sum)
          line4 += " " * (line_length - len(sum_text)) + sum_text
        else:
          sum = int(operand1) - int(operand2)
          sum_text = str(sum)
          line4 += " " * (line_length - len(sum_text)) + sum_text
      


  arranged_problems += line1 + "\n" + line2 + "\n" + line3
  if calculate:
    arranged_problems += "\n" + line4
  return arranged_problems