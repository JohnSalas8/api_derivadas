import math
import ExpMath

class Differentiation:
    def __init__(self):
        pass

    def differentation_centralized (self, exp, x, h):
        """ exp -> Es f(x) de la integral
            x   -> Es el punto en el que se va evaluar
            h   -> Es el intervalo
        """
        expression = exp.replace(' ','')
        
        for i in ExpMath.exp_math:
            expression = expression.replace(i[0] , i[1])

        vjson = {}

        vjson['exp'] = exp
        vjson['x'] = x
        vjson['h'] = h

        if not len(expression):
            raise Exception('El tamanio de la expresion es cero.')
        else:
            vjson['procedure'] = []
            x = x+h
            new_exp = expression.replace('x','('+str(x)+')')
            f_xi1 = eval(new_exp)
            vjson['procedure'].append('f(' + str(x) + ') = ' + new_exp + ' = ' + str(f_xi1))

            x = x-2*h
            new_exp = expression.replace('x','('+str(x)+')')
            f_xi2 = eval(new_exp)
            vjson['procedure'].append('f(' + str(x) + ') = ' + new_exp + ' = ' + str(f_xi2))

            fp_xi = (f_xi1 - f_xi2) / (2*h)

            vjson['procedure'][0] = vjson['procedure'][0].replace('math.', '').replace('**', '^')
            vjson['procedure'][1] = vjson['procedure'][1].replace('**', '^').replace('math.', '')

            vjson['result'] = ''
            vjson['result'] += "f'(" + str(x+h) + ") = " + '('+ str(f_xi1) +' - ' + str(f_xi2) + ')/(2*'+ str(h) +') = ' + str(fp_xi)

            return vjson
        

if __name__ == '__main__':
    print Differentiation().differentation_centralized (
        'e^(-2*x+1) * cos(7*x-8) * (6*x^2-1)',
        1, 0.01
    )