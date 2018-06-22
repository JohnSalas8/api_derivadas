import math
import json
import ExpMath


class DifferentiationToRight:
    def __init__(self):
        pass
        

    def differentation_to_right (self, exp, x, h):
        """ exp -> Es f(x) de la integral
            x   -> Es el punto en el que se va evaluar
            h   -> Es el intervalo
        """
        expression = exp

        for i in ExpMath.exp_math:
            expression = expression.replace(i[0], i[1])

        vjson = {}

        vjson['exp'] = exp
        vjson['x'] = x
        vjson['h'] = h

        vjson['procedure'] = []

        vjson['result'] = ''

        if not len(expression):
            raise Exception('El tamanio de la expresion es cero.')
        else:
            new_exp = expression.replace('x','('+str(x)+')')
            f_xi = eval(new_exp)
            vjson['procedure'].append('f(' + str(x) + ') = ' + new_exp + ' = ' + str(f_xi))

            x = x+h
            new_exp = expression.replace('x','('+str(x)+')')
            f_xi1 = eval(new_exp)
            vjson['procedure'].append('f(' + str(x) + ') = ' + new_exp + ' = ' + str(f_xi1))

            x = x+h
            new_exp = expression.replace('x','('+str(x)+')')
            f_xi2 = eval(new_exp)
            vjson['procedure'].append('f(' + str(x) + ') = ' + new_exp + ' = ' + str(f_xi2))

            fp_xi = (-f_xi2 + 4*f_xi1 -3*f_xi) / (2*h)

            vjson['result'] += "f'(" + str(x-h*2) + ") = ( " + str(-f_xi2)  + ' + 4*' + str(f_xi1) + '- 3*' + str(f_xi) + ') / (' + '2*' + str(h) + ' ) = ' + str(fp_xi)

            vjson['procedure'][0] = vjson['procedure'][0].replace('math.', '').replace('**', '^')
            vjson['procedure'][1] = vjson['procedure'][1].replace('math.', '').replace('**', '^')
            vjson['procedure'][2] = vjson['procedure'][2].replace('math.', '').replace('**', '^')

            return vjson

def main():
    exp = 'math.e**(-2*x+1) * math.cos(7*x-8) * (6*x**2-1)'
    differentation_to_right(exp, 1, 0.01)

if __name__ == '__main__':
    main()