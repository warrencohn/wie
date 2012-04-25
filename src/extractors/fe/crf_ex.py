#Copyright (C) 2007 Roland Memisevic
#
#This program is distributed WITHOUT ANY WARRANTY; without even the implied 
#warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
#LICENSE file for more details.
#
#
#
#This example file shows how to build a simple model using monte, how to 
#train the model using the provided trainers, and how to apply the trained 
#model to some data.


from monte.models.crf import ChainCrfLinear #ready-to-use models are in 
                                            #monte.models
from monte import train #trainers are in monte.train
from cores.features import *
import pickle 

#Make a linear-chain CRF:
mycrf = ChainCrfLinear(6,9)

#Make a trainer (that does 5 steps per call), and register mycrf with it:
mytrainer = train.Conjugategradients(mycrf,5)

#Alternatively, we could have used one of these, for example:
#mytrainer = trainers.OnlinegradientNocost(mycrf,0.95,0.01)
#mytrainer = trainers.Bolddriver(mycrf,0.01)
#mytrainer = trainers.GradientdescentMomentum(mycrf,0.95,0.01)

#Produce some stupid toy data for training:
#inStr = ['+84083756321', '(84) 08 3645726', '08 3970465', '083876458', '453', '0343556765', '03435567656', '54 54 979529']
#cost = [0.001, 0.001, 0.001, 0.001, 0.001, 0.01, 0.001, 0.001]
#inputs = array([[numDigits(s), numDigitsMax(s)] for s in inStr])
#outputs = array([1, 1, 1, 1, 0, 1, 0, 0])

#Train the model. Since we have registered our model with this trainer, 
#calling the trainers step-method trains our model (for a number of steps):
t = [createTrainInput('cores/out/0.out'), createTrainInput('cores/out/1.out')]
for i in range(20):
    mytrainer.step(t,0.001)
    print mycrf.cost(t,0.001)

#Apply to some stupid test data:
#testInStr = ['+84083796321', '34356', '(84) 058 3645726', '08 3970765', '08386458', '453', '0343556765', '03435567656', '54 54 979529']
#testinputs = array([[numDigits(s), numDigitsMax(s)] for s in testInStr])

file = open('crf.obj', 'w') 
pickle.dump(mycrf, file) 

predictions = mycrf.viterbi(createInput('cores/out1/0.out'))

print predictions

