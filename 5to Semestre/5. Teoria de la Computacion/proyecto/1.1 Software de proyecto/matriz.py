
class Matriz():
    #inicializador de los objetos
    def __init__(self):
        #lam = 0
        #num = ['0','1','2','3','4','5','6','7','8','9']
        #letMin = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        #Formato:  (Entrada, POP, PUSH, Sig. Estado)
        self.matriz = [
            [('lam','lam','#LLLLLLLLPPP',1)],#q0
            [('letMin','P','lam',1),('letMin','L','lam',1),('lam','L','lam',1),('.','lam','LLLLLLLLPPP',2)],#q1
            [('letMin','P','lam',2),('letMin','L','lam',2),('lam','L','lam',2),('lam','lam','NNN',3)],#q2
            [('num','N','lam',3),('@','#','lam',4)],#q3
            [('a','lam','lam',5)],#q4
            [('l','lam','lam',6)],#q5
            [('u','lam','lam',7)],#q6
            [('m','lam','lam',8)],#q7
            [('n','lam','lam',9)],#q8
            [('o','lam','lam',10)],#q9
            [('s','lam','lam',11)],#q10
            [('.','lam','lam',12)],#q11
            [('u','lam','lam',13)],#q12
            [('d','lam','lam',14)],#q13
            [('g','lam','lam',15)],#q14
            [('.','lam','lam',16)],#q15
            [('m','lam','lam',17)],#q16
            [('x','lam','lam',18)],#q17
            ['-']]#q18

