import numpy as np
import matplotlib.pyplot as plt
import os
from jaratoolbox import loadbehavior
from jaratoolbox import behavioranalysis
from jaratoolbox import extraplots

subject = 'sole017'
paradigm = '2afc'
session = '20231106a'

behavFile = loadbehavior.path_to_behavior_data(subject, paradigm, session)
bdata = loadbehavior.BehaviorData(behavFile)


validTrials = bdata['valid'].astype(bool)
rightwardChoice = bdata['choice']==bdata.labels['choice']['right']
targetParamValue = bdata['targetFrequency']
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
titleStr = f'{subject}: {session}'
plt.title(titleStr, fontsize=fontSizeLabels, fontweight='bold')

plt.show()
