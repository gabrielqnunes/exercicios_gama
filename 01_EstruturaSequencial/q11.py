from stringprep import in_table_c11_c12


int1 = int(input('Insert the first integer: '))
int2 = int(input('Insert the second integer: '))
float1 = float(input('Insert the float number: '))

def CalculateA(numeric1, numeric2):
    return (numeric1 * 2) * (numeric2 / 2)

def CalculateB(numeric1, numeric2):
    return (numeric1 * 3) + numeric2

print(CalculateA(int1,int2), CalculateB(int1, float1), float1**3)