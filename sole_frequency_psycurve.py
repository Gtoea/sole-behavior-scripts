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
from matplotlib.ticker import ScalarFormatter

subject = 'sole028'
paradigm = '2afc'
sessions = ['20240315a','20240317a','20240319a']

bdata = behavioranalysis.load_many_sessions(subject, paradigm=paradigm, sessions=sessions)
nSessions = bdata['sessionID'][-1]

choice = bdata['choice']
choiceRight = (choice==bdata.labels['choice']['right'])
targetFrequency = bdata['targetFrequency']
valid = bdata['valid'] & (choice!=bdata.labels['choice']['none'])

(possibleValues,fractionHitsEachValue,ciHitsEachValue,nTrialsEachValue,nHitsEachValue) = behavioranalysis.calculate_psychometric(choiceRight,targetFrequency,valid)

fontSizeLabels = 12
(pline, pcaps, pbars, pdots) = extraplots.plot_psychometric(possibleValues,fractionHitsEachValue,ciHitsEachValue)

plt.xscale('log')
plt.ylim([0,105])
plt.ylabel('Rightward trials (%)',fontsize=fontSizeLabels)
plt.xlabel('Frequency (Hz)',fontsize=fontSizeLabels)
plt.title('{0} {1}'.format(subject,sessions))
plt.show()
