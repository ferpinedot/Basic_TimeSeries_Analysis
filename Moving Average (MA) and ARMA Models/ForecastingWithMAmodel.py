# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:11:17 2020

@author: User


Forecasting with MA Model

As you did with AR models, you will use MA models to forecast in-sample and 
out-of-sample data using statsmodels.

For the simulated series simulated_data_1 with θ=−0.9, you will plot in-sample 
and out-of-sample forecasts. One big difference you will see between 
out-of-sample forecasts with an MA(1) model and an AR(1) model is that the MA(1) 
forecasts more than one period in the future are simply the mean of the sample.

"""

# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA

import matplotlib.pyplot as plt

simulated_data_1 = ([-1.08563060e+00,  1.97441299e+00, -6.14632404e-01, -1.76097536e+00,
        7.77064991e-01,  2.17217676e+00, -3.91297213e+00,  1.75509869e+00,
        1.65195762e+00, -2.00608304e+00,  1.01180210e-01,  5.16288568e-01,
        1.57662770e+00, -1.98115266e+00,  1.31029837e-01, -3.47675119e-02,
        2.59684623e+00,  2.01449015e-01, -9.64053582e-01, -5.17462109e-01,
        3.89800817e-01,  8.27100310e-01, -2.27749269e+00,  2.01807953e+00,
       -2.31212681e+00,  4.90741099e-01,  1.48108155e+00, -2.24507538e+00,
        1.14574391e+00, -7.35693048e-01,  5.19960036e-01, -2.56853167e+00,
        7.47197090e-01,  8.94502559e-01,  1.55735194e+00, -1.00835187e+00,
        1.59118030e-01,  6.85661387e-01, -1.49893678e+00,  1.07521003e+00,
       -1.06063111e+00, -1.00283963e+00,  1.16400275e+00,  9.25615677e-01,
       -1.77836225e-01, -3.16560640e-01,  2.40301271e+00, -1.74021658e+00,
        6.07115062e-01,  1.35728093e+00, -3.30841433e+00,  1.25888581e-01,
        2.67862161e+00, -2.36740374e+00,  7.47939692e-01,  1.04260106e+00,
       -7.16779812e-02,  9.53250430e-01, -8.37534267e-02, -2.76687054e-01,
       -1.73516212e+00,  1.49030051e+00, -4.01104407e-01, -1.60911025e+00,
        2.61093796e+00, -4.68332607e-01, -6.81022800e-01, -2.74033134e-01,
       -9.88518290e-01,  1.27799510e+00,  2.88867453e-01, -1.25275019e+00,
        1.91024353e+00, -2.14318669e+00, -1.13561761e+00,  2.95051741e+00,
       -1.33912042e+00,  2.36999849e-01, -7.24090096e-01, -8.52197710e-01,
        2.70060386e+00, -1.81858262e+00,  2.28093457e+00, -6.87549053e-01,
       -1.04133551e+00, -8.02620069e-01,  2.44850174e-01, -5.53307343e-01,
        3.17838418e+00, -1.71396079e+00,  1.00220844e+00, -2.30253704e+00,
        1.32165197e+00,  1.01493032e+00, -1.39508651e+00,  1.33262414e+00,
       -2.01257093e+00, -3.87360424e-01,  1.60652500e+00, -7.20636985e-01,
        9.83313480e-01, -2.55573715e+00,  2.49236377e+00,  1.95726576e+00,
       -2.36309952e+00,  5.63055122e-02,  1.48821569e-01, -2.02357025e+00,
        2.10192478e+00, -1.98894172e+00,  1.01718917e+00,  1.62778119e+00,
       -1.85379955e+00,  1.16294425e+00,  5.61614963e-01, -6.32724292e-01,
       -1.62181524e+00,  9.01378348e-01,  2.25863909e+00, -3.78851597e+00,
        1.54675517e+00, -3.03900659e-01,  6.17644627e-01,  6.39542990e-01,
        9.35296913e-01, -1.71805426e+00,  1.05555048e+00, -2.31367052e-01,
        2.45811675e-02, -9.90836500e-01, -4.89789930e-01, -2.02453791e-01,
        2.33601592e-01,  1.00248006e+00,  4.71431475e-01, -3.61385606e-01,
       -8.40077059e-01,  2.30002970e+00, -1.06507475e-01, -1.72097917e+00,
       -5.04831305e-01,  8.71303220e-01,  1.15010519e+00, -8.07803803e-01,
        2.57060225e-01, -7.12973957e-01,  6.47143005e-01,  1.13390065e+00,
       -1.62975879e+00,  3.59009636e-01,  1.24839517e-01,  5.52905269e-02,
       -1.66724170e+00, -6.06168667e-01,  6.69526719e-01,  1.08563186e+00,
        4.02708100e-01, -1.02914511e+00,  1.85486459e+00, -1.38270771e+00,
        1.49174375e-01, -2.12248269e-01,  3.08594276e-01,  5.83849961e-01,
        3.16267713e-02, -1.49751103e+00,  2.33224442e+00, -2.46632386e+00,
        1.06475083e+00, -3.45700886e-01, -8.02034761e-01,  8.68971922e-01,
       -6.73205244e-01,  7.39639639e-01,  3.37469442e-01,  1.10915200e+00,
       -1.01735221e+00, -8.87871137e-01,  1.58482996e-01,  4.92435936e-01,
       -3.25194660e-02,  1.37547452e+00,  8.17225884e-02, -1.61475356e+00,
       -2.25599795e-01, -2.06327669e+00,  1.75242873e+00, -4.84029334e-01,
        5.25427477e-01,  7.10926255e-01, -1.75233489e-01, -1.89441103e-01,
        2.26553317e-01, -3.05741673e-01,  3.10524928e-01, -3.40837205e+00,
        2.63865602e+00,  1.31513420e-01, -2.41496067e-01,  8.91892825e-02,
        8.99461754e-01, -1.23108444e+00,  2.73899690e+00, -1.29233496e+00,
       -6.25774488e-01, -2.00985777e-01,  9.94737865e-02, -8.37437012e-01,
        7.28573824e-01,  3.64365802e-01,  3.28726451e-01,  5.81023251e-02,
       -7.96598348e-01, -1.16869246e+00,  6.05371401e-01,  2.21438541e+00,
       -5.54915425e-01, -4.36832896e-01, -1.09395187e+00,  6.88809975e-01,
       -1.25894933e+00,  5.78164941e-01,  2.51539846e-01, -1.40956924e-01,
        1.28207787e+00, -2.27966765e+00,  4.11421051e-01, -5.95798927e-01,
       -1.34038768e-04,  1.23767379e+00, -1.71209084e+00,  2.19426526e+00,
       -9.25297678e-01,  2.90922532e-01,  2.60667239e-01, -7.24485584e-01,
        1.42322958e+00, -1.12357447e+00,  7.68978709e-01, -7.33775612e-01,
        4.70075532e-01,  1.78757215e-02, -1.72646369e-03, -1.19928080e+00,
        1.31275284e+00, -7.11245183e-01,  9.17549321e-01, -2.71993267e+00,
        4.72127878e-01,  1.68205016e+00,  1.53582658e+00, -8.41576080e-01,
       -1.43400381e+00, -1.07784657e+00,  2.26553340e+00, -7.49000821e-01,
        6.63229118e-01, -4.16335074e-01, -7.41259249e-02,  2.93194681e+00,
       -2.66889286e+00, -1.53728244e-01,  2.18720129e-02, -4.74232909e-01,
        1.51531594e+00, -1.24487394e+00,  9.54321606e-01, -2.87745405e-01,
        9.62843135e-01, -6.76907679e-01, -1.59154642e+00, -2.34441482e-01,
        2.60220815e+00, -1.87624303e+00, -7.72762857e-01,  5.18923722e-01,
        1.86728203e+00, -2.55837576e+00,  4.11696495e-01,  1.13038175e-01,
       -6.51063116e-01, -5.82564524e-02, -4.52213371e-01,  9.05109765e-01,
        6.01598401e-02, -3.63120206e-01, -1.03941350e+00,  2.74166400e+00,
       -2.45708118e+00,  1.47420466e+00, -1.32499693e+00,  1.63560680e+00,
        3.54347175e-01, -1.73786271e+00, -1.13386350e+00,  2.42713148e+00,
        1.24959196e+00, -1.27252595e+00, -2.13580664e-01,  6.75270630e-01,
        2.72702973e-02, -1.51753820e+00,  8.69386397e-02,  1.20435973e+00,
       -6.94024543e-01,  1.44621761e+00, -1.88928718e+00,  1.38451785e+00,
       -3.32910944e-01, -4.34811747e-01,  1.28970458e+00, -3.78248162e-01,
       -1.61703153e+00,  1.54468912e+00,  7.98793819e-01, -1.36793626e+00,
       -1.31255630e-01, -4.45856882e-01,  5.89078547e-01,  6.98444183e-01,
       -1.43524892e+00, -6.10456091e-01,  8.35971894e-01, -1.04155006e+00,
        1.76497092e+00, -8.97586367e-01, -1.37138105e+00,  1.23125415e+00,
        1.21131777e-01,  6.22489101e-01, -5.49585595e-01,  1.99955365e+00,
       -2.20055766e+00,  4.04434918e-01, -4.67519205e-02, -1.90008832e-01,
        3.96791131e-01,  4.13048271e-01,  8.52990536e-01, -2.77534496e+00,
        9.01987641e-01,  1.15371611e-02,  1.34084458e+00, -1.20072833e+00,
       -1.57417884e+00,  1.79338850e+00, -1.12646649e-01,  2.10071874e-01,
       -1.20193929e+00,  2.65518127e+00, -1.87099100e+00,  1.03176947e-01,
       -7.30541397e-01, -1.20994291e-01, -3.84835156e-01,  7.07152412e-01,
       -6.03602072e-01,  2.91829100e+00, -3.73931299e+00,  5.71312594e-01,
        6.14083065e-01,  1.03476426e+00, -1.01989903e+00,  1.04834459e+00,
       -1.59517094e+00,  9.47414634e-01,  1.69067907e+00, -2.53738137e+00,
        1.29053763e+00, -1.70683389e-01, -2.43776975e+00,  1.43741094e+00,
        1.66122540e+00, -8.82959042e-01, -1.33383887e+00,  1.78181934e+00,
       -1.10082249e+00,  7.91261379e-01,  5.28744592e-02, -1.45792370e+00,
        1.79665408e+00, -1.71835403e+00, -3.99027945e-01,  2.92378292e-01,
        4.48456055e-01,  4.20884187e-01, -8.71046573e-01,  1.44014467e+00,
       -4.18873197e-01, -9.21115981e-01,  1.51431131e+00,  3.60974732e-01,
       -1.14364622e+00, -1.26166818e-01, -1.58028661e+00,  1.18888163e+00,
        7.52546206e-02,  5.07735449e-01, -3.89267898e-01,  3.95610727e-01,
        1.31446604e+00, -1.91059536e+00, -1.40495938e-02, -8.67290260e-01,
        1.16958832e+00,  9.84607403e-01, -2.63020203e+00,  9.10106347e-01,
        6.35211773e-01,  8.17756431e-01, -3.82222356e-01, -1.91195869e-02,
       -5.17230051e-01,  6.83755764e-01,  5.80617052e-01, -2.62186527e+00,
        2.26662800e+00, -7.54441667e-01, -4.41105039e-01, -1.96608581e+00,
        8.18416884e-01,  2.94037518e+00, -2.21680163e+00, -4.65075092e-01,
        5.19865938e-01, -3.34363861e-01,  7.94991132e-01,  1.40505091e+00,
       -1.95189226e+00,  6.82244406e-01, -1.28609819e+00,  2.55267987e+00,
       -1.17910636e+00, -1.25195822e+00,  1.87794343e+00,  3.86112050e-01,
       -9.18532520e-01, -1.78470769e+00,  3.26062608e+00, -1.29652941e+00,
        8.91344029e-01, -1.60430207e+00,  9.71799599e-02,  4.69214642e-01,
        1.01399388e+00, -8.59071482e-01, -1.38552484e+00,  1.39313963e+00,
        1.39374392e+00, -1.40077449e+00,  7.01598696e-02, -1.37899071e+00,
       -2.66699719e-01,  6.24998040e-01,  2.47405278e-01,  3.97926617e-01,
        7.23023130e-02,  1.45254637e+00, -1.38302945e+00,  1.01160399e+00,
       -9.97309754e-01,  1.48430001e+00, -3.17441073e+00,  1.08462596e+00,
        1.52189199e+00, -1.05632606e+00,  1.08596602e+00, -4.53310549e-01,
        5.99317491e-01, -2.38221557e-01,  1.21887979e-01,  8.86171347e-01,
       -3.56735830e-01,  1.05980090e-01, -8.74007278e-01, -6.00227093e-01,
       -1.35894899e-01,  1.34454868e+00, -3.11431070e+00,  8.87436319e-01,
        2.13206684e-01,  6.19306939e-01, -2.40857880e+00,  3.62701554e+00,
       -5.32673936e-01,  1.44442469e+00, -7.23909690e-01,  7.43863091e-02,
        1.32333463e+00, -2.59656651e+00, -9.89596121e-01,  1.12075516e+00,
       -6.15870397e-01,  4.85647487e-01, -8.19058165e-01,  1.51307716e+00,
        1.89078889e-03, -4.88607155e-01,  3.35811835e-01, -4.22474080e-01,
        8.79879323e-01, -6.07189552e-01, -3.28122299e-01,  1.16848553e+00,
        4.24195246e-01,  2.02714683e-01, -2.19398313e+00,  3.56800012e-01,
       -1.22049361e+00,  1.29278147e+00,  6.30832331e-01, -5.07312608e-01,
        2.05037192e+00, -2.14360916e+00, -7.23249518e-01,  1.54816191e+00,
       -3.61719958e-01,  4.14702150e-01, -1.90890405e-01, -2.96433772e-02,
       -2.34168807e+00,  1.18395497e+00,  6.31777068e-02,  1.83328088e-01,
       -1.35223734e-01,  8.16371236e-01,  2.29345623e-01, -1.67243518e+00,
        1.70528124e+00, -3.23558274e-02, -6.14212588e-02, -1.83708755e+00,
        1.71668734e+00, -3.13928651e-01,  8.86544198e-01,  9.19564728e-01,
       -1.78532302e-02, -1.31661692e+00, -1.03254447e-01,  6.33635507e-01,
       -1.68379341e+00, -4.47147184e-01,  8.33084235e-01,  1.64584645e+00,
       -1.42964032e+00,  1.80059637e+00, -4.14043570e+00,  9.22095168e-01,
        1.30479705e+00,  9.99514401e-01, -8.68998186e-01, -3.29919556e-02,
       -3.56540252e-02, -1.65333039e+00,  2.74467684e+00, -1.72502671e+00,
        1.70402091e+00, -1.05110281e+00,  1.13163146e+00, -6.18086368e-01,
       -4.15606673e-01,  3.22268689e-01, -1.67661309e+00,  1.33170918e+00,
        1.71061393e+00, -2.36242726e-01, -2.16239779e+00,  1.39220708e+00,
       -2.07137381e-01,  5.94006384e-01, -6.41316567e-01, -3.18241590e-01,
        1.54078437e+00, -9.81171130e-01,  1.06070741e+00, -1.55531686e-01,
       -1.20143482e+00,  1.25038243e-01,  2.08013268e+00, -1.54536687e+00,
       -9.30962516e-01, -5.17277697e-01,  2.05417139e+00, -7.16425471e-01,
       -9.36356300e-01,  1.38746759e+00, -4.47377653e-01, -1.80424890e+00,
        2.08311312e+00,  8.03373704e-01,  1.35997860e+00, -2.26896264e+00,
        2.01237351e-01,  1.39721211e+00, -1.27721486e+00,  1.23491823e-01,
       -8.78426068e-01, -8.26818560e-01,  2.16762554e+00, -2.09498938e+00,
        2.28686946e+00, -1.81475618e+00,  9.74582961e-01, -6.10982294e-01,
        1.50964480e+00, -7.56293812e-01,  1.68833359e+00, -2.84686350e+00,
        1.38917299e+00, -3.25134892e-01,  2.37335878e-01,  1.34397196e+00,
       -8.51011024e-01, -1.67431164e+00,  1.56628369e+00, -8.95779113e-01,
       -9.92975315e-02,  1.47187680e+00, -1.54361158e+00,  1.62375657e-01,
        3.74164549e-01,  9.17019368e-01, -2.69977504e-01, -7.57845734e-01,
       -6.12030450e-02, -9.15170842e-01,  2.84281607e-01,  2.94704939e-02,
        4.39652035e-01,  2.12112488e+00, -2.46355617e+00,  3.12093423e-01,
       -1.78615224e+00,  2.44772966e+00, -2.11796278e+00,  5.13114392e-01,
        1.85826594e+00, -3.04303026e+00,  1.99035600e+00,  7.14601276e-01,
        8.04607554e-01, -2.29299292e+00,  2.04058947e-01,  2.36605869e+00,
       -1.64905284e+00, -7.13709804e-01, -5.48482965e-02, -3.26819070e-01,
        4.35628486e-01,  1.48392546e+00, -9.16323602e-02, -1.97325976e+00,
        1.27142935e+00, -5.95287202e-01,  1.14438417e+00, -8.60556091e-01,
        5.12248436e-01, -4.92977421e-01, -2.04434124e+00,  2.01537978e+00,
       -1.31404915e+00,  1.89170067e+00, -1.35224346e+00,  6.83244709e-03,
        5.35608565e-01,  5.85806497e-01, -6.89758377e-01,  1.79495221e+00,
        1.70853367e-01,  2.31532517e-01, -1.77824046e+00, -1.27107160e+00,
        2.55384112e+00, -1.51441595e+00,  4.12877069e-01,  5.93970422e-01,
       -2.16992449e+00,  3.07311397e+00, -5.91246756e-01, -4.35194514e-01,
        5.73872327e-01, -2.44872536e-01, -3.84429170e-01, -4.12919626e-01,
       -4.62145384e-01,  9.52442328e-01,  1.02710207e-01,  7.58116049e-01,
       -7.74218914e-01, -1.03379552e+00, -8.08351483e-01,  1.29104740e+00,
        8.73475691e-02, -7.33790438e-02, -1.44223047e+00,  2.45192675e+00,
        1.05611120e-01, -1.78865194e+00,  1.54693876e+00,  2.27446961e-01,
       -8.19100699e-01, -9.83100995e-01,  2.46703030e+00, -1.07112195e+00,
       -5.93866746e-01,  9.98779105e-01,  9.26647632e-01, -1.95714779e+00,
        1.13886668e+00,  1.32087988e+00, -2.86540899e+00,  4.55654762e-01,
       -1.03526851e-01,  3.79742435e-01, -6.74793125e-02,  4.89771802e-01,
       -1.09109142e+00,  1.15674479e-01,  8.61687624e-01, -1.16249576e-01,
        7.34659135e-01, -3.77316803e-01,  4.03427113e-01, -1.83761401e+00,
        6.45240524e-01,  2.19345463e+00, -1.27146391e+00,  3.94522720e-01,
       -3.99918928e-01,  1.79874593e-01, -6.13706323e-01,  3.77939286e+00,
       -3.61057722e+00,  3.18219112e-01, -2.39034723e+00,  3.28861935e+00,
       -1.54789294e+00,  4.36233549e-01, -4.73325855e-01,  3.36553551e-01,
       -1.59432448e-01,  2.12780613e-01, -1.40638845e-02, -1.06683977e-01,
       -2.90924462e-02,  1.45960796e+00, -2.96249687e-01,  9.41670907e-02,
       -1.53114697e+00,  1.91602482e+00,  5.05760532e-04, -1.57188439e+00,
        2.02191591e+00, -2.05469276e+00, -1.22712849e+00,  2.75935464e+00,
       -1.11089217e+00,  1.08448847e+00, -1.63343157e+00, -5.82988065e-01,
        2.36746480e+00, -2.51595317e+00, -2.94488804e-01, -5.20659430e-01,
       -1.06144410e+00,  1.47592069e+00, -1.23421401e+00,  1.91686168e+00,
       -2.20437241e+00,  9.18502196e-01,  3.31690807e+00, -1.75373156e+00,
       -2.57806141e-01, -1.66827709e+00,  1.21307912e+00,  2.69146462e-01,
       -1.64847850e+00,  1.57084340e+00,  1.07766984e+00, -1.42036733e+00,
        1.16195939e-01, -1.86458368e+00,  4.38652905e-01,  2.31700558e+00,
       -1.61347624e+00, -3.34316053e-01,  1.44157355e-01,  5.65858677e-01,
       -1.10669640e+00,  1.16909083e+00, -1.47387253e+00,  1.99800691e+00,
       -1.75365578e+00,  2.27161852e+00, -1.19827414e+00, -8.36615041e-01,
        1.67254060e+00, -2.19481143e+00,  6.89981546e-01,  4.92283554e-01,
       -1.21098829e-01, -1.89953535e+00,  8.87080379e-01,  9.96816231e-01,
       -1.47130247e+00,  2.45433170e+00, -6.44605480e-01, -9.59903191e-01,
        2.42523886e-01,  2.05982734e+00, -7.39419261e-01, -4.62170461e-01,
       -1.75771600e+00,  2.90357821e+00, -4.14249118e-01, -1.09556635e+00,
       -4.16133220e-01,  3.06824324e-01, -1.03282314e+00,  6.10957455e-01,
        1.18686752e+00, -2.49446574e+00,  1.31278478e+00,  3.96422910e-01,
        1.18766173e-03, -1.27214819e+00, -1.21109633e-01,  2.15310298e+00,
       -2.20477794e+00,  2.11072714e+00, -1.39015118e+00,  1.51392513e+00,
       -1.39289522e+00, -7.87500666e-01,  1.90637904e+00, -7.88290593e-01,
        1.46422869e+00, -4.11518842e-01, -1.03240671e+00, -2.43183636e-01,
        4.28073185e-01,  1.69174909e-01, -1.05293754e+00,  1.63551325e+00,
       -1.15510911e+00, -6.54006025e-02, -1.59963367e-01,  7.17636771e-01,
       -8.99968142e-01,  7.57817452e-01,  2.64512997e+00, -2.54355222e+00,
       -3.85756224e-01, -1.27708496e+00,  1.55114223e+00, -1.15443068e+00,
        6.22749730e-01,  4.89609901e-01, -1.86743628e+00,  1.71535326e+00,
        1.62798698e-01, -1.57116368e+00,  7.75080826e-01, -1.47758809e+00,
        3.22310066e+00, -1.08738757e+00, -4.77095450e-01, -1.80617977e-03,
        1.27853586e+00, -1.11246480e+00,  4.15565768e-01,  1.22089447e+00,
       -1.71293375e+00, -7.81084891e-01,  1.58871217e-01,  2.17071435e+00,
       -1.19436914e+00, -5.84616766e-01,  1.42574254e+00,  1.21677444e-01,
       -1.37380942e+00, -5.43853846e-01, -6.95785448e-01, -3.80413180e-01,
        1.34951358e+00, -6.54708140e-01,  2.66235076e+00, -1.61408921e+00,
       -1.99483352e+00,  3.16666386e+00, -1.11514604e+00,  5.59440202e-01,
        4.75532445e-02, -3.17274732e-01,  2.56441720e-01, -2.32247696e-01,
       -1.32127051e+00,  1.36247951e+00,  6.93846527e-01, -1.13157137e+00,
        7.40352989e-01, -7.65828511e-02,  1.43802183e+00, -1.88683716e+00,
       -6.45288921e-02,  1.45872006e-01,  2.84749103e-03, -2.18046574e+00,
        1.40274610e+00,  8.78233924e-01, -2.78153075e-01, -7.91908291e-01,
        5.46259866e-02,  2.42688199e-01, -4.81519965e-01,  2.08363992e-01,
       -7.76445701e-02,  1.38082195e+00,  2.10557507e-01,  1.88329527e-02,
       -4.13524786e-01, -1.09235410e+00,  1.59732069e+00, -1.17809799e+00,
        3.05877736e-01,  1.31747354e+00, -1.12040562e+00,  1.71690460e-01,
       -1.63533511e+00,  1.75851083e+00, -1.41831501e+00,  1.89394564e+00,
       -1.09534487e+00, -2.07002958e+00,  1.65453186e+00,  9.41835540e-02,
        6.90706311e-01,  2.33584687e-01, -9.31225396e-01,  1.30785602e+00,
       -4.07863670e+00,  2.13636080e+00, -4.69774173e-01, -2.53055667e-01,
        2.08847153e+00, -3.45653352e-02, -1.52202338e+00,  1.87625002e+00,
       -9.58784411e-01, -5.13004304e-01, -3.13407106e-01, -1.54641210e-01,
        1.17321941e+00,  2.24657529e-01, -3.46638199e-01, -2.26486877e+00,
        2.14155457e+00,  2.98673774e-01, -1.17806251e+00,  6.45535588e-01,
       -1.90280979e+00,  4.47526808e-01,  7.82736807e-01, -1.79393306e-02,
        6.30455401e-01, -1.50343682e+00,  7.27026783e-01, -1.82694322e-01,
        9.68812276e-01,  9.45833342e-01,  4.41981828e-01, -3.11726833e+00,
        1.36358185e+00, -1.06931654e+00,  9.36531428e-01,  4.81189736e-01,
       -2.99136453e-01, -1.22353508e-01,  1.52714970e+00, -6.13745866e-01,
       -9.21544914e-01,  2.69600376e-01,  8.49107582e-01, -1.74017520e-01,
       -9.73887559e-01, -1.39267435e+00,  4.13061064e-01,  1.21217097e+00,
       -1.91790816e+00,  1.45547967e+00, -3.16414128e-01,  1.40746506e+00,
       -2.21737135e+00, -7.45529538e-01,  1.31895134e+00,  1.01243980e+00,
        4.98631780e-01, -1.87225376e+00,  1.28865806e+00, -1.53466782e+00])

# Forecast the first MA(1) model
mod = ARMA(simulated_data_1, order=(0,1))
res = mod.fit()
res.plot_predict(start=990, end=1010)
plt.show()