# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0.2
    return answerDiscount, answerNoise

def question3a():
    answerDiscount = None
    answerNoise = None
    answerLivingReward = None
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    answerDiscount = None
    answerNoise = None
    answerLivingReward = None
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    answerDiscount = None
    answerNoise = None
    answerLivingReward = None
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    answerDiscount = None
    answerNoise = None
    answerLivingReward = None
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    answerDiscount = None
    answerNoise = None
    answerLivingReward = None
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    answerEpsilon = None
    answerLearningRate = None
    """
        Es imposible. Pongamos e = 'epsilon' para simplificar.
        La probabilidad de que el agente tome una acci??n aleatoria es e. Pongamos que hay la misma probabilidad
        de que el agente escoja 'up', 'down', 'east' o 'west' cuando escoge una aleatoria. Entonces tendremos
        que la probabilidad de que el agente se mueva a la derecha es de 0.25e. As?? pues, como los eventos
        "escoger si lo hacemos aleatoriamente o no" son independientes, podemos concluir que la probabilidad de
        que el agente se mueva a la derecha n veces seguidas es de:
                                                    (0.25e)^n = (0.25)^n * e^n
        con lo que, si n es grande, es un n??mero muy bajo. As?? pues es bastante complicado que, aunque se suba
        la e hasta 1, ya que (0.25)^n, si n es grande, se hace peque??o muy r??pidamente. En nuestro caso, el
        n??mero de casillas que deber??a hacer hacia la derecha es de 5, con lo que la probabilidad de que con e=1
        vaya directamente hacia la derecha hasta la ??ltima casilla es de 1/1024 = 0.0009765625, pr??cticamente imposible.
        
        Ahora bien, tiene en total 50 intentos para realizarlo, no hace falta que lo haga en 5, as?? que esta
        probabilidad aumenta. Aun as??, la probabilidad es tan baja que a la m??nima que descubra la casilla de +1, ir??
        siempre a por ella, por muy alta que sea la e y por muy baja que sea la alpha, porque es mucho m??s probable que
        acabe ah?? y por tanto aprenda de ello y vaya siempre ah??, y aunque explore, necesita much??sima suerte para
        poder llegar a la casilla del +5.
        
        Para que eso pudiese ser posible, habr??a que empezar a ejecutar con una e muy alta, de forma que explorase lo
        m??ximo posible, y cuando hubiese explorado la casilla del +5, bajar much??simo la e, de forma que vaya por
        los caminos aprendidos y as?? ir??a m??s veces a la de +5. Esto no es posible puesto que la e y la alpha son 
        par??metros fijos durante toda la ejecuci??n.
    """
    return 'NOT POSSIBLE'

    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
