from monte.models.crf import ChainCrfLinear #ready-to-use models are in 
                                            #monte.models
from monte import train #trainers are in monte.train
from cores.features import *
import pickle 

file = open('crf.obj', 'r') 

mycrf = pickle.load(file)

predictions = mycrf.viterbi(createInput('cores/out1/0.out'))

print predictions