import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from jaratoolbox import settings
from jaratoolbox import loadbehavior
from jaratoolbox import behavioranalysis
from jaratoolbox import extraplots
from jaratoolbox import extrastats


subject = 'sole017'
paradigm = '2afc'
sessions = '20231121a'

behavFile = loadbehavior.path_to_behavior_data(subject,paradigm,sessions)
bdata = loadbehavior.BehaviorData(behavFile)

choice = bdata['choice']
choiceRight = (choice==bdata.labels['choice']['right'])
targetFrequency = bdata['targetFrequency']
valid = bdata['valid'] & (choice!=bdata.labels['choice']['none'])

(possibleValues,fractionHitsEachValue,ciHitsEachValue,nTrialsEachValue,nHitsEachValue) = behavioranalysis.calculate_psychometric(choiceRight,targetFrequency,valid)

plt.clf()
(pline, pcaps, pbars, pdots) = extraplots.plot_psychometric(possibleValues,fractionHitsEachValue,ciHitsEachValue)

plt.ylabel('Rightward trials (%)')
plt.xlabel('Frequency (Hz)')
plt.title('{0} [{1}]'.format(subject,sessions))
plt.show()

