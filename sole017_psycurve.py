import numpy as np
import matplotlib.pyplot as plt
import os
from jaratoolbox import loadbehavior
from jaratoolbox import behavioranalysis
from jaratoolbox import extraplots

subject = 'sole017'
paradigm = '2afc'
sessions = ['20231106a','20231107a','20231108a']

bdata = behavioranalysis.load_many_sessions(subject, paradigm=paradigm, sessions=sessions)
nSessions = bdata['sessionID'][-1]

validTrials = bdata['valid'].astype(bool)
rightwardChoice = bdata['choice']==bdata.labels['choice']['right']
targetParamValue = bdata['targetAMrate']
possibleParamValue = np.unique(targetParamValue)
nParamValues = len(possibleParamValue)

xTicks = [8, 16, 32] 
(possibleValues, fractionHitsEachValue, ciHitsEachValue, nTrialsEachValue, nHitsEachValue)=\
    behavioranalysis.calculate_psychometric(rightwardChoice, targetParamValue, validTrials)

plt.clf()
fontSizeLabels = 12
(pline, pcaps, pbars, pdots) = extraplots.plot_psychometric(possibleValues,fractionHitsEachValue,
                                                            ciHitsEachValue, xTicks=xTicks,
                                                            xscale='log')
plt.ylim([0,105])
plt.ylabel('Rightward choice (%)', fontsize=fontSizeLabels)
plt.xlabel('AM rate (Hz)', fontsize=fontSizeLabels)
titleStr = f'{subject}: {sessions}'
plt.title(titleStr, fontsize=fontSizeLabels, fontweight='bold')

plt.show()
