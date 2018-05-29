import math

expression = ''

def differentation_to_right (exp, x, h):
    """ exp -> Es f(x) de la integral
        x   -> Es el punto en el que se va evaluar
        h   -> Es el intervalo
    """
    expression = exp.replace(' ','')

    if not len(expression):
        raise Exception('El tamanio de la expresion es cero.')
    else:
        new_exp = expression.replace('x','('+str(x)+')')
        f_xi = eval(new_exp)
        print 'f('+str(x)+') =', new_exp, '=', f_xi

        x = x+h
        new_exp = expression.replace('x','('+str(x)+')')
        f_xi1 = eval(new_exp)
        print 'f('+str(x)+') =', new_exp, '=', f_xi1

        x = x+h
        new_exp = expression.replace('x','('+str(x)+')')
        f_xi2 = eval(new_exp)
        print 'f('+str(x)+') =', new_exp, '=', f_xi2

        fp_xi = (-f_xi2 + 4*f_xi1 -3*f_xi) / (2*h)

        print ''
        print "f'("+str(x-h*2)+") =", fp_xi

def main():
    exp = 'math.e**(-2*x+1) * math.cos(7*x-8) * (6*x**2-1)'
    differentation_to_right(exp, 1, 0.01)

if __name__ == '__main__':
    main()