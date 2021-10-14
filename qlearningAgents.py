# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"
        # El Q-valor tiene que hacer referencia a un par estado-acción, con lo que es mejor que sea un diccionario
        # En el diccionario, el par (estado, acción) será la "key" que relacionará el Q-valor.
        self.qValue = util.Counter()  # Hay que ponerlos todos a 0, por eso uso el Counter, que es un diccionario "mejorado"

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        return self.qValue[(state, action)]  # Devuelve el valor relacionado con esta clave
        # util.raiseNotDefined()


    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"

        legalActions = self.getLegalActions(state)  # Cogemos una lista de todas las posibles acciones legales
        if not legalActions:  # Si está vacía...
            return 0.0  # ...devolvemos 0.0
        values = []  # Inicializamos una lista vacía para poner los q-valores

        for action in legalActions:  # Para cada acción posible en ese estado...
            values.append(self.getQValue(state, action))  # ...añadimos su q-valor a la lista
        return max(values)  # Devolvemos el máximo de esa lista, el mejor q-valor

        # util.raiseNotDefined()

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        legalActions = self.getLegalActions(state)  # Cogemos una lista de todas las posibles acciones legales
        qValues = []  # Inicializo una lista de q-valores
        maxValues = []  # Inicializo otra lista para guardar los máximos (puede ser que haya un "empate")
        if not legalActions:  # Si no hay acciones legales devolvemos None
            return None

        for action in legalActions:
            qValues.append((self.getQValue(state,action), action)) # Creo una lista con todos los qValues
        # He descubierto que el máximo de python para una lista de n-tuplas (de valores enteros o reales)
        # realiza el máximo de la primera componente de cada n-tupla, que es lo que a mí me interesa
        maxValue = max(qValues)  # Me quedo con el máximo, pero puede haber más de uno!!
        for va in qValues:  # Voy a ver si hay más valores que sean el máximo
            if va[0] == maxValue[0]:  # Atención porque son tuplas (valor, acción)
                maxValues.append(va)  # Añadiré aquí todos los valores máximos, y después escogeré uno aleatoriamente
        bestValueAction = random.choice(maxValues) # Escojo un valor random de los máximos
        return bestValueAction[1]  # Quiero que me dé la acción, el q-valor me da igual.

        # util.raiseNotDefined()

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)

          flipCoin este es:
            def flipCoin(p):
                r = random.random()
                return r < p

          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        "*** YOUR CODE HERE ***"
        if not legalActions:
            return None
        # Ahora tenemos que escoger una acción random si la probabilidad es menor que epsilon, es decir, "exploramos"
        if flipCoin(self.epsilon):  # Esto devuelve True si es menor y entrará
            return random.choice(legalActions)  # Devolvemos una acción aleatoria de las legales
        else:  # Esto significa que la probabilidad es mayor que epsilon y por tanto tenemos que "explotar"
            return self.getPolicy(state)
        # util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        # Las fórmulas son:
        # sample = R(s,a,s') + \gamma \max_{a} Q(s',a')
        # Q(s,a) <-- (1-\alpha)Q(s,a)+\alpha * sample
        sample = reward + self.discount * self.getValue(nextState)
        self.qValue[(state, action)] = (1-self.alpha) * self.getQValue(state, action) + self.alpha * sample
        # util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
