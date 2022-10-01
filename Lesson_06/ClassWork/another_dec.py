text = "5+8/4*3+5"

dict_op = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y,
           }

for oper in dict_op:
    text = text.replace(oper, f'#{oper}#')

terms  = text.split('#')

print(terms)