# Generated with SMOP  0.41
# from libsmop import *
# loadmol.m
from copy import*
from numpy import*
    

def loadmol(molid=None,*args,**kwargs):

    molstats['DK'] = copy(0)
# loadmol.m:3
    molstats['DJK'] = copy(0)
# loadmol.m:4
    molstats['DJ'] = copy(0)
# loadmol.m:5
    molstats['deltaK'] = copy(0)
# loadmol.m:6
    molstats['deltaJ'] = copy(0)
# loadmol.m:7
    if 'generic' == molid:
        molstats['a'] = copy(10000)
# loadmol.m:13
        molstats['b'] = copy(8000)
# loadmol.m:14
        molstats['c'] = copy(5000)
# loadmol.m:15
        molstats['DK'] = copy(0)
# loadmol.m:16
        molstats['DJK'] = copy(0)
# loadmol.m:17
        molstats['DJ'] = copy(0)
# loadmol.m:18
        molstats['deltaK'] = copy(0)
# loadmol.m:19
        molstats['deltaJ'] = copy(0)
# loadmol.m:20
        molstats['mua'] = copy(1)
# loadmol.m:22
        molstats['mub'] = copy(1)
# loadmol.m:23
        molstats['muc'] = copy(1)
# loadmol.m:24
        molstats['molname'] = copy('generic')
# loadmol.m:26
        molstats['conformer'] = copy(1)
# loadmol.m:27
        molstats['color'] = copy('r')
# loadmol.m:28
    else:
        if 'annso' == molid:
            molstats['a'] = copy(553.80105 / 1000)
# loadmol.m:30
            molstats['b'] = copy(359.73363 / 1000)
# loadmol.m:31
            molstats['c'] = copy(277.57441 / 1000)
# loadmol.m:32
            molstats['DK'] = copy(0 / 1000)
# loadmol.m:33
            molstats['DJK'] = copy(0 / 1000)
# loadmol.m:34
            molstats['DJ'] = copy(0 / 1000)
# loadmol.m:35
            molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:36
            molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:37
            molstats['mua'] = copy(1)
# loadmol.m:39
            molstats['mub'] = copy(1)
# loadmol.m:40
            molstats['muc'] = copy(0)
# loadmol.m:41
            molstats['molname'] = copy('annso')
# loadmol.m:43
            molstats['conformer'] = copy(3)
# loadmol.m:44
            molstats['color'] = copy('r')
# loadmol.m:45
        else:
            if 'fluorobenzene' == molid:
                molstats['a'] = copy(5663.713 / 1000)
# loadmol.m:48
                molstats['b'] = copy(2570.6531 / 1000)
# loadmol.m:49
                molstats['c'] = copy(1767.9136 / 1000)
# loadmol.m:50
                molstats['mua'] = copy(1.6)
# loadmol.m:52
                molstats['mub'] = copy(0)
# loadmol.m:53
                molstats['muc'] = copy(0)
# loadmol.m:54
                #     molstats['AllowComplex= 1;
                molstats['molname'] = copy('fluorobenzene')
# loadmol.m:58
            else:
                if 'pent1' == molid:
                    molstats['a'] = copy(15644.21396 / 1000)
# loadmol.m:61
                    molstats['b'] = copy(1136.193887 / 1000)
# loadmol.m:62
                    molstats['c'] = copy(1097.914562 / 1000)
# loadmol.m:63
                    molstats['DK'] = copy(0)
# loadmol.m:64
                    molstats['DJK'] = copy(0)
# loadmol.m:65
                    molstats['DJ'] = copy(0)
# loadmol.m:66
                    molstats['deltaK'] = copy(0)
# loadmol.m:67
                    molstats['deltaJ'] = copy(0)
# loadmol.m:68
                    molstats['mua'] = copy(1)
# loadmol.m:70
                    molstats['mub'] = copy(0)
# loadmol.m:71
                    molstats['muc'] = copy(0)
# loadmol.m:72
                    molstats['molname'] = copy('pent1')
# loadmol.m:74
                    molstats['conformer'] = copy(2)
# loadmol.m:75
                    molstats['color'] = copy('r')
# loadmol.m:76
                else:
                    if 'pent2' == molid:
                        #III-D) A    '] = 8947.966372           B    '] = 1345.504933           C    '] = 1250.464296
#DK   '] = 0.0000e+00            DJK  '] = -1.3447e-03           DJ   '] = 1.9511e-04
#dK   '] = 0.0000e+00            dJ   '] = 3.3422e-05
                        molstats['a'] = copy(15928.312294 / 1000)
# loadmol.m:82
                        molstats['b'] = copy(1136.339041 / 1000)
# loadmol.m:83
                        molstats['c'] = copy(1098.266977 / 1000)
# loadmol.m:84
                        molstats['DK'] = copy(0)
# loadmol.m:85
                        molstats['DJK'] = copy(0)
# loadmol.m:86
                        molstats['DJ'] = copy(0)
# loadmol.m:87
                        molstats['deltaK'] = copy(0)
# loadmol.m:88
                        molstats['deltaJ'] = copy(0)
# loadmol.m:89
                        molstats['mua'] = copy(1)
# loadmol.m:91
                        molstats['mub'] = copy(0)
# loadmol.m:92
                        molstats['muc'] = copy(0)
# loadmol.m:93
                        molstats['molname'] = copy('pent2')
# loadmol.m:95
                        molstats['conformer'] = copy(2)
# loadmol.m:96
                        molstats['color'] = copy('r')
# loadmol.m:97
                    else:
                        if 'pent3' == molid:
                            #III-D) A    '] = 8947.966372           B    '] = 1345.504933           C    '] = 1250.464296
#DK   '] = 0.0000e+00            DJK  '] = -1.3447e-03           DJ   '] = 1.9511e-04
#dK   '] = 0.0000e+00            dJ   '] = 3.3422e-05
                            molstats['a'] = copy(9151.9205 / 1000)
# loadmol.m:103
                            molstats['b'] = copy(1373.988635 / 1000)
# loadmol.m:104
                            molstats['c'] = copy(1278.9537 / 1000)
# loadmol.m:105
                            molstats['DK'] = copy(0.041727 / 1000)
# loadmol.m:106
                            molstats['DJK'] = copy(- 0.0031392 / 1000)
# loadmol.m:107
                            molstats['DJ'] = copy(0.00023945 / 1000)
# loadmol.m:108
                            molstats['deltaK'] = copy(0.0016496 / 1000)
# loadmol.m:109
                            molstats['deltaJ'] = copy(4.274e-05 / 1000)
# loadmol.m:110
                            molstats['mua'] = copy(1)
# loadmol.m:112
                            molstats['mub'] = copy(1)
# loadmol.m:113
                            molstats['muc'] = copy(1)
# loadmol.m:114
                            molstats['molname'] = copy('pent3')
# loadmol.m:116
                            molstats['conformer'] = copy(3)
# loadmol.m:117
                            molstats['color'] = copy('r')
# loadmol.m:118
                        else:
                            if 'pulegone2' == molid:
                                molstats['a'] = copy(1819.907 / 1000)
# loadmol.m:120
                                molstats['b'] = copy(816.6853 / 1000)
# loadmol.m:121
                                molstats['c'] = copy(635.94683 / 1000)
# loadmol.m:122
                                molstats['DK'] = copy(0 / 1000)
# loadmol.m:123
                                molstats['DJK'] = copy(0 / 1000)
# loadmol.m:124
                                molstats['DJ'] = copy(0 / 1000)
# loadmol.m:125
                                molstats['deltaK'] = copy(0 / 1000)
# loadmol.m:126
                                molstats['deltaJ'] = copy(0 / 1000)
# loadmol.m:127
                                molstats['mua'] = copy(1)
# loadmol.m:129
                                molstats['mub'] = copy(1)
# loadmol.m:130
                                molstats['muc'] = copy(1)
# loadmol.m:131
                                molstats['molname'] = copy('pulegon1')
# loadmol.m:133
                                molstats['conformer'] = copy(3)
# loadmol.m:134
                                molstats['color'] = copy('r')
# loadmol.m:135
                            else:
                                if 'pulegone1' == molid:
                                    molstats['a'] = copy(1908.49298 / 1000)
# loadmol.m:138
                                    molstats['b'] = copy(738.85952 / 1000)
# loadmol.m:139
                                    molstats['c'] = copy(578.1415 / 1000)
# loadmol.m:140
                                    molstats['DK'] = copy(0 / 1000)
# loadmol.m:141
                                    molstats['DJK'] = copy(0 / 1000)
# loadmol.m:142
                                    molstats['DJ'] = copy(0 / 1000)
# loadmol.m:143
                                    molstats['deltaK'] = copy(0 / 1000)
# loadmol.m:144
                                    molstats['deltaJ'] = copy(0 / 1000)
# loadmol.m:145
                                    molstats['mua'] = copy(1)
# loadmol.m:147
                                    molstats['mub'] = copy(1)
# loadmol.m:148
                                    molstats['muc'] = copy(1)
# loadmol.m:149
                                    molstats['molname'] = copy('pulegon1')
# loadmol.m:151
                                    molstats['conformer'] = copy(3)
# loadmol.m:152
                                    molstats['color'] = copy('r')
# loadmol.m:153
                                else:
                                    if 'pent4' == molid:
                                        #III-D) A    '] = 8947.966372           B    '] = 1345.504933           C    '] = 1250.464296
#DK   '] = 0.0000e+00            DJK  '] = -1.3447e-03           DJ   '] = 1.9511e-04
#dK   '] = 0.0000e+00            dJ   '] = 3.3422e-05
                                        molstats['a'] = copy(9182.53477 / 1000)
# loadmol.m:158
                                        molstats['b'] = copy(1357.763838 / 1000)
# loadmol.m:159
                                        molstats['c'] = copy(1262.3455 / 1000)
# loadmol.m:160
                                        molstats['DK'] = copy(0.08636 / 1000)
# loadmol.m:161
                                        molstats['DJK'] = copy(- 0.002672 / 1000)
# loadmol.m:162
                                        molstats['DJ'] = copy(0.00023709 / 1000)
# loadmol.m:163
                                        molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:164
                                        molstats['deltaJ'] = copy(6.1375e-05 / 1000)
# loadmol.m:165
                                        molstats['mua'] = copy(1)
# loadmol.m:167
                                        molstats['mub'] = copy(1)
# loadmol.m:168
                                        molstats['muc'] = copy(1)
# loadmol.m:169
                                        molstats['molname'] = copy('pent4')
# loadmol.m:171
                                        molstats['conformer'] = copy(3)
# loadmol.m:172
                                        molstats['color'] = copy('r')
# loadmol.m:173
                                    else:
                                        if 'eucalyptol' == molid:
                                            #III-D) A    '] = 8947.966372           B    '] = 1345.504933           C    '] = 1250.464296
#DK   '] = 0.0000e+00            DJK  '] = -1.3447e-03           DJ   '] = 1.9511e-04
#dK   '] = 0.0000e+00            dJ   '] = 3.3422e-05
                                            molstats['a'] = copy(1545.887 / 1000)
# loadmol.m:179
                                            molstats['b'] = copy(1080.4679 / 1000)
# loadmol.m:180
                                            molstats['c'] = copy(1038.9331 / 1000)
# loadmol.m:181
                                            molstats['DK'] = copy(- 3e-05 / 1000)
# loadmol.m:182
                                            molstats['DJK'] = copy(2e-05 / 1000)
# loadmol.m:183
                                            molstats['DJ'] = copy(2.3709e-05 / 1000)
# loadmol.m:184
                                            molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:185
                                            molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:186
                                            molstats['mua'] = copy(0)
# loadmol.m:188
                                            molstats['mub'] = copy(1)
# loadmol.m:189
                                            molstats['muc'] = copy(0)
# loadmol.m:190
                                            molstats['molname'] = copy('eucalyptal')
# loadmol.m:192
                                            molstats['conformer'] = copy(3)
# loadmol.m:193
                                            molstats['color'] = copy('r')
# loadmol.m:194
                                        else:
                                            if 'cineole' == molid:
                                                molstats['a'] = copy(2035.4639 / 1000)
# loadmol.m:197
                                                molstats['b'] = copy(842.273 / 1000)
# loadmol.m:198
                                                molstats['c'] = copy(778.63 / 1000)
# loadmol.m:199
                                                molstats['DK'] = copy(- 0.0 / 1000)
# loadmol.m:200
                                                molstats['DJK'] = copy(0.0 / 1000)
# loadmol.m:201
                                                molstats['DJ'] = copy(0.0 / 1000)
# loadmol.m:202
                                                molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:203
                                                molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:204
                                                molstats['mua'] = copy(1)
# loadmol.m:206
                                                molstats['mub'] = copy(1)
# loadmol.m:207
                                                molstats['muc'] = copy(1)
# loadmol.m:208
                                                molstats['molname'] = copy('cineole')
# loadmol.m:210
                                                molstats['conformer'] = copy(3)
# loadmol.m:211
                                                molstats['color'] = copy('r')
# loadmol.m:212
                                            else:
                                                if 'camphor' == molid:
                                                    molstats['a'] = copy(1446.698977 / 1000)
# loadmol.m:215
                                                    molstats['b'] = copy(1183.36711 / 1000)
# loadmol.m:216
                                                    molstats['c'] = copy(1097.101031 / 1000)
# loadmol.m:217
                                                    molstats['DK'] = copy(- 6.558e-05 / 1000)
# loadmol.m:218
                                                    molstats['DJK'] = copy(8.3681e-05 / 1000)
# loadmol.m:219
                                                    molstats['DJ'] = copy(3.34804e-05 / 1000)
# loadmol.m:220
                                                    molstats['deltaK'] = copy(2.8637e-06 / 1000)
# loadmol.m:221
                                                    molstats['deltaJ'] = copy(2.4858e-05 / 1000)
# loadmol.m:222
                                                    molstats['mua'] = copy(0)
# loadmol.m:224
                                                    molstats['mub'] = copy(1)
# loadmol.m:225
                                                    molstats['muc'] = copy(0)
# loadmol.m:226
                                                    molstats['molname'] = copy('camphor')
# loadmol.m:228
                                                    molstats['conformer'] = copy(3)
# loadmol.m:229
                                                    molstats['color'] = copy('r')
# loadmol.m:230
                                                else:
                                                    if 'linalool' == molid:
                                                        molstats['a'] = copy(1646.7402 / 1000)
# loadmol.m:233
                                                        molstats['b'] = copy(682.19862 / 1000)
# loadmol.m:234
                                                        molstats['c'] = copy(618.751 / 1000)
# loadmol.m:235
                                                        molstats['DK'] = copy(0 / 1000)
# loadmol.m:236
                                                        molstats['DJK'] = copy(0.0003843 / 1000)
# loadmol.m:237
                                                        molstats['DJ'] = copy(0.0001155 / 1000)
# loadmol.m:238
                                                        molstats['deltaK'] = copy(0.000234 / 1000)
# loadmol.m:239
                                                        molstats['deltaJ'] = copy(4.35e-06 / 1000)
# loadmol.m:240
                                                        molstats['mua'] = copy(0)
# loadmol.m:242
                                                        molstats['mub'] = copy(1)
# loadmol.m:243
                                                        molstats['muc'] = copy(0)
# loadmol.m:244
                                                        molstats['molname'] = copy('linalool')
# loadmol.m:246
                                                        molstats['color'] = copy('r')
# loadmol.m:247
                                                    else:
                                                        if 'heptaldehyde1' == molid:
                                                            molstats['a'] = copy(7813.98 / 1000)
# loadmol.m:251
                                                            molstats['b'] = copy(572.42 / 1000)
# loadmol.m:252
                                                            molstats['c'] = copy(544.72 / 1000)
# loadmol.m:253
                                                            molstats['DK'] = copy(0 / 1000)
# loadmol.m:254
                                                            molstats['DJK'] = copy(0 / 1000)
# loadmol.m:255
                                                            molstats['DJ'] = copy(0 / 1000)
# loadmol.m:256
                                                            molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:257
                                                            molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:258
                                                            molstats['mua'] = copy(1)
# loadmol.m:260
                                                            molstats['mub'] = copy(1)
# loadmol.m:261
                                                            molstats['muc'] = copy(0)
# loadmol.m:262
                                                            molstats['molname'] = copy('heptaldehyde1')
# loadmol.m:264
                                                            molstats['conformer'] = copy(3)
# loadmol.m:265
                                                            molstats['color'] = copy('r')
# loadmol.m:266
                                                        else:
                                                            if 'test3' == molid:
                                                                molstats['a'] = copy(5000 / 1000)
# loadmol.m:269
                                                                molstats['b'] = copy(1750 / 1000)
# loadmol.m:270
                                                                molstats['c'] = copy(1350 / 1000)
# loadmol.m:271
                                                                molstats['DK'] = copy(0 / 1000)
# loadmol.m:272
                                                                molstats['DJK'] = copy(0 / 1000)
# loadmol.m:273
                                                                molstats['DJ'] = copy(0 / 1000)
# loadmol.m:274
                                                                molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:275
                                                                molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:276
                                                                molstats['mua'] = copy(1)
# loadmol.m:278
                                                                molstats['mub'] = copy(1)
# loadmol.m:279
                                                                molstats['muc'] = copy(0)
# loadmol.m:280
                                                                molstats['molname'] = copy('test3')
# loadmol.m:282
                                                                molstats['conformer'] = copy(3)
# loadmol.m:283
                                                                molstats['color'] = copy('r')
# loadmol.m:284
                                                            else:
                                                                if 'test1' == molid:
                                                                    molstats['a'] = copy(5000 / 1000)
# loadmol.m:287
                                                                    molstats['b'] = copy(1680 / 1000)
# loadmol.m:288
                                                                    molstats['c'] = copy(1420 / 1000)
# loadmol.m:289
                                                                    molstats['DK'] = copy(0 / 1000)
# loadmol.m:290
                                                                    molstats['DJK'] = copy(0 / 1000)
# loadmol.m:291
                                                                    molstats['DJ'] = copy(0 / 1000)
# loadmol.m:292
                                                                    molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:293
                                                                    molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:294
                                                                    molstats['mua'] = copy(1)
# loadmol.m:296
                                                                    molstats['mub'] = copy(1)
# loadmol.m:297
                                                                    molstats['muc'] = copy(0)
# loadmol.m:298
                                                                    molstats['molname'] = copy('test1')
# loadmol.m:300
                                                                    molstats['conformer'] = copy(3)
# loadmol.m:301
                                                                    molstats['color'] = copy('r')
# loadmol.m:302
                                                                else:
                                                                    if 'test2' == molid:
                                                                        molstats['a'] = copy(5500 / 1000)
# loadmol.m:305
                                                                        molstats['b'] = copy(1650 / 1000)
# loadmol.m:306
                                                                        molstats['c'] = copy(1450 / 1000)
# loadmol.m:307
                                                                        molstats['DK'] = copy(0 / 1000)
# loadmol.m:308
                                                                        molstats['DJK'] = copy(0 / 1000)
# loadmol.m:309
                                                                        molstats['DJ'] = copy(0 / 1000)
# loadmol.m:310
                                                                        molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:311
                                                                        molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:312
                                                                        molstats['mua'] = copy(1)
# loadmol.m:314
                                                                        molstats['mub'] = copy(1)
# loadmol.m:315
                                                                        molstats['muc'] = copy(0)
# loadmol.m:316
                                                                        molstats['molname'] = copy('test2')
# loadmol.m:318
                                                                        molstats['conformer'] = copy(3)
# loadmol.m:319
                                                                        molstats['color'] = copy('r')
# loadmol.m:320
                                                                    else:
                                                                        if 'test2floppy' == molid:
                                                                            molstats['a'] = copy(7000 / 1000)
# loadmol.m:323
                                                                            molstats['b'] = copy(1650 / 1000)
# loadmol.m:324
                                                                            molstats['c'] = copy(1450 / 1000)
# loadmol.m:325
                                                                            molstats['mua'] = copy(1)
# loadmol.m:327
                                                                            molstats['mub'] = copy(1)
# loadmol.m:328
                                                                            molstats['muc'] = copy(0)
# loadmol.m:329
                                                                            molstats['molname'] = copy('test1')
# loadmol.m:331
                                                                            molstats['conformer'] = copy(3)
# loadmol.m:332
                                                                            molstats['color'] = copy('r')
# loadmol.m:333
                                                                            molstats['DK'] = copy(0.024 / 1000)
# loadmol.m:335
                                                                            molstats['DJK'] = copy(0.002 / 1000)
# loadmol.m:336
                                                                            molstats['DJ'] = copy(0.001 / 1000)
# loadmol.m:337
                                                                            molstats['deltaK'] = copy(0.001 / 1000)
# loadmol.m:338
                                                                            molstats['deltaJ'] = copy(0.0003 / 1000)
# loadmol.m:339
                                                                        else:
                                                                            if 'test4' == molid:
                                                                                molstats['a'] = copy(3000 / 1000)
# loadmol.m:342
                                                                                molstats['b'] = copy(1630 / 1000)
# loadmol.m:343
                                                                                molstats['c'] = copy(1470 / 1000)
# loadmol.m:344
                                                                                molstats['DK'] = copy(0 / 1000)
# loadmol.m:345
                                                                                molstats['DJK'] = copy(0 / 1000)
# loadmol.m:346
                                                                                molstats['DJ'] = copy(0 / 1000)
# loadmol.m:347
                                                                                molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:348
                                                                                molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:349
                                                                                molstats['mua'] = copy(1)
# loadmol.m:351
                                                                                molstats['mub'] = copy(1)
# loadmol.m:352
                                                                                molstats['muc'] = copy(0)
# loadmol.m:353
                                                                                molstats['molname'] = copy('test1')
# loadmol.m:355
                                                                                molstats['conformer'] = copy(3)
# loadmol.m:356
                                                                                molstats['color'] = copy('r')
# loadmol.m:357
                                                                            else:
                                                                                if 'test6' == molid:
                                                                                    molstats['a'] = copy(3000 / 1000)
# loadmol.m:360
                                                                                    molstats['b'] = copy(1800 / 1000)
# loadmol.m:361
                                                                                    molstats['c'] = copy(1300 / 1000)
# loadmol.m:362
                                                                                    molstats['DK'] = copy(0 / 1000)
# loadmol.m:363
                                                                                    molstats['DJK'] = copy(0 / 1000)
# loadmol.m:364
                                                                                    molstats['DJ'] = copy(0 / 1000)
# loadmol.m:365
                                                                                    molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:366
                                                                                    molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:367
                                                                                    molstats['mua'] = copy(1)
# loadmol.m:369
                                                                                    molstats['mub'] = copy(1)
# loadmol.m:370
                                                                                    molstats['muc'] = copy(0)
# loadmol.m:371
                                                                                    molstats['molname'] = copy('test1')
# loadmol.m:373
                                                                                    molstats['conformer'] = copy(3)
# loadmol.m:374
                                                                                    molstats['color'] = copy('r')
# loadmol.m:375
                                                                                else:
                                                                                    if 'test5' == molid:
                                                                                        molstats['a'] = copy(1500 / 1000)
# loadmol.m:378
                                                                                        molstats['b'] = copy(700 / 1000)
# loadmol.m:379
                                                                                        molstats['c'] = copy(500 / 1000)
# loadmol.m:380
                                                                                        molstats['DK'] = copy(0 / 1000)
# loadmol.m:381
                                                                                        molstats['DJK'] = copy(0 / 1000)
# loadmol.m:382
                                                                                        molstats['DJ'] = copy(0 / 1000)
# loadmol.m:383
                                                                                        molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:384
                                                                                        molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:385
                                                                                        molstats['mua'] = copy(1)
# loadmol.m:387
                                                                                        molstats['mub'] = copy(1)
# loadmol.m:388
                                                                                        molstats['muc'] = copy(0)
# loadmol.m:389
                                                                                        molstats['molname'] = copy('test5')
# loadmol.m:391
                                                                                        molstats['conformer'] = copy(3)
# loadmol.m:392
                                                                                        molstats['color'] = copy('r')
# loadmol.m:393
                                                                                    else:
                                                                                        if 'angelica' == molid:
                                                                                            molstats['a'] = copy(6041.2302 / 1000)
# loadmol.m:396
                                                                                            molstats['b'] = copy(2240.1566 / 1000)
# loadmol.m:397
                                                                                            molstats['c'] = copy(1668.313 / 1000)
# loadmol.m:398
                                                                                            molstats['DK'] = copy(0 / 1000)
# loadmol.m:399
                                                                                            molstats['DJK'] = copy(0 / 1000)
# loadmol.m:400
                                                                                            molstats['DJ'] = copy(0 / 1000)
# loadmol.m:401
                                                                                            molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:402
                                                                                            molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:403
                                                                                            molstats['mua'] = copy(1)
# loadmol.m:405
                                                                                            molstats['mub'] = copy(1)
# loadmol.m:406
                                                                                            molstats['muc'] = copy(0)
# loadmol.m:407
                                                                                            molstats['molname'] = copy('angelica')
# loadmol.m:409
                                                                                        else:
                                                                                            if 'ethylguiacol' == molid:
                                                                                                molstats['a'] = copy(1640.45 / 1000)
# loadmol.m:412
                                                                                                molstats['b'] = copy(802.45 / 1000)
# loadmol.m:413
                                                                                                molstats['c'] = copy(567.84 / 1000)
# loadmol.m:414
                                                                                                molstats['DK'] = copy(0 / 1000)
# loadmol.m:415
                                                                                                molstats['DJK'] = copy(0 / 1000)
# loadmol.m:416
                                                                                                molstats['DJ'] = copy(0 / 1000)
# loadmol.m:417
                                                                                                molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:418
                                                                                                molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:419
                                                                                                molstats['mua'] = copy(1)
# loadmol.m:421
                                                                                                molstats['mub'] = copy(1)
# loadmol.m:422
                                                                                                molstats['muc'] = copy(0)
# loadmol.m:423
                                                                                                molstats['molname'] = copy('ethylguiacol')
# loadmol.m:425
                                                                                            else:
                                                                                                if 'cinnamylalcohol' == molid:
                                                                                                    molstats['a'] = copy(4298.7 / 1000)
# loadmol.m:428
                                                                                                    molstats['b'] = copy(562.3 / 1000)
# loadmol.m:429
                                                                                                    molstats['c'] = copy(513.75 / 1000)
# loadmol.m:430
                                                                                                    molstats['DK'] = copy(0 / 1000)
# loadmol.m:431
                                                                                                    molstats['DJK'] = copy(0 / 1000)
# loadmol.m:432
                                                                                                    molstats['DJ'] = copy(0 / 1000)
# loadmol.m:433
                                                                                                    molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:434
                                                                                                    molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:435
                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:437
                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:438
                                                                                                    molstats['muc'] = copy(0)
# loadmol.m:439
                                                                                                    molstats['molname'] = copy('cinnamylalcohol')
# loadmol.m:441
                                                                                                else:
                                                                                                    if 'terpineol1' == molid:
                                                                                                        molstats['a'] = copy(2329.3 / 1000)
# loadmol.m:444
                                                                                                        molstats['b'] = copy(618.97 / 1000)
# loadmol.m:445
                                                                                                        molstats['c'] = copy(560.39 / 1000)
# loadmol.m:446
                                                                                                        molstats['DK'] = copy(0 / 1000)
# loadmol.m:447
                                                                                                        molstats['DJK'] = copy(0 / 1000)
# loadmol.m:448
                                                                                                        molstats['DJ'] = copy(0 / 1000)
# loadmol.m:449
                                                                                                        molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:450
                                                                                                        molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:451
                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:453
                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:454
                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:455
                                                                                                        molstats['molname'] = copy('alpha-terpineol 1')
# loadmol.m:457
                                                                                                        molstats['conformer'] = copy(3)
# loadmol.m:458
                                                                                                        molstats['color'] = copy('r')
# loadmol.m:459
                                                                                                    else:
                                                                                                        if 'hexanalnot' == molid:
                                                                                                            molstats['a'] = copy(9735.59 / 1000)
# loadmol.m:462
                                                                                                            molstats['b'] = copy(868.845 / 1000)
# loadmol.m:463
                                                                                                            molstats['c'] = copy(818.518 / 1000)
# loadmol.m:464
                                                                                                            molstats['DK'] = copy(0)
# loadmol.m:465
                                                                                                            molstats['DJK'] = copy(0)
# loadmol.m:466
                                                                                                            molstats['DJ'] = copy(0)
# loadmol.m:467
                                                                                                            molstats['deltaK'] = copy(0)
# loadmol.m:468
                                                                                                            molstats['deltaJ'] = copy(0)
# loadmol.m:469
                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:471
                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:472
                                                                                                            molstats['muc'] = copy(0)
# loadmol.m:473
                                                                                                            molstats['molname'] = copy('hexanalnot')
# loadmol.m:475
                                                                                                            molstats['conformer'] = copy(3)
# loadmol.m:476
                                                                                                            molstats['color'] = copy('r')
# loadmol.m:477
                                                                                                        else:
                                                                                                            if 'hexanalrigid' == molid:
                                                                                                                molstats['a'] = copy(9769.63045 / 1000)
# loadmol.m:480
                                                                                                                molstats['b'] = copy(868.84588 / 1000)
# loadmol.m:481
                                                                                                                molstats['c'] = copy(818.518 / 1000)
# loadmol.m:482
                                                                                                                molstats['DK'] = copy(0.0 / 1000)
# loadmol.m:483
                                                                                                                molstats['DJK'] = copy(0.0 / 1000)
# loadmol.m:484
                                                                                                                molstats['DJ'] = copy(0.0 / 1000)
# loadmol.m:485
                                                                                                                molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:486
                                                                                                                molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:487
                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:489
                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:490
                                                                                                                molstats['muc'] = copy(0)
# loadmol.m:491
                                                                                                                molstats['molname'] = copy('hexanalrigid')
# loadmol.m:493
                                                                                                                molstats['conformer'] = copy(3)
# loadmol.m:494
                                                                                                                molstats['color'] = copy('r')
# loadmol.m:495
                                                                                                            else:
                                                                                                                if 'skinnytrouble' == molid:
                                                                                                                    molstats['a'] = copy(7451.4 / 1000)
# loadmol.m:498
                                                                                                                    molstats['b'] = copy(830.8 / 1000)
# loadmol.m:499
                                                                                                                    molstats['c'] = copy(806.7 / 1000)
# loadmol.m:500
                                                                                                                    molstats['DK'] = copy(0.024 / 1000)
# loadmol.m:501
                                                                                                                    molstats['DJK'] = copy(0.002 / 1000)
# loadmol.m:502
                                                                                                                    molstats['DJ'] = copy(0.001 / 1000)
# loadmol.m:503
                                                                                                                    molstats['deltaK'] = copy(0.001 / 1000)
# loadmol.m:504
                                                                                                                    molstats['deltaJ'] = copy(0.0003 / 1000)
# loadmol.m:505
                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:507
                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:508
                                                                                                                    molstats['muc'] = copy(0)
# loadmol.m:509
                                                                                                                    molstats['molname'] = copy('skinny')
# loadmol.m:511
                                                                                                                    molstats['conformer'] = copy(3)
# loadmol.m:512
                                                                                                                    molstats['color'] = copy('r')
# loadmol.m:513
                                                                                                                else:
                                                                                                                    if 'hexanalbare' == molid:
                                                                                                                        molstats['a'] = copy(9735.59 / 1000)
# loadmol.m:516
                                                                                                                        molstats['b'] = copy(868.85 / 1000)
# loadmol.m:517
                                                                                                                        molstats['c'] = copy(818.51 / 1000)
# loadmol.m:518
                                                                                                                        molstats['DK'] = copy(0.0 / 1000)
# loadmol.m:519
                                                                                                                        molstats['DJK'] = copy(0.0 / 1000)
# loadmol.m:520
                                                                                                                        molstats['DJ'] = copy(0.0 / 1000)
# loadmol.m:521
                                                                                                                        molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:522
                                                                                                                        molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:523
                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:525
                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:526
                                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:527
                                                                                                                        molstats['molname'] = copy('hexanal1')
# loadmol.m:529
                                                                                                                        molstats['conformer'] = copy(3)
# loadmol.m:530
                                                                                                                        molstats['color'] = copy('r')
# loadmol.m:531
                                                                                                                    else:
                                                                                                                        if 'hexanal1' == molid:
                                                                                                                            molstats['a'] = copy(9769.63045 / 1000)
# loadmol.m:534
                                                                                                                            molstats['b'] = copy(868.84588 / 1000)
# loadmol.m:535
                                                                                                                            molstats['c'] = copy(818.518 / 1000)
# loadmol.m:536
                                                                                                                            molstats['DK'] = copy(0.024 / 1000)
# loadmol.m:537
                                                                                                                            molstats['DJK'] = copy(0.002 / 1000)
# loadmol.m:538
                                                                                                                            molstats['DJ'] = copy(0.001 / 1000)
# loadmol.m:539
                                                                                                                            molstats['deltaK'] = copy(0.001 / 1000)
# loadmol.m:540
                                                                                                                            molstats['deltaJ'] = copy(0.0003 / 1000)
# loadmol.m:541
                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:543
                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:544
                                                                                                                            molstats['muc'] = copy(0)
# loadmol.m:545
                                                                                                                            molstats['molname'] = copy('hexanal1')
# loadmol.m:547
                                                                                                                            molstats['conformer'] = copy(3)
# loadmol.m:548
                                                                                                                            molstats['color'] = copy('r')
# loadmol.m:549
                                                                                                                        else:
                                                                                                                            if 'hexanal2' == molid:
                                                                                                                                molstats['a'] = copy(5399.89 / 1000)
# loadmol.m:555
                                                                                                                                molstats['b'] = copy(1143.24 / 1000)
# loadmol.m:556
                                                                                                                                molstats['c'] = copy(1028.99 / 1000)
# loadmol.m:557
                                                                                                                                molstats['DK'] = copy(0.014 / 1000)
# loadmol.m:558
                                                                                                                                molstats['DJK'] = copy(0 / 1000)
# loadmol.m:559
                                                                                                                                molstats['DJ'] = copy(0 / 1000)
# loadmol.m:560
                                                                                                                                molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:561
                                                                                                                                molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:562
                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:564
                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:565
                                                                                                                                molstats['muc'] = copy(0)
# loadmol.m:566
                                                                                                                                molstats['molname'] = copy('hexanal1')
# loadmol.m:568
                                                                                                                                molstats['conformer'] = copy(3)
# loadmol.m:569
                                                                                                                                molstats['color'] = copy('r')
# loadmol.m:570
                                                                                                                            else:
                                                                                                                                if 'hexanal3' == molid:
                                                                                                                                    molstats['a'] = copy(8975.49 / 1000)
# loadmol.m:572
                                                                                                                                    molstats['b'] = copy(933.43 / 1000)
# loadmol.m:573
                                                                                                                                    molstats['c'] = copy(898.08 / 1000)
# loadmol.m:574
                                                                                                                                    molstats['DK'] = copy(0.072 / 1000)
# loadmol.m:575
                                                                                                                                    molstats['DJK'] = copy(0 / 1000)
# loadmol.m:576
                                                                                                                                    molstats['DJ'] = copy(0 / 1000)
# loadmol.m:577
                                                                                                                                    molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:578
                                                                                                                                    molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:579
                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:581
                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:582
                                                                                                                                    molstats['muc'] = copy(0)
# loadmol.m:583
                                                                                                                                    molstats['molname'] = copy('hexanal13')
# loadmol.m:585
                                                                                                                                    molstats['conformer'] = copy(3)
# loadmol.m:586
                                                                                                                                    molstats['color'] = copy('r')
# loadmol.m:587
                                                                                                                                else:
                                                                                                                                    if 'hexanal4' == molid:
                                                                                                                                        molstats['a'] = copy(5995.206 / 1000)
# loadmol.m:589
                                                                                                                                        molstats['b'] = copy(1046.739 / 1000)
# loadmol.m:590
                                                                                                                                        molstats['c'] = copy(945.971 / 1000)
# loadmol.m:591
                                                                                                                                        molstats['DK'] = copy(0.018 / 1000)
# loadmol.m:592
                                                                                                                                        molstats['DJK'] = copy(0 / 1000)
# loadmol.m:593
                                                                                                                                        molstats['DJ'] = copy(0 / 1000)
# loadmol.m:594
                                                                                                                                        molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:595
                                                                                                                                        molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:596
                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:598
                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:599
                                                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:600
                                                                                                                                        molstats['molname'] = copy('hexanal4')
# loadmol.m:602
                                                                                                                                        molstats['conformer'] = copy(3)
# loadmol.m:603
                                                                                                                                        molstats['color'] = copy('r')
# loadmol.m:604
                                                                                                                                    else:
                                                                                                                                        if 'hexanal5' == molid:
                                                                                                                                            molstats['a'] = copy(6116.502 / 1000)
# loadmol.m:606
                                                                                                                                            molstats['b'] = copy(1167.3003 / 1000)
# loadmol.m:607
                                                                                                                                            molstats['c'] = copy(1059.541 / 1000)
# loadmol.m:608
                                                                                                                                            molstats['DK'] = copy(0.0178 / 1000)
# loadmol.m:609
                                                                                                                                            molstats['DJK'] = copy(- 0.002 / 1000)
# loadmol.m:610
                                                                                                                                            molstats['DJ'] = copy(0 / 1000)
# loadmol.m:611
                                                                                                                                            molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:612
                                                                                                                                            molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:613
                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:615
                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:616
                                                                                                                                            molstats['muc'] = copy(0)
# loadmol.m:617
                                                                                                                                            molstats['molname'] = copy('hexanal5')
# loadmol.m:619
                                                                                                                                            molstats['conformer'] = copy(3)
# loadmol.m:620
                                                                                                                                            molstats['color'] = copy('r')
# loadmol.m:621
                                                                                                                                        else:
                                                                                                                                            if 'hexanal6' == molid:
                                                                                                                                                molstats['a'] = copy(4667.6175 / 1000)
# loadmol.m:623
                                                                                                                                                molstats['b'] = copy(1336.769 / 1000)
# loadmol.m:624
                                                                                                                                                molstats['c'] = copy(1166.123 / 1000)
# loadmol.m:625
                                                                                                                                                molstats['DK'] = copy(0.0207 / 1000)
# loadmol.m:626
                                                                                                                                                molstats['DJK'] = copy(- 0.005 / 1000)
# loadmol.m:627
                                                                                                                                                molstats['DJ'] = copy(0 / 1000)
# loadmol.m:628
                                                                                                                                                molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:629
                                                                                                                                                molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:630
                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:632
                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:633
                                                                                                                                                molstats['muc'] = copy(0)
# loadmol.m:634
                                                                                                                                                molstats['molname'] = copy('hexanal6')
# loadmol.m:636
                                                                                                                                                molstats['conformer'] = copy(3)
# loadmol.m:637
                                                                                                                                                molstats['color'] = copy('r')
# loadmol.m:638
                                                                                                                                            else:
                                                                                                                                                if 'hexanal7' == molid:
                                                                                                                                                    molstats['a'] = copy(5455.608 / 1000)
# loadmol.m:640
                                                                                                                                                    molstats['b'] = copy(1055.756 / 1000)
# loadmol.m:641
                                                                                                                                                    molstats['c'] = copy(937.27 / 1000)
# loadmol.m:642
                                                                                                                                                    molstats['DK'] = copy(0.041 / 1000)
# loadmol.m:643
                                                                                                                                                    molstats['DJK'] = copy(- 0.005 / 1000)
# loadmol.m:644
                                                                                                                                                    molstats['DJ'] = copy(0 / 1000)
# loadmol.m:645
                                                                                                                                                    molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:646
                                                                                                                                                    molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:647
                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:649
                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:650
                                                                                                                                                    molstats['muc'] = copy(0)
# loadmol.m:651
                                                                                                                                                    molstats['molname'] = copy('hexanal7')
# loadmol.m:653
                                                                                                                                                    molstats['conformer'] = copy(3)
# loadmol.m:654
                                                                                                                                                    molstats['color'] = copy('r')
# loadmol.m:655
                                                                                                                                                else:
                                                                                                                                                    if 'hexanal8' == molid:
                                                                                                                                                        molstats['a'] = copy(4827.9103 / 1000)
# loadmol.m:657
                                                                                                                                                        molstats['b'] = copy(1240.841 / 1000)
# loadmol.m:658
                                                                                                                                                        molstats['c'] = copy(1159.91 / 1000)
# loadmol.m:659
                                                                                                                                                        molstats['DK'] = copy(0.04 / 1000)
# loadmol.m:660
                                                                                                                                                        molstats['DJK'] = copy(- 0.005 / 1000)
# loadmol.m:661
                                                                                                                                                        molstats['DJ'] = copy(0 / 1000)
# loadmol.m:662
                                                                                                                                                        molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:663
                                                                                                                                                        molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:664
                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:666
                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:667
                                                                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:668
                                                                                                                                                        molstats['molname'] = copy('hexanal8')
# loadmol.m:670
                                                                                                                                                        molstats['conformer'] = copy(3)
# loadmol.m:671
                                                                                                                                                        molstats['color'] = copy('r')
# loadmol.m:672
                                                                                                                                                    else:
                                                                                                                                                        if 'guac' == molid:
                                                                                                                                                            molstats['a'] = copy(1640.45 / 1000)
# loadmol.m:674
                                                                                                                                                            molstats['b'] = copy(802.454 / 1000)
# loadmol.m:675
                                                                                                                                                            molstats['c'] = copy(567.84 / 1000)
# loadmol.m:676
                                                                                                                                                            #         molstats['DK'] = 0.0000 / 1000;
#         molstats['DJK'] = 0 / 1000; # distortion constants in units of MHz
#         molstats['DJ'] = 0 / 1000;
#         molstats['deltaK'] = 0.00 / 1000;
#         molstats['deltaJ'] = 0.0000 / 1000;
                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:683
                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:684
                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:685
                                                                                                                                                            molstats['molname'] = copy('benzOH1')
# loadmol.m:687
                                                                                                                                                            molstats['conformer'] = copy(3)
# loadmol.m:688
                                                                                                                                                            molstats['color'] = copy('r')
# loadmol.m:689
                                                                                                                                                        else:
                                                                                                                                                            if 'benzOD1' == molid:
                                                                                                                                                                molstats['a'] = copy(4678.9317326 / 1000)
# loadmol.m:692
                                                                                                                                                                molstats['b'] = copy(1442.9604 / 1000)
# loadmol.m:693
                                                                                                                                                                molstats['c'] = copy(1169.2206 / 1000)
# loadmol.m:694
                                                                                                                                                                molstats['DK'] = copy(- 0.00138 / 1000)
# loadmol.m:695
                                                                                                                                                                molstats['DJK'] = copy(0.0031611 / 1000)
# loadmol.m:696
                                                                                                                                                                molstats['DJ'] = copy(0.000154189 / 1000)
# loadmol.m:697
                                                                                                                                                                molstats['deltaK'] = copy(- 0.0003 / 1000)
# loadmol.m:698
                                                                                                                                                                molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:699
                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:701
                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:702
                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:703
                                                                                                                                                                molstats['molname'] = copy('benzOD1')
# loadmol.m:705
                                                                                                                                                                molstats['conformer'] = copy(3)
# loadmol.m:706
                                                                                                                                                                molstats['color'] = copy('r')
# loadmol.m:707
                                                                                                                                                            else:
                                                                                                                                                                if 'benzOD2' == molid:
                                                                                                                                                                    molstats['a'] = copy(4667.4299 / 1000)
# loadmol.m:709
                                                                                                                                                                    molstats['b'] = copy(1452.106 / 1000)
# loadmol.m:710
                                                                                                                                                                    molstats['c'] = copy(1163.6514 / 1000)
# loadmol.m:711
                                                                                                                                                                    molstats['DK'] = copy(- 0.00144 / 1000)
# loadmol.m:712
                                                                                                                                                                    molstats['DJK'] = copy(0.0029011 / 1000)
# loadmol.m:713
                                                                                                                                                                    molstats['DJ'] = copy(0.00028889 / 1000)
# loadmol.m:714
                                                                                                                                                                    molstats['deltaK'] = copy(- 0.00244 / 1000)
# loadmol.m:715
                                                                                                                                                                    molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:716
                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:718
                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:719
                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:720
                                                                                                                                                                    molstats['molname'] = copy('benzOD1')
# loadmol.m:722
                                                                                                                                                                    molstats['conformer'] = copy(3)
# loadmol.m:723
                                                                                                                                                                    molstats['color'] = copy('r')
# loadmol.m:724
                                                                                                                                                                else:
                                                                                                                                                                    if 'benzOH1' == molid:
                                                                                                                                                                        molstats['a'] = copy(4678.960326 / 1000)
# loadmol.m:727
                                                                                                                                                                        molstats['b'] = copy(1442.955701 / 1000)
# loadmol.m:728
                                                                                                                                                                        molstats['c'] = copy(1169.219333 / 1000)
# loadmol.m:729
                                                                                                                                                                        molstats['DK'] = copy(0.0 / 1000)
# loadmol.m:730
                                                                                                                                                                        molstats['DJK'] = copy(0.003202021 / 1000)
# loadmol.m:731
                                                                                                                                                                        molstats['DJ'] = copy(0.0001175189 / 1000)
# loadmol.m:732
                                                                                                                                                                        molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:733
                                                                                                                                                                        molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:734
                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:736
                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:737
                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:738
                                                                                                                                                                        molstats['molname'] = copy('benzOH1')
# loadmol.m:740
                                                                                                                                                                        molstats['conformer'] = copy(3)
# loadmol.m:741
                                                                                                                                                                        molstats['color'] = copy('r')
# loadmol.m:742
                                                                                                                                                                    else:
                                                                                                                                                                        if 'benzOH2' == molid:
                                                                                                                                                                            molstats['a'] = copy(4667.418335 / 1000)
# loadmol.m:744
                                                                                                                                                                            molstats['b'] = copy(1452.08694 / 1000)
# loadmol.m:745
                                                                                                                                                                            molstats['c'] = copy(1163.65239 / 1000)
# loadmol.m:746
                                                                                                                                                                            molstats['DK'] = copy(0.0 / 1000)
# loadmol.m:747
                                                                                                                                                                            molstats['DJK'] = copy(0.002888046 / 1000)
# loadmol.m:748
                                                                                                                                                                            molstats['DJ'] = copy(0.0001637668 / 1000)
# loadmol.m:749
                                                                                                                                                                            molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:750
                                                                                                                                                                            molstats['deltaJ'] = copy(0.0 / 1000)
# loadmol.m:751
                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:753
                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:754
                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:755
                                                                                                                                                                            molstats['molname'] = copy('benzOH2')
# loadmol.m:757
                                                                                                                                                                            molstats['conformer'] = copy(3)
# loadmol.m:758
                                                                                                                                                                            molstats['color'] = copy('r')
# loadmol.m:759
                                                                                                                                                                        else:
                                                                                                                                                                            if '13prop' == molid:
                                                                                                                                                                                #III-D) A    '] = 8947.966372           B    '] = 1345.504933           C    '] = 1250.464296
#DK   '] = 0.0000e+00            DJK  '] = -1.3447e-03           DJ   '] = 1.9511e-04
#dK   '] = 0.0000e+00            dJ   '] = 3.3422e-05 
#https://ac.els-cdn.com/S0022285285711289/1-s2.0-S0022285285711289-main.pdf?_tid=d1706b3c-a631-11e7-9ba6-00000aab0f02&acdnat=1506812035_8c14a070a2ec3252336e244cc8b1cfb1
                                                                                                                                                                                molstats['a'] = copy(7701.232 / 1000)
# loadmol.m:766
                                                                                                                                                                                molstats['b'] = copy(3891.298 / 1000)
# loadmol.m:767
                                                                                                                                                                                molstats['c'] = copy(2854.556 / 1000)
# loadmol.m:768
                                                                                                                                                                                molstats['DK'] = copy(0.00239 / 1000)
# loadmol.m:769
                                                                                                                                                                                molstats['DJK'] = copy(0.00012 / 1000)
# loadmol.m:770
                                                                                                                                                                                molstats['DJ'] = copy(0.00023709 / 1000)
# loadmol.m:771
                                                                                                                                                                                molstats['deltaK'] = copy(0.004 / 1000)
# loadmol.m:772
                                                                                                                                                                                molstats['deltaJ'] = copy(7e-05 / 1000)
# loadmol.m:773
                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:775
                                                                                                                                                                                molstats['mub'] = copy(0)
# loadmol.m:776
                                                                                                                                                                                molstats['muc'] = copy(0)
# loadmol.m:777
                                                                                                                                                                                molstats['molname'] = copy('1,3 propanediol from Camninati')
# loadmol.m:779
                                                                                                                                                                                molstats['conformer'] = copy(1)
# loadmol.m:780
                                                                                                                                                                                molstats['color'] = copy('r')
# loadmol.m:781
                                                                                                                                                                            else:
                                                                                                                                                                                if 'pent5' == molid:
                                                                                                                                                                                    # A    '] = 9330.579234           B    '] = 1471.774296           C    '] = 1363.472674
# DK   '] = 0.0000e+00            DJK  '] = -2.1912e-03           DJ   '] = 2.3821e-04
# dK   '] = 0.0000e+00            dJ   '] = 3.4582e-05
                                                                                                                                                                                    molstats['a'] = copy(9330.5792 / 1000)
# loadmol.m:788
                                                                                                                                                                                    molstats['b'] = copy(1471.774 / 1000)
# loadmol.m:789
                                                                                                                                                                                    molstats['c'] = copy(1363.4726 / 1000)
# loadmol.m:790
                                                                                                                                                                                    molstats['DK'] = copy(0.0 / 1000)
# loadmol.m:791
                                                                                                                                                                                    molstats['DJK'] = copy(- 0.00219 / 1000)
# loadmol.m:792
                                                                                                                                                                                    molstats['DJ'] = copy(0.000238 / 1000)
# loadmol.m:793
                                                                                                                                                                                    molstats['deltaK'] = copy(0.0 / 1000)
# loadmol.m:794
                                                                                                                                                                                    molstats['deltaJ'] = copy(4.5e-05 / 1000)
# loadmol.m:795
                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:797
                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:798
                                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:799
                                                                                                                                                                                    molstats['molname'] = copy('pent5')
# loadmol.m:801
                                                                                                                                                                                    molstats['conformer'] = copy(3)
# loadmol.m:802
                                                                                                                                                                                    molstats['color'] = copy('r')
# loadmol.m:803
                                                                                                                                                                                else:
                                                                                                                                                                                    if 'Dpent3' == molid:
                                                                                                                                                                                        #III-D) A    '] = 8947.966372           B    '] = 1345.504933           C    '] = 1250.464296
#DK   '] = 0.0000e+00            DJK  '] = -1.3447e-03           DJ   '] = 1.9511e-04
#dK   '] = 0.0000e+00            dJ   '] = 3.3422e-05
                                                                                                                                                                                        molstats['a'] = copy(8947.888112 / 1000)
# loadmol.m:809
                                                                                                                                                                                        molstats['b'] = copy(1345.507967 / 1000)
# loadmol.m:810
                                                                                                                                                                                        molstats['c'] = copy(1250.459244 / 1000)
# loadmol.m:811
                                                                                                                                                                                        molstats['DK'] = copy(0.032898 / 1000)
# loadmol.m:812
                                                                                                                                                                                        molstats['DJK'] = copy(- 0.0025095 / 1000)
# loadmol.m:813
                                                                                                                                                                                        molstats['DJ'] = copy(0.00021514 / 1000)
# loadmol.m:814
                                                                                                                                                                                        molstats['deltaK'] = copy(0.0019845 / 1000)
# loadmol.m:815
                                                                                                                                                                                        molstats['deltaJ'] = copy(3.59e-05 / 1000)
# loadmol.m:816
                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:818
                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:819
                                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:820
                                                                                                                                                                                        molstats['molname'] = copy('Dpent3')
# loadmol.m:822
                                                                                                                                                                                        molstats['conformer'] = copy(3)
# loadmol.m:823
                                                                                                                                                                                        molstats['color'] = copy('r')
# loadmol.m:824
                                                                                                                                                                                    else:
                                                                                                                                                                                        if 'Dpent4' == molid:
                                                                                                                                                                                            #III-D) A    '] = 8947.966372           B    '] = 1345.504933           C    '] = 1250.464296
#DK   '] = 0.0000e+00            DJK  '] = -1.3447e-03           DJ   '] = 1.9511e-04
#dK   '] = 0.0000e+00            dJ   '] = 3.3422e-05
                                                                                                                                                                                            molstats['a'] = copy(8812.226057 / 1000)
# loadmol.m:830
                                                                                                                                                                                            molstats['b'] = copy(1352.2967 / 1000)
# loadmol.m:831
                                                                                                                                                                                            molstats['c'] = copy(1266.195 / 1000)
# loadmol.m:832
                                                                                                                                                                                            molstats['DK'] = copy(0.035372 / 1000)
# loadmol.m:833
                                                                                                                                                                                            molstats['DJK'] = copy(- 0.0025095 / 1000)
# loadmol.m:834
                                                                                                                                                                                            molstats['DJ'] = copy(0.00022937 / 1000)
# loadmol.m:835
                                                                                                                                                                                            molstats['deltaK'] = copy(0.002418 / 1000)
# loadmol.m:836
                                                                                                                                                                                            molstats['deltaJ'] = copy(3.802e-05 / 1000)
# loadmol.m:837
                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:839
                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:840
                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:841
                                                                                                                                                                                            molstats['molname'] = copy('Dpent4')
# loadmol.m:843
                                                                                                                                                                                            molstats['conformer'] = copy(3)
# loadmol.m:844
                                                                                                                                                                                            molstats['color'] = copy('r')
# loadmol.m:845
                                                                                                                                                                                        else:
                                                                                                                                                                                            if array([1,'prop3']) == molid:
                                                                                                                                                                                                molstats['a'] = copy(8572.0553 / 1000)
# loadmol.m:847
                                                                                                                                                                                                molstats['b'] = copy(3640.1063 / 1000)
# loadmol.m:848
                                                                                                                                                                                                molstats['c'] = copy(2790.9666 / 1000)
# loadmol.m:849
                                                                                                                                                                                                molstats['DK'] = copy(0.00253 / 1000)
# loadmol.m:850
                                                                                                                                                                                                molstats['DJK'] = copy(0.005276 / 1000)
# loadmol.m:851
                                                                                                                                                                                                molstats['DJ'] = copy(0.000738 / 1000)
# loadmol.m:852
                                                                                                                                                                                                molstats['deltaK'] = copy(0.00318 / 1000)
# loadmol.m:853
                                                                                                                                                                                                molstats['deltaJ'] = copy(0.0001631 / 1000)
# loadmol.m:854
                                                                                                                                                                                                molstats['mua'] = copy(1.21)
# loadmol.m:856
                                                                                                                                                                                                molstats['mub'] = copy(2.1)
# loadmol.m:857
                                                                                                                                                                                                molstats['muc'] = copy(0.45)
# loadmol.m:858
                                                                                                                                                                                                molstats['molname'] = copy('1,2-propanediol Conf. 3')
# loadmol.m:859
                                                                                                                                                                                                molstats['conformer'] = copy(3)
# loadmol.m:861
                                                                                                                                                                                                molstats['color'] = copy('r')
# loadmol.m:862
                                                                                                                                                                                            else:
                                                                                                                                                                                                if 701 == molid:
                                                                                                                                                                                                    molstats['a'] = copy(8.5720553)
# loadmol.m:864
                                                                                                                                                                                                    molstats['b'] = copy(3.6401063)
# loadmol.m:865
                                                                                                                                                                                                    molstats['c'] = copy(2.7909666)
# loadmol.m:866
                                                                                                                                                                                                    molstats['DK'] = copy(0)
# loadmol.m:867
                                                                                                                                                                                                    molstats['DJK'] = copy(0)
# loadmol.m:868
                                                                                                                                                                                                    molstats['DJ'] = copy(0)
# loadmol.m:869
                                                                                                                                                                                                    molstats['deltaK'] = copy(0)
# loadmol.m:870
                                                                                                                                                                                                    molstats['deltaJ'] = copy(0)
# loadmol.m:871
                                                                                                                                                                                                    molstats['mua'] = copy(1.21)
# loadmol.m:873
                                                                                                                                                                                                    molstats['mub'] = copy(2.1)
# loadmol.m:874
                                                                                                                                                                                                    molstats['muc'] = copy(0.45)
# loadmol.m:875
                                                                                                                                                                                                    molstats['molname'] = copy('1-2 propanediol Conformer 3 no centrip')
# loadmol.m:876
                                                                                                                                                                                                    molstats['molname'] = copy('prop3')
# loadmol.m:877
                                                                                                                                                                                                    molstats['conformer'] = copy(3)
# loadmol.m:878
                                                                                                                                                                                                    molstats['color'] = copy('r')
# loadmol.m:879
                                                                                                                                                                                                else:
                                                                                                                                                                                                    if array([101,'prop3,13C3']) == molid:
                                                                                                                                                                                                        molstats['a'] = copy(8485.725 / 1000.0)
# loadmol.m:882
                                                                                                                                                                                                        molstats['b'] = copy(3625.759 / 1000.0)
# loadmol.m:883
                                                                                                                                                                                                        molstats['c'] = copy(2775.135 / 1000.0)
# loadmol.m:884
                                                                                                                                                                                                        molstats['DK'] = copy(0.00253 / 1000.0)
# loadmol.m:885
                                                                                                                                                                                                        molstats['DJK'] = copy(0.005276 / 1000.0)
# loadmol.m:886
                                                                                                                                                                                                        molstats['DJ'] = copy(0.000738 / 1000.0)
# loadmol.m:887
                                                                                                                                                                                                        molstats['deltaK'] = copy(0.00318 / 1000.0)
# loadmol.m:888
                                                                                                                                                                                                        molstats['deltaJ'] = copy(0.0001631 / 1000.0)
# loadmol.m:889
                                                                                                                                                                                                        molstats['mua'] = copy(1.21)
# loadmol.m:891
                                                                                                                                                                                                        molstats['mub'] = copy(2.1)
# loadmol.m:892
                                                                                                                                                                                                        molstats['muc'] = copy(0.45)
# loadmol.m:893
                                                                                                                                                                                                        molstats['molname'] = copy('1-2 propanediol Conf 3,13c3')
# loadmol.m:894
                                                                                                                                                                                                        molstats['conformer'] = copy(3)
# loadmol.m:895
                                                                                                                                                                                                        molstats['color'] = copy('r')
# loadmol.m:896
                                                                                                                                                                                                    else:
                                                                                                                                                                                                        if array([102,'prop3,13C4']) == molid:
                                                                                                                                                                                                            molstats['a'] = copy(8555.92 / 1000.0)
# loadmol.m:899
                                                                                                                                                                                                            molstats['b'] = copy(3631.166 / 1000.0)
# loadmol.m:900
                                                                                                                                                                                                            molstats['c'] = copy(2787.564 / 1000.0)
# loadmol.m:901
                                                                                                                                                                                                            molstats['DK'] = copy(0.00253 / 1000.0)
# loadmol.m:902
                                                                                                                                                                                                            molstats['DJK'] = copy(0.005276 / 1000.0)
# loadmol.m:903
                                                                                                                                                                                                            molstats['DJ'] = copy(0.000738 / 1000.0)
# loadmol.m:904
                                                                                                                                                                                                            molstats['deltaK'] = copy(0.00318 / 1000.0)
# loadmol.m:905
                                                                                                                                                                                                            molstats['deltaJ'] = copy(0.0001631 / 1000.0)
# loadmol.m:906
                                                                                                                                                                                                            molstats['mua'] = copy(1.21)
# loadmol.m:908
                                                                                                                                                                                                            molstats['mub'] = copy(2.1)
# loadmol.m:909
                                                                                                                                                                                                            molstats['muc'] = copy(0.45)
# loadmol.m:910
                                                                                                                                                                                                            molstats['molname'] = copy('1-2 propanediol Conf 3,13c4')
# loadmol.m:911
                                                                                                                                                                                                            molstats['conformer'] = copy(3)
# loadmol.m:912
                                                                                                                                                                                                            molstats['color'] = copy('r')
# loadmol.m:913
                                                                                                                                                                                                        else:
                                                                                                                                                                                                            if array([103,'prop3,13C7']) == molid:
                                                                                                                                                                                                                molstats['a'] = copy(8506.815 / 1000.0)
# loadmol.m:916
                                                                                                                                                                                                                molstats['b'] = copy(3557.975 / 1000.0)
# loadmol.m:917
                                                                                                                                                                                                                molstats['c'] = copy(2735.709 / 1000.0)
# loadmol.m:918
                                                                                                                                                                                                                molstats['DK'] = copy(0.00253 / 1000.0)
# loadmol.m:919
                                                                                                                                                                                                                molstats['DJK'] = copy(0.005276 / 1000.0)
# loadmol.m:920
                                                                                                                                                                                                                molstats['DJ'] = copy(0.000738 / 1000.0)
# loadmol.m:921
                                                                                                                                                                                                                molstats['deltaK'] = copy(0.00318 / 1000.0)
# loadmol.m:922
                                                                                                                                                                                                                molstats['deltaJ'] = copy(0.0001631 / 1000.0)
# loadmol.m:923
                                                                                                                                                                                                                molstats['mua'] = copy(1.21)
# loadmol.m:925
                                                                                                                                                                                                                molstats['mub'] = copy(2.1)
# loadmol.m:926
                                                                                                                                                                                                                molstats['muc'] = copy(0.45)
# loadmol.m:927
                                                                                                                                                                                                                molstats['molname'] = copy('1-2 propanediol Conf 3,13c7')
# loadmol.m:928
                                                                                                                                                                                                                molstats['conformer'] = copy(3)
# loadmol.m:929
                                                                                                                                                                                                                molstats['color'] = copy('r')
# loadmol.m:930
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                if 104 == molid:
                                                                                                                                                                                                                    molstats['a'] = copy(8.314741)
# loadmol.m:935
                                                                                                                                                                                                                    molstats['b'] = copy(3.633983)
# loadmol.m:936
                                                                                                                                                                                                                    molstats['c'] = copy(2.763027)
# loadmol.m:937
                                                                                                                                                                                                                    molstats['DK'] = copy(0.00316 / 1000.0)
# loadmol.m:938
                                                                                                                                                                                                                    molstats['DJK'] = copy(0.0044851 / 1000.0)
# loadmol.m:939
                                                                                                                                                                                                                    molstats['DJ'] = copy(0.0007971 / 1000.0)
# loadmol.m:940
                                                                                                                                                                                                                    molstats['deltaK'] = copy(0.00314 / 1000.0)
# loadmol.m:941
                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0.0001827 / 1000.0)
# loadmol.m:942
                                                                                                                                                                                                                    molstats['mua'] = copy(2.64)
# loadmol.m:944
                                                                                                                                                                                                                    molstats['mub'] = copy(0.28)
# loadmol.m:945
                                                                                                                                                                                                                    molstats['muc'] = copy(0.57)
# loadmol.m:946
                                                                                                                                                                                                                    # molstats['mass'] = 76 * AMU;
                                                                                                                                                                                                                    molstats['molname'] = copy('1-2 propanediol #2 13C31 ')
# loadmol.m:948
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                    if 'cinn2' == molid:
                                                                                                                                                                                                                        molstats['a'] = copy(8866.41)
# loadmol.m:952
                                                                                                                                                                                                                        molstats['b'] = copy(579.06)
# loadmol.m:953
                                                                                                                                                                                                                        molstats['c'] = copy(517.81)
# loadmol.m:954
                                                                                                                                                                                                                        molstats['DK'] = copy(0)
# loadmol.m:955
                                                                                                                                                                                                                        molstats['DJK'] = copy(0)
# loadmol.m:956
                                                                                                                                                                                                                        molstats['DJ'] = copy(0)
# loadmol.m:957
                                                                                                                                                                                                                        molstats['deltaK'] = copy(0)
# loadmol.m:958
                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0)
# loadmol.m:959
                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:961
                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:962
                                                                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:963
                                                                                                                                                                                                                        molstats['molname'] = copy('cinn')
# loadmol.m:964
                                                                                                                                                                                                                        molstats['conformer'] = copy(1)
# loadmol.m:965
                                                                                                                                                                                                                        molstats['color'] = copy('r')
# loadmol.m:966
                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                        if 'rose1' == molid:
                                                                                                                                                                                                                            molstats['a'] = copy(1400.9025)
# loadmol.m:968
                                                                                                                                                                                                                            molstats['b'] = copy(1161.9887)
# loadmol.m:969
                                                                                                                                                                                                                            molstats['c'] = copy(1089.45165)
# loadmol.m:970
                                                                                                                                                                                                                            molstats['DK'] = copy(0)
# loadmol.m:971
                                                                                                                                                                                                                            molstats['DJK'] = copy(0)
# loadmol.m:972
                                                                                                                                                                                                                            molstats['DJ'] = copy(0)
# loadmol.m:973
                                                                                                                                                                                                                            molstats['deltaK'] = copy(0)
# loadmol.m:974
                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0)
# loadmol.m:975
                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:977
                                                                                                                                                                                                                            molstats['mub'] = copy(0)
# loadmol.m:978
                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:979
                                                                                                                                                                                                                            molstats['molname'] = copy('rosemary1')
# loadmol.m:980
                                                                                                                                                                                                                            molstats['conformer'] = copy(1)
# loadmol.m:981
                                                                                                                                                                                                                            molstats['color'] = copy('r')
# loadmol.m:982
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                            if 'cinn' == molid:
                                                                                                                                                                                                                                molstats['a'] = copy(4866.41)
# loadmol.m:985
                                                                                                                                                                                                                                molstats['b'] = copy(579.06)
# loadmol.m:986
                                                                                                                                                                                                                                molstats['c'] = copy(517.81)
# loadmol.m:987
                                                                                                                                                                                                                                molstats['DK'] = copy(0)
# loadmol.m:988
                                                                                                                                                                                                                                molstats['DJK'] = copy(0)
# loadmol.m:989
                                                                                                                                                                                                                                molstats['DJ'] = copy(0)
# loadmol.m:990
                                                                                                                                                                                                                                molstats['deltaK'] = copy(0)
# loadmol.m:991
                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0)
# loadmol.m:992
                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:994
                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:995
                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:996
                                                                                                                                                                                                                                molstats['molname'] = copy('cinn')
# loadmol.m:997
                                                                                                                                                                                                                                molstats['conformer'] = copy(1)
# loadmol.m:998
                                                                                                                                                                                                                                molstats['color'] = copy('r')
# loadmol.m:999
                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                if 'cinnac' == molid:
                                                                                                                                                                                                                                    molstats['a'] = copy(4866.41)
# loadmol.m:1002
                                                                                                                                                                                                                                    molstats['b'] = copy(579.06)
# loadmol.m:1003
                                                                                                                                                                                                                                    molstats['c'] = copy(517.81)
# loadmol.m:1004
                                                                                                                                                                                                                                    molstats['DK'] = copy(0)
# loadmol.m:1005
                                                                                                                                                                                                                                    molstats['DJK'] = copy(0)
# loadmol.m:1006
                                                                                                                                                                                                                                    molstats['DJ'] = copy(0)
# loadmol.m:1007
                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0)
# loadmol.m:1008
                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0)
# loadmol.m:1009
                                                                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:1011
                                                                                                                                                                                                                                    molstats['mub'] = copy(0)
# loadmol.m:1012
                                                                                                                                                                                                                                    molstats['muc'] = copy(5)
# loadmol.m:1013
                                                                                                                                                                                                                                    molstats['molname'] = copy('cinnac')
# loadmol.m:1014
                                                                                                                                                                                                                                    molstats['conformer'] = copy(1)
# loadmol.m:1015
                                                                                                                                                                                                                                    molstats['color'] = copy('r')
# loadmol.m:1016
                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                    if 'cinnjusta' == molid:
                                                                                                                                                                                                                                        molstats['a'] = copy(4866.41)
# loadmol.m:1019
                                                                                                                                                                                                                                        molstats['b'] = copy(579.06)
# loadmol.m:1020
                                                                                                                                                                                                                                        molstats['c'] = copy(517.81)
# loadmol.m:1021
                                                                                                                                                                                                                                        molstats['DK'] = copy(0)
# loadmol.m:1022
                                                                                                                                                                                                                                        molstats['DJK'] = copy(0)
# loadmol.m:1023
                                                                                                                                                                                                                                        molstats['DJ'] = copy(0)
# loadmol.m:1024
                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0)
# loadmol.m:1025
                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0)
# loadmol.m:1026
                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:1028
                                                                                                                                                                                                                                        molstats['mub'] = copy(0)
# loadmol.m:1029
                                                                                                                                                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:1030
                                                                                                                                                                                                                                        molstats['molname'] = copy('cinnac')
# loadmol.m:1031
                                                                                                                                                                                                                                        molstats['conformer'] = copy(1)
# loadmol.m:1032
                                                                                                                                                                                                                                        molstats['color'] = copy('r')
# loadmol.m:1033
                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                        if 'oblate' == molid:
                                                                                                                                                                                                                                            molstats['a'] = copy(866.41)
# loadmol.m:1036
                                                                                                                                                                                                                                            molstats['b'] = copy(679.06)
# loadmol.m:1037
                                                                                                                                                                                                                                            molstats['c'] = copy(517.81)
# loadmol.m:1038
                                                                                                                                                                                                                                            molstats['DK'] = copy(0)
# loadmol.m:1039
                                                                                                                                                                                                                                            molstats['DJK'] = copy(0)
# loadmol.m:1040
                                                                                                                                                                                                                                            molstats['DJ'] = copy(0)
# loadmol.m:1041
                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0)
# loadmol.m:1042
                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0)
# loadmol.m:1043
                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:1045
                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:1046
                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:1047
                                                                                                                                                                                                                                            molstats['molname'] = copy('oblate')
# loadmol.m:1048
                                                                                                                                                                                                                                            molstats['conformer'] = copy(0)
# loadmol.m:1049
                                                                                                                                                                                                                                            molstats['color'] = copy('r')
# loadmol.m:1050
                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                            if 'bigoblate' == molid:
                                                                                                                                                                                                                                                molstats['a'] = copy(1866.41)
# loadmol.m:1053
                                                                                                                                                                                                                                                molstats['b'] = copy(1679.06)
# loadmol.m:1054
                                                                                                                                                                                                                                                molstats['c'] = copy(1217.81)
# loadmol.m:1055
                                                                                                                                                                                                                                                molstats['DK'] = copy(0)
# loadmol.m:1056
                                                                                                                                                                                                                                                molstats['DJK'] = copy(0)
# loadmol.m:1057
                                                                                                                                                                                                                                                molstats['DJ'] = copy(0)
# loadmol.m:1058
                                                                                                                                                                                                                                                molstats['deltaK'] = copy(0)
# loadmol.m:1059
                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0)
# loadmol.m:1060
                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:1062
                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:1063
                                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:1064
                                                                                                                                                                                                                                                molstats['molname'] = copy('bigoblate')
# loadmol.m:1065
                                                                                                                                                                                                                                                molstats['conformer'] = copy(0)
# loadmol.m:1066
                                                                                                                                                                                                                                                molstats['color'] = copy('r')
# loadmol.m:1067
                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                if 2 == molid:
                                                                                                                                                                                                                                                    molstats['a'] = copy(2.2569)
# loadmol.m:1070
                                                                                                                                                                                                                                                    molstats['b'] = copy(0.6729)
# loadmol.m:1071
                                                                                                                                                                                                                                                    molstats['c'] = copy(0.5545)
# loadmol.m:1072
                                                                                                                                                                                                                                                    molstats['DK'] = copy(- 0.00111)
# loadmol.m:1073
                                                                                                                                                                                                                                                    molstats['DJK'] = copy(3.12e-05)
# loadmol.m:1074
                                                                                                                                                                                                                                                    molstats['DJ'] = copy(1.413e-05)
# loadmol.m:1075
                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(- 0.000363)
# loadmol.m:1076
                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(1.55e-06)
# loadmol.m:1077
                                                                                                                                                                                                                                                    molstats['mua'] = copy(1.68)
# loadmol.m:1079
                                                                                                                                                                                                                                                    molstats['mub'] = copy(2.54)
# loadmol.m:1080
                                                                                                                                                                                                                                                    molstats['muc'] = copy(0.7)
# loadmol.m:1081
                                                                                                                                                                                                                                                    molstats['molname'] = copy('EQ1 Carvone')
# loadmol.m:1082
                                                                                                                                                                                                                                                    molstats['conformer'] = copy(1)
# loadmol.m:1083
                                                                                                                                                                                                                                                    molstats['color'] = copy('r')
# loadmol.m:1084
                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                    if 3 == molid:
                                                                                                                                                                                                                                                        molstats['a'] = copy(2.2372)
# loadmol.m:1088
                                                                                                                                                                                                                                                        molstats['b'] = copy(0.65628)
# loadmol.m:1089
                                                                                                                                                                                                                                                        molstats['c'] = copy(0.57964)
# loadmol.m:1090
                                                                                                                                                                                                                                                        molstats['DK'] = copy(- 0.0007562 / 1000)
# loadmol.m:1091
                                                                                                                                                                                                                                                        molstats['DJK'] = copy(0.0001487 / 1000)
# loadmol.m:1092
                                                                                                                                                                                                                                                        molstats['DJ'] = copy(1.246e-05 / 1000)
# loadmol.m:1093
                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(- 0.001308 / 1000)
# loadmol.m:1094
                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(4.49e-06 / 1000)
# loadmol.m:1095
                                                                                                                                                                                                                                                        molstats['forcemaxj'] = copy(24)
# loadmol.m:1096
                                                                                                                                                                                                                                                        molstats['mua'] = copy(1.82)
# loadmol.m:1097
                                                                                                                                                                                                                                                        molstats['mub'] = copy(2.76)
# loadmol.m:1098
                                                                                                                                                                                                                                                        molstats['muc'] = copy(0.5)
# loadmol.m:1099
                                                                                                                                                                                                                                                        molstats['molname'] = copy('EQ2 Carvone')
# loadmol.m:1100
                                                                                                                                                                                                                                                        molstats['conformer'] = copy(2)
# loadmol.m:1101
                                                                                                                                                                                                                                                        molstats['color'] = copy('b')
# loadmol.m:1102
                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                        if 4 == molid:
                                                                                                                                                                                                                                                            molstats['a'] = copy(2.2128)
# loadmol.m:1106
                                                                                                                                                                                                                                                            molstats['b'] = copy(0.68452)
# loadmol.m:1107
                                                                                                                                                                                                                                                            molstats['c'] = copy(0.55473)
# loadmol.m:1108
                                                                                                                                                                                                                                                            molstats['DK'] = copy(0)
# loadmol.m:1109
                                                                                                                                                                                                                                                            molstats['DJK'] = copy(0)
# loadmol.m:1110
                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0)
# loadmol.m:1111
                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0)
# loadmol.m:1112
                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0)
# loadmol.m:1113
                                                                                                                                                                                                                                                            molstats['mua'] = copy(1.54)
# loadmol.m:1115
                                                                                                                                                                                                                                                            molstats['mub'] = copy(2.27)
# loadmol.m:1116
                                                                                                                                                                                                                                                            molstats['muc'] = copy(0.32)
# loadmol.m:1117
                                                                                                                                                                                                                                                            molstats['molname'] = copy('EQ3 Carvone')
# loadmol.m:1118
                                                                                                                                                                                                                                                            molstats['conformer'] = copy(3)
# loadmol.m:1119
                                                                                                                                                                                                                                                            molstats['color'] = copy('g')
# loadmol.m:1120
                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                            if 6 == molid:
                                                                                                                                                                                                                                                                molstats['a'] = copy(10.34787)
# loadmol.m:1127
                                                                                                                                                                                                                                                                molstats['b'] = copy(4.10236)
# loadmol.m:1128
                                                                                                                                                                                                                                                                molstats['c'] = copy(3.78195)
# loadmol.m:1129
                                                                                                                                                                                                                                                                molstats['mua'] = copy(0.61)
# loadmol.m:1131
                                                                                                                                                                                                                                                                molstats['mub'] = copy(1.2)
# loadmol.m:1132
                                                                                                                                                                                                                                                                molstats['muc'] = copy(0.52)
# loadmol.m:1133
                                                                                                                                                                                                                                                                molstats['molname'] = copy('glycidol')
# loadmol.m:1134
                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                if 7 == molid:
                                                                                                                                                                                                                                                                    molstats['a'] = copy(7.948403)
# loadmol.m:1137
                                                                                                                                                                                                                                                                    molstats['b'] = copy(3.64057)
# loadmol.m:1138
                                                                                                                                                                                                                                                                    molstats['c'] = copy(2.747727)
# loadmol.m:1139
                                                                                                                                                                                                                                                                    molstats['mua'] = copy(3.0)
# loadmol.m:1141
                                                                                                                                                                                                                                                                    molstats['mub'] = copy(0.54)
# loadmol.m:1142
                                                                                                                                                                                                                                                                    molstats['muc'] = copy(0.57)
# loadmol.m:1143
                                                                                                                                                                                                                                                                    molstats['molname'] = copy('alaninol-1')
# loadmol.m:1144
                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                    if 8 == molid:
                                                                                                                                                                                                                                                                        molstats['a'] = copy(6.46162)
# loadmol.m:1146
                                                                                                                                                                                                                                                                        molstats['b'] = copy(4.144442)
# loadmol.m:1147
                                                                                                                                                                                                                                                                        molstats['c'] = copy(3.336136)
# loadmol.m:1148
                                                                                                                                                                                                                                                                        molstats['mua'] = copy(2.19)
# loadmol.m:1150
                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1.46)
# loadmol.m:1151
                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1.17)
# loadmol.m:1152
                                                                                                                                                                                                                                                                        molstats['molname'] = copy('alaninol-2')
# loadmol.m:1153
                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                        if 9 == molid:
                                                                                                                                                                                                                                                                            molstats['a'] = copy(6.54183)
# loadmol.m:1155
                                                                                                                                                                                                                                                                            molstats['b'] = copy(2.26406)
# loadmol.m:1156
                                                                                                                                                                                                                                                                            molstats['c'] = copy(1.81284)
# loadmol.m:1157
                                                                                                                                                                                                                                                                            molstats['mua'] = copy(2.0)
# loadmol.m:1159
                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1.8)
# loadmol.m:1160
                                                                                                                                                                                                                                                                            molstats['muc'] = copy(0.5)
# loadmol.m:1161
                                                                                                                                                                                                                                                                            molstats['molname'] = copy('13butandiol-2')
# loadmol.m:1162
                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                            if 11 == molid:
                                                                                                                                                                                                                                                                                molstats['a'] = copy(1.699)
# loadmol.m:1165
                                                                                                                                                                                                                                                                                molstats['b'] = copy(0.696)
# loadmol.m:1166
                                                                                                                                                                                                                                                                                molstats['c'] = copy(0.561)
# loadmol.m:1167
                                                                                                                                                                                                                                                                                molstats['mua'] = copy(0.6)
# loadmol.m:1169
                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1.2)
# loadmol.m:1170
                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0.7)
# loadmol.m:1171
                                                                                                                                                                                                                                                                                molstats['molname'] = copy('Tryptamine')
# loadmol.m:1172
                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                if 12 == molid:
                                                                                                                                                                                                                                                                                    molstats['a'] = copy(2.049)
# loadmol.m:1174
                                                                                                                                                                                                                                                                                    molstats['b'] = copy(0.584)
# loadmol.m:1175
                                                                                                                                                                                                                                                                                    molstats['c'] = copy(0.555)
# loadmol.m:1176
                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1.5)
# loadmol.m:1178
                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(0.4)
# loadmol.m:1179
                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(2.6)
# loadmol.m:1180
                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('Nicotine')
# loadmol.m:1181
                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                    if 13 == molid:
                                                                                                                                                                                                                                                                                        molstats['a'] = copy(dot(29.99792458,4.2537))
# loadmol.m:1184
                                                                                                                                                                                                                                                                                        molstats['b'] = copy(dot(29.99792458,0.82357))
# loadmol.m:1185
                                                                                                                                                                                                                                                                                        molstats['c'] = copy(dot(29.99792458,0.792538))
# loadmol.m:1186
                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1.6)
# loadmol.m:1188
                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(0)
# loadmol.m:1189
                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:1190
                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('Methanol')
# loadmol.m:1191
                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                        if 14 == molid:
                                                                                                                                                                                                                                                                                            molstats['a'] = copy(5655.2654 / 1000.0)
# loadmol.m:1194
                                                                                                                                                                                                                                                                                            molstats['b'] = copy(1546.8758 / 1000.0)
# loadmol.m:1195
                                                                                                                                                                                                                                                                                            molstats['c'] = copy(1214.404 / 1000.0)
# loadmol.m:1196
                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(4.5152)
# loadmol.m:1198
                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(0)
# loadmol.m:1199
                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(0)
# loadmol.m:1200
                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(0)
# loadmol.m:1202
                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(0.937 / 1000.0)
# loadmol.m:1203
                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0.045 / 1000.0)
# loadmol.m:1204
                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0.603 / 1000.0)
# loadmol.m:1205
                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0.0112 / 1000.0)
# loadmol.m:1206
                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('Benznormal')
# loadmol.m:1207
                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                            if 'benzlia' == molid:
                                                                                                                                                                                                                                                                                                molstats['a'] = copy(5655.2121 / 1000.0)
# loadmol.m:1210
                                                                                                                                                                                                                                                                                                molstats['b'] = copy(1500.56 / 1000.0)
# loadmol.m:1211
                                                                                                                                                                                                                                                                                                molstats['c'] = copy(1185.87 / 1000.0)
# loadmol.m:1212
                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(4.5152)
# loadmol.m:1214
                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(0)
# loadmol.m:1215
                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0)
# loadmol.m:1216
                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(0)
# loadmol.m:1218
                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(0.937 / 1000.0)
# loadmol.m:1219
                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(0.045 / 1000.0)
# loadmol.m:1220
                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(0.603 / 1000.0)
# loadmol.m:1221
                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0.0112 / 1000.0)
# loadmol.m:1222
                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('Benznormal')
# loadmol.m:1223
                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                if 114 == molid:
                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(5655.5075 / 1000.0)
# loadmol.m:1225
                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(1545.55183 / 1000.0)
# loadmol.m:1226
                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(1213.6014 / 1000.0)
# loadmol.m:1227
                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(4.5152)
# loadmol.m:1229
                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(0)
# loadmol.m:1230
                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(0)
# loadmol.m:1231
                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(0)
# loadmol.m:1233
                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(0.937 / 1000.0)
# loadmol.m:1234
                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(0.045 / 1000.0)
# loadmol.m:1235
                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0.603 / 1000.0)
# loadmol.m:1236
                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0.0112 / 1000.0)
# loadmol.m:1237
                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('Benz_1C13')
# loadmol.m:1238
                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                    if 115 == molid:
                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(5563.9185 / 1000.0)
# loadmol.m:1240
                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(1546.8034 / 1000.0)
# loadmol.m:1241
                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(1210.0897 / 1000.0)
# loadmol.m:1242
                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(4.5152)
# loadmol.m:1244
                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(0)
# loadmol.m:1245
                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:1246
                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(0)
# loadmol.m:1248
                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(0.937 / 1000.0)
# loadmol.m:1249
                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.045 / 1000.0)
# loadmol.m:1250
                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0.603 / 1000.0)
# loadmol.m:1251
                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0.0112 / 1000.0)
# loadmol.m:1252
                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('Benz_2C13')
# loadmol.m:1253
                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                        if 116 == molid:
                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(5565.6669 / 1000.0)
# loadmol.m:1255
                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(1535.713 / 1000.0)
# loadmol.m:1256
                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(1203.373 / 1000.0)
# loadmol.m:1257
                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(4.5152)
# loadmol.m:1259
                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(0)
# loadmol.m:1260
                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(0)
# loadmol.m:1261
                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(0)
# loadmol.m:1263
                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(0.937 / 1000.0)
# loadmol.m:1264
                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0.045 / 1000.0)
# loadmol.m:1265
                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0.603 / 1000.0)
# loadmol.m:1266
                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0.0112 / 1000.0)
# loadmol.m:1267
                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('Benz_3C13')
# loadmol.m:1268
                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                            if 117 == molid:
                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(5655.4544 / 1000.0)
# loadmol.m:1270
                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(1523.6552 / 1000.0)
# loadmol.m:1271
                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(1200.0578 / 1000.0)
# loadmol.m:1272
                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(4.5152)
# loadmol.m:1274
                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(0)
# loadmol.m:1275
                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0)
# loadmol.m:1276
                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(0)
# loadmol.m:1278
                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(0.937 / 1000.0)
# loadmol.m:1279
                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(0.045 / 1000.0)
# loadmol.m:1280
                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(0.603 / 1000.0)
# loadmol.m:1281
                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0.0112 / 1000.0)
# loadmol.m:1282
                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('Benz_4C13')
# loadmol.m:1283
                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                if 118 == molid:
                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(5655.2407 / 1000.0)
# loadmol.m:1285
                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(1528.6407 / 1000.0)
# loadmol.m:1286
                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(1203.1368 / 1000.0)
# loadmol.m:1287
                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(4.5152)
# loadmol.m:1289
                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(0)
# loadmol.m:1290
                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(0)
# loadmol.m:1291
                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(0)
# loadmol.m:1293
                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(0.937 / 1000.0)
# loadmol.m:1294
                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(0.045 / 1000.0)
# loadmol.m:1295
                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0.603 / 1000.0)
# loadmol.m:1296
                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0.0112 / 1000.0)
# loadmol.m:1297
                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('Benz_7C13')
# loadmol.m:1298
                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                    if 119 == molid:
                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(5655.27 / 1000.0)
# loadmol.m:1300
                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(1502.14915 / 1000.0)
# loadmol.m:1301
                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(1186.65856 / 1000.0)
# loadmol.m:1302
                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(4.5152)
# loadmol.m:1304
                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(0)
# loadmol.m:1305
                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:1306
                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(0)
# loadmol.m:1308
                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(0.937 / 1000.0)
# loadmol.m:1309
                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.045 / 1000.0)
# loadmol.m:1310
                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0.603 / 1000.0)
# loadmol.m:1311
                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0.0112 / 1000.0)
# loadmol.m:1312
                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('Benz_N15')
# loadmol.m:1313
                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                        if 24 == molid:
                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(5.58099)
# loadmol.m:1315
                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(0.99036)
# loadmol.m:1316
                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(0.84148)
# loadmol.m:1317
                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(6.5152)
# loadmol.m:1319
                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:1320
                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:1321
                                                                                                                                                                                                                                                                                                                            molstats['mass'] = copy(118)
# loadmol.m:1322
                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('ABN')
# loadmol.m:1323
                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                            if array([15,'menthone1']) == molid:
                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(1.95343192)
# loadmol.m:1325
                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(0.694514561)
# loadmol.m:1326
                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(0.58657673)
# loadmol.m:1327
                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:1329
                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:1330
                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0)
# loadmol.m:1331
                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('Menth1')
# loadmol.m:1332
                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('menthone1')
# loadmol.m:1335
                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                if array([15,'menthone1']) == molid:
                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(1.95343192)
# loadmol.m:1337
                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(0.694514561)
# loadmol.m:1338
                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(0.58657673)
# loadmol.m:1339
                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:1341
                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:1342
                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(0)
# loadmol.m:1343
                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('Menth1')
# loadmol.m:1344
                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('menthone1')
# loadmol.m:1347
                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                    if array(['dioxolane']) == molid:
                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(2750.5369)
# loadmol.m:1350
                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(1230.8359)
# loadmol.m:1351
                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(1076.6905)
# loadmol.m:1352
                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(0.0012)
# loadmol.m:1354
                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(- 0.000648)
# loadmol.m:1355
                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.000479)
# loadmol.m:1356
                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(- 2.33e-05)
# loadmol.m:1357
                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0.000112)
# loadmol.m:1358
                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:1360
                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:1361
                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:1362
                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('dioxolane')
# loadmol.m:1363
                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                        if array(['dioxolane2']) == molid:
                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(2870.550955)
# loadmol.m:1365
                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(1201.4624)
# loadmol.m:1366
                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(1125.47327)
# loadmol.m:1367
                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(0.00048)
# loadmol.m:1369
                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(- 0.000314)
# loadmol.m:1370
                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0.000297)
# loadmol.m:1371
                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0.000743)
# loadmol.m:1372
                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(6e-05)
# loadmol.m:1373
                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:1375
                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:1376
                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:1377
                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('dioxolane2')
# loadmol.m:1378
                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                            if array(['bs1']) == molid:
                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(2000)
# loadmol.m:1381
                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(1500)
# loadmol.m:1382
                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(1200)
# loadmol.m:1383
                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:1385
                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:1386
                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0)
# loadmol.m:1387
                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('bs1')
# loadmol.m:1388
                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                if array(['bs2']) == molid:
                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(2000.523)
# loadmol.m:1390
                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(1523.573)
# loadmol.m:1391
                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(1151.17)
# loadmol.m:1392
                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:1394
                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:1395
                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(0)
# loadmol.m:1396
                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('bs1')
# loadmol.m:1397
                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                    if array(['fakementh']) == molid:
                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(1.95343192)
# loadmol.m:1400
                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(0.694514561)
# loadmol.m:1401
                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(0.58657673)
# loadmol.m:1402
                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:1404
                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:1405
                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:1406
                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('Fakementh')
# loadmol.m:1407
                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                        if array(['fakementh2']) == molid:
                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(2953.43192)
# loadmol.m:1409
                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(794.514561)
# loadmol.m:1410
                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(586.57673)
# loadmol.m:1411
                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:1413
                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:1414
                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(0)
# loadmol.m:1415
                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('Fakementh2')
# loadmol.m:1416
                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                            if array(['fakementh2abc']) == molid:
                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(dot(2.95343192,1000))
# loadmol.m:1418
                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(dot(0.794514561,1000))
# loadmol.m:1419
                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(dot(0.58657673,1000))
# loadmol.m:1420
                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:1422
                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:1423
                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:1424
                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('Fakementh2bc')
# loadmol.m:1425
                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                if array(['fakementh2bc']) == molid:
                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(dot(2.95343192,1000))
# loadmol.m:1427
                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(dot(0.794514561,1000))
# loadmol.m:1428
                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(dot(0.58657673,1000))
# loadmol.m:1429
                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(0)
# loadmol.m:1431
                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:1432
                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:1433
                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('Fakementh2bc')
# loadmol.m:1434
                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                    if array(['fakementh2ac']) == molid:
                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(dot(2.95343192,1000))
# loadmol.m:1436
                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(dot(0.794514561,1000))
# loadmol.m:1437
                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(dot(0.58657673,1000))
# loadmol.m:1438
                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:1440
                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(0)
# loadmol.m:1441
                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:1442
                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('Fakementh2ac')
# loadmol.m:1443
                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                        if array([16,'menthone2']) == molid:
                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(2.02198414)
# loadmol.m:1445
                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(0.693535995)
# loadmol.m:1446
                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(0.562135763)
# loadmol.m:1447
                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:1449
                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(4)
# loadmol.m:1450
                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:1451
                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('MenthoneSuccess2')
# loadmol.m:1452
                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                            if array(['menthCD']) == molid:
                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(2021.98414)
# loadmol.m:1454
                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(693.535995)
# loadmol.m:1455
                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(562.135763)
# loadmol.m:1456
                                                                                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(0.002)
# loadmol.m:1458
                                                                                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(0.002)
# loadmol.m:1459
                                                                                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(0.002)
# loadmol.m:1460
                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(0.002)
# loadmol.m:1461
                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0.002)
# loadmol.m:1462
                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:1464
                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:1465
                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:1466
                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('MenthoneSuccess2')
# loadmol.m:1467
                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                if array(['menthliteCD']) == molid:
                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(2021.98414)
# loadmol.m:1469
                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(693.535995)
# loadmol.m:1470
                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(562.135763)
# loadmol.m:1471
                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(- 0.00151)
# loadmol.m:1473
                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(0.001354)
# loadmol.m:1474
                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(0.001774)
# loadmol.m:1475
                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0.00174)
# loadmol.m:1476
                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0.000267)
# loadmol.m:1477
                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:1479
                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:1480
                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:1481
                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('MenthoneSuccess2')
# loadmol.m:1482
                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                    if 'myrtenal' == molid:
                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(1666.41)
# loadmol.m:1485
                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(962.37)
# loadmol.m:1486
                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(836.9)
# loadmol.m:1487
                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(- 0.0001)
# loadmol.m:1489
                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(5e-05)
# loadmol.m:1490
                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.0001)
# loadmol.m:1491
                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0.0001)
# loadmol.m:1492
                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(5e-05)
# loadmol.m:1493
                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:1495
                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:1496
                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:1497
                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('Myrtenal')
# loadmol.m:1498
                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                        if 'myrtenalbigac' == molid:
                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(1666.41)
# loadmol.m:1501
                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(962.37)
# loadmol.m:1502
                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(836.9)
# loadmol.m:1503
                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(- 0.0001)
# loadmol.m:1505
                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(5e-05)
# loadmol.m:1506
                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0.0001)
# loadmol.m:1507
                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0.0001)
# loadmol.m:1508
                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(5e-05)
# loadmol.m:1509
                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:1511
                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(0)
# loadmol.m:1512
                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(2)
# loadmol.m:1513
                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('Myrtenalbigac')
# loadmol.m:1514
                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                            if 'weirdac' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(1000)
# loadmol.m:1517
                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(470)
# loadmol.m:1518
                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(380)
# loadmol.m:1519
                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:1522
                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(0)
# loadmol.m:1523
                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:1524
                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('weird1000_470_380_ac')
# loadmol.m:1525
                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                if 'nopinone' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(1923.2)
# loadmol.m:1528
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(1297.6)
# loadmol.m:1529
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(1164.0)
# loadmol.m:1530
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(0.0001)
# loadmol.m:1532
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(- 4e-05)
# loadmol.m:1533
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(6e-05)
# loadmol.m:1534
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(- 0.0001)
# loadmol.m:1535
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(1e-06)
# loadmol.m:1536
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:1538
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:1539
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:1540
                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('nopinone')
# loadmol.m:1541
                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                    if 'alphapinene' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(1936.558)
# loadmol.m:1545
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(1228.635)
# loadmol.m:1546
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(1127.02)
# loadmol.m:1547
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(0.0001)
# loadmol.m:1549
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(- 4e-05)
# loadmol.m:1550
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(6e-05)
# loadmol.m:1551
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(- 0.0001)
# loadmol.m:1552
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(1e-06)
# loadmol.m:1553
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:1555
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:1556
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:1557
                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('alpha_pinene')
# loadmol.m:1558
                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                        if 'alphapinene' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(1936.558)
# loadmol.m:1562
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(1228.635)
# loadmol.m:1563
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(1127.02)
# loadmol.m:1564
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(0.0001)
# loadmol.m:1566
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(- 4e-05)
# loadmol.m:1567
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(6e-05)
# loadmol.m:1568
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(- 0.0001)
# loadmol.m:1569
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(1e-06)
# loadmol.m:1570
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:1572
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:1573
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:1574
                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('alpha_pinene')
# loadmol.m:1575
                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                            if 'benzaldehyde' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(5234.28)
# loadmol.m:1579
                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(1564.29)
# loadmol.m:1580
                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(1204.68)
# loadmol.m:1581
                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:1584
                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:1585
                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:1586
                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                if 'twisty' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(5873.49337)
# loadmol.m:1590
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(982.494081)
# loadmol.m:1591
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(776.14728)
# loadmol.m:1592
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(- 0.0003)
# loadmol.m:1594
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(0.0005)
# loadmol.m:1595
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(0.001)
# loadmol.m:1596
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0.0007)
# loadmol.m:1597
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0.001)
# loadmol.m:1598
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:1600
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:1601
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:1602
                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('twisty')
# loadmol.m:1603
                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                    if array(['menthveryliteCD']) == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(2021.98414)
# loadmol.m:1605
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(693.535995)
# loadmol.m:1606
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(562.135763)
# loadmol.m:1607
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(- 0.0001)
# loadmol.m:1609
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(5e-05)
# loadmol.m:1610
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.0001)
# loadmol.m:1611
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0.0001)
# loadmol.m:1612
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(5e-05)
# loadmol.m:1613
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:1615
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:1616
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:1617
                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('MenthoneSuccess2')
# loadmol.m:1618
                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                        if 17 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(30000)
# loadmol.m:1620
                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(dot(29.99,3.67))
# loadmol.m:1621
                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(dot(29.99,3.67))
# loadmol.m:1622
                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:1624
                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(0)
# loadmol.m:1625
                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(0)
# loadmol.m:1626
                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('Diatomic SrH')
# loadmol.m:1627
                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                            if array([18,'prop1']) == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(6.6424488)
# loadmol.m:1629
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(4.1635949)
# loadmol.m:1630
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(3.3653627)
# loadmol.m:1631
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(- 0.00451 / 1000)
# loadmol.m:1632
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(0.006354 / 1000)
# loadmol.m:1633
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(0.001774 / 1000)
# loadmol.m:1634
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(0.00174 / 1000)
# loadmol.m:1635
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0.000267 / 1000)
# loadmol.m:1636
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(2.35)
# loadmol.m:1638
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(0.3)
# loadmol.m:1639
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0.7)
# loadmol.m:1640
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('prop1')
# loadmol.m:1641
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['conformer'] = copy(1)
# loadmol.m:1642
                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['color'] = copy('b')
# loadmol.m:1643
                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                if array([19,'prop2']) == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(8.3934003)
# loadmol.m:1645
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(3.6485661)
# loadmol.m:1646
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(2.7782963)
# loadmol.m:1647
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(0.00316 / 1000)
# loadmol.m:1648
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(0.004485 / 1000)
# loadmol.m:1649
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(0.000797 / 1000)
# loadmol.m:1650
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0.00314 / 1000)
# loadmol.m:1651
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0.0001827 / 1000)
# loadmol.m:1652
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(2.496)
# loadmol.m:1654
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(0.309)
# loadmol.m:1655
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(0.45)
# loadmol.m:1656
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('prop2')
# loadmol.m:1657
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['shortname'] = copy('prop2')
# loadmol.m:1658
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['conformer'] = copy(2)
# loadmol.m:1659
                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['color'] = copy('y')
# loadmol.m:1660
                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                    if 219 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(8.314741)
# loadmol.m:1662
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(3.633983)
# loadmol.m:1663
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(2.763027)
# loadmol.m:1664
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(0.00316 / 1000)
# loadmol.m:1665
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(0.004485 / 1000)
# loadmol.m:1666
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.000797 / 1000)
# loadmol.m:1667
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0.00314 / 1000)
# loadmol.m:1668
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0.0001827 / 1000)
# loadmol.m:1669
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(2.496)
# loadmol.m:1671
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(0.309)
# loadmol.m:1672
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(0.45)
# loadmol.m:1673
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('1-2 propanediol Conf 2, 13C3')
# loadmol.m:1674
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['conformer'] = copy(2)
# loadmol.m:1675
                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['color'] = copy('y')
# loadmol.m:1676
                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                        if 220 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(8.377518)
# loadmol.m:1678
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(3.639168)
# loadmol.m:1679
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(2.774789)
# loadmol.m:1680
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(0.00316)
# loadmol.m:1681
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(0.004485 / 1000)
# loadmol.m:1682
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0.000797 / 1000)
# loadmol.m:1683
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0.00314 / 1000)
# loadmol.m:1684
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0.0001827 / 1000)
# loadmol.m:1685
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(2.496)
# loadmol.m:1687
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(0.309)
# loadmol.m:1688
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(0.45)
# loadmol.m:1689
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('1-2 propanediol Conf 2, 13C4')
# loadmol.m:1690
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['conformer'] = copy(2)
# loadmol.m:1691
                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['color'] = copy('y')
# loadmol.m:1692
                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                            if 221 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(8.327826)
# loadmol.m:1694
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(3.565701)
# loadmol.m:1695
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(2.723004)
# loadmol.m:1696
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(0.00316 / 1000)
# loadmol.m:1697
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(0.004485 / 1000)
# loadmol.m:1698
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(0.000797 / 1000)
# loadmol.m:1699
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(0.00314 / 1000)
# loadmol.m:1700
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0.0001827 / 1000)
# loadmol.m:1701
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(2.496)
# loadmol.m:1703
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(0.309)
# loadmol.m:1704
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0.45)
# loadmol.m:1705
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('1-2 propanediol Conf 2, 13C7?')
# loadmol.m:1706
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['conformer'] = copy(2)
# loadmol.m:1707
                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['color'] = copy('y')
# loadmol.m:1708
                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                if array([21,'prop5']) == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(8.53677)
# loadmol.m:1710
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(3.604198)
# loadmol.m:1711
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(2.778331)
# loadmol.m:1712
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(0.00275 / 1000)
# loadmol.m:1713
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(0.00529 / 1000)
# loadmol.m:1714
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(0.000751 / 1000)
# loadmol.m:1715
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0.00334 / 1000)
# loadmol.m:1716
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0.000152 / 1000)
# loadmol.m:1717
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(0.41)
# loadmol.m:1719
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1.86)
# loadmol.m:1720
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1.51)
# loadmol.m:1721
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('prop5')
# loadmol.m:1722
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['conformer'] = copy(5)
# loadmol.m:1723
                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['color'] = copy('c')
# loadmol.m:1724
                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                    if array([22,'prop6']) == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(8.327599)
# loadmol.m:1726
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(3.642001)
# loadmol.m:1727
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(2.776902)
# loadmol.m:1728
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(0.0028 / 1000)
# loadmol.m:1729
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(0.0051 / 1000)
# loadmol.m:1730
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.00076 / 1000)
# loadmol.m:1731
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0.0029 / 1000)
# loadmol.m:1732
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0.00024 / 1000)
# loadmol.m:1733
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(2.26)
# loadmol.m:1735
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(0.7)
# loadmol.m:1736
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1.2)
# loadmol.m:1737
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('prop6')
# loadmol.m:1738
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['conformer'] = copy(6)
# loadmol.m:1739
                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['color'] = copy('k')
# loadmol.m:1740
                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                        if array([23,'prop7']) == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(6.627612)
# loadmol.m:1742
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(4.146287)
# loadmol.m:1743
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(3.363345)
# loadmol.m:1744
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(- 0.005 / 1000)
# loadmol.m:1745
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(0.0062 / 1000)
# loadmol.m:1746
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0.00184 / 1000)
# loadmol.m:1747
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0.0018 / 1000)
# loadmol.m:1748
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0.00023 / 1000)
# loadmol.m:1749
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(0.98)
# loadmol.m:1751
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(0.8)
# loadmol.m:1752
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1.91)
# loadmol.m:1753
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('prop7')
# loadmol.m:1754
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['conformer'] = copy(7)
# loadmol.m:1755
                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['color'] = copy(concat([1.0,0.5,0.3]))
# loadmol.m:1756
                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                            if 'but1' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(6.604908)
# loadmol.m:1759
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(2.2290431)
# loadmol.m:1760
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(1.8153657)
# loadmol.m:1761
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(0)
# loadmol.m:1762
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(dot(0.29,0.001) / 1000)
# loadmol.m:1763
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(dot(0.37,0.001) / 1000)
# loadmol.m:1764
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(0)
# loadmol.m:1765
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(dot(0.06,0.001) / 1000)
# loadmol.m:1766
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(6.9)
# loadmol.m:1768
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:1769
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(6.9 / 3)
# loadmol.m:1770
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('1,3-butanediol Conf 1')
# loadmol.m:1771
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['conformer'] = copy(1)
# loadmol.m:1772
                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['color'] = copy(concat([0,0,1]))
# loadmol.m:1773
                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                if 26 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(6.5418393)
# loadmol.m:1776
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(2.2640596)
# loadmol.m:1777
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(1.8128437)
# loadmol.m:1778
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(0)
# loadmol.m:1779
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(dot(0.53,0.001))
# loadmol.m:1780
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(dot(0.36,0.001))
# loadmol.m:1781
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0)
# loadmol.m:1782
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(dot(0.089,0.001))
# loadmol.m:1783
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1.1)
# loadmol.m:1785
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:1786
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1.1 / 4)
# loadmol.m:1787
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('1,3-butanediol Conf 2')
# loadmol.m:1788
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['conformer'] = copy(2)
# loadmol.m:1789
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['color'] = copy(concat([0,0.5,0]))
# loadmol.m:1790
                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if 27 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(6.544798)
# loadmol.m:1793
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(2.2414905)
# loadmol.m:1794
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(1.8081532)
# loadmol.m:1795
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(0)
# loadmol.m:1796
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(dot(0.66,0.001))
# loadmol.m:1797
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(dot(0.33,0.001))
# loadmol.m:1798
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0)
# loadmol.m:1799
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0)
# loadmol.m:1800
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(0.6)
# loadmol.m:1802
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:1803
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(0.6 / 4)
# loadmol.m:1804
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('1,3-butanediol Conf 3')
# loadmol.m:1805
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['conformer'] = copy(3)
# loadmol.m:1806
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['color'] = copy(concat([1,0,0]))
# loadmol.m:1807
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if 28 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(6.497768)
# loadmol.m:1810
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(2.2398548)
# loadmol.m:1811
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(1.8098292)
# loadmol.m:1812
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(0)
# loadmol.m:1813
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(dot(0.37,0.001))
# loadmol.m:1814
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(dot(0.35,0.001))
# loadmol.m:1815
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0)
# loadmol.m:1816
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0)
# loadmol.m:1817
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(3)
# loadmol.m:1819
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:1820
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(3 / 10)
# loadmol.m:1821
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('1,3-butanediol Conf 4')
# loadmol.m:1822
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['conformer'] = copy(4)
# loadmol.m:1823
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['color'] = copy(concat([0,0.75,0.75]))
# loadmol.m:1824
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if 29 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(5.169682)
# loadmol.m:1827
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(2.525132)
# loadmol.m:1828
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(2.152733)
# loadmol.m:1829
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(0)
# loadmol.m:1830
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(dot(- 1.3,0.001))
# loadmol.m:1831
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(dot(1.71,0.001))
# loadmol.m:1832
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(0)
# loadmol.m:1833
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(dot(- 0.11,0.001))
# loadmol.m:1834
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(3.79)
# loadmol.m:1836
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(- 1.04)
# loadmol.m:1837
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0.01)
# loadmol.m:1838
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('1,3-butanediol Conf 6')
# loadmol.m:1839
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['conformer'] = copy(5)
# loadmol.m:1840
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['color'] = copy(concat([0.75,0.75,0]))
# loadmol.m:1841
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if 30 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(1.84498735)
# loadmol.m:1844
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(1.30513587)
# loadmol.m:1845
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(1.0878419)
# loadmol.m:1846
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(0)
# loadmol.m:1847
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(0)
# loadmol.m:1848
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(6.46e-05)
# loadmol.m:1849
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0)
# loadmol.m:1850
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0)
# loadmol.m:1851
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1.4)
# loadmol.m:1853
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(0.9)
# loadmol.m:1854
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1.0)
# loadmol.m:1855
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('Ribose Conformer A')
# loadmol.m:1856
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['conformer'] = copy(1)
# loadmol.m:1857
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['color'] = copy('r')
# loadmol.m:1858
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if 31 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(7.096729)
# loadmol.m:1860
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(6.976339)
# loadmol.m:1861
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(4.008201)
# loadmol.m:1862
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(- 0.0109 / 1000)
# loadmol.m:1864
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(0.0092 / 1000)
# loadmol.m:1865
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0)
# loadmol.m:1866
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0)
# loadmol.m:1867
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0)
# loadmol.m:1868
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['conformer'] = copy(1)
# loadmol.m:1869
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:1871
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:1872
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:1873
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('THFv=0')
# loadmol.m:1874
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if 32 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(7.092788)
# loadmol.m:1877
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(6.98286)
# loadmol.m:1878
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(4.008356)
# loadmol.m:1879
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(- 0.0032 / 1000)
# loadmol.m:1881
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(0.00262 / 1000)
# loadmol.m:1882
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0)
# loadmol.m:1883
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0)
# loadmol.m:1884
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0)
# loadmol.m:1885
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['conformer'] = copy(1)
# loadmol.m:1886
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:1888
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:1889
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:1890
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('THFv=1')
# loadmol.m:1891
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if 33 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(7131.297 / 1000)
# loadmol.m:1893
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(6920.427 / 1000)
# loadmol.m:1894
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(3998.977 / 1000)
# loadmol.m:1895
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(- 0.0053 / 1000)
# loadmol.m:1897
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(- 0.00683 / 1000)
# loadmol.m:1898
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(0)
# loadmol.m:1899
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(0)
# loadmol.m:1900
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0)
# loadmol.m:1901
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['conformer'] = copy(1)
# loadmol.m:1902
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:1904
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:1905
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:1906
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('THFv=2')
# loadmol.m:1907
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if 34 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(7127.92 / 1000)
# loadmol.m:1910
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(6926.919 / 1000)
# loadmol.m:1911
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(3997.018 / 1000)
# loadmol.m:1912
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(0.0024 / 1000)
# loadmol.m:1914
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(- 0.0041 / 1000)
# loadmol.m:1915
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(0)
# loadmol.m:1916
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0)
# loadmol.m:1917
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0)
# loadmol.m:1918
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['conformer'] = copy(1)
# loadmol.m:1919
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:1921
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:1922
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:1923
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('THFv=3')
# loadmol.m:1924
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if 35 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(7114.672 / 1000)
# loadmol.m:1926
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(6943.789 / 1000)
# loadmol.m:1927
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(4007.024 / 1000)
# loadmol.m:1928
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(- 0.015 / 1000)
# loadmol.m:1930
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(0.01397 / 1000)
# loadmol.m:1931
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0)
# loadmol.m:1932
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0)
# loadmol.m:1933
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0)
# loadmol.m:1934
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['conformer'] = copy(1)
# loadmol.m:1935
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:1937
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:1938
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:1939
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('THFv=4')
# loadmol.m:1940
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if 36 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(7123.69 / 1000)
# loadmol.m:1943
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(6931.98 / 1000)
# loadmol.m:1944
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(3929.83 / 1000)
# loadmol.m:1945
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(- 0.083 / 1000)
# loadmol.m:1947
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(0 / 1000)
# loadmol.m:1948
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0)
# loadmol.m:1949
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(0)
# loadmol.m:1950
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0)
# loadmol.m:1951
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['conformer'] = copy(1)
# loadmol.m:1952
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:1954
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:1955
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:1956
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('THFv=5')
# loadmol.m:1957
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if 37 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(45)
# loadmol.m:1959
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(8.5458425)
# loadmol.m:1960
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(8.5458425)
# loadmol.m:1961
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(0.71521)
# loadmol.m:1963
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(0.65)
# loadmol.m:1964
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0)
# loadmol.m:1965
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('methylacetylene')
# loadmol.m:1966
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if 38 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(4758.986 / 1000.0)
# loadmol.m:1969
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(1475.398 / 1000.0)
# loadmol.m:1970
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(1193.4018 / 1000.0)
# loadmol.m:1971
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(- 1.723 / 1000000.0)
# loadmol.m:1973
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(- 2.494 / 1000000.0)
# loadmol.m:1974
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(- 0.0819 / 1000000.0)
# loadmol.m:1975
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(- 0.1741 / 1000000.0)
# loadmol.m:1976
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:1977
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:1978
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:1979
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('benzyl alcohol')
# loadmol.m:1980
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if 'amineprop' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(8487.1037 / 1000)
# loadmol.m:1983
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(3564.3804 / 1000)
# loadmol.m:1984
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(2767.2212 / 1000)
# loadmol.m:1985
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(2.947 / 1000)
# loadmol.m:1987
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(4.237 / 1000)
# loadmol.m:1988
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.6577 / 1000)
# loadmol.m:1989
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0.1311 / 1000)
# loadmol.m:1990
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(2.411 / 1000)
# loadmol.m:1991
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:1993
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:1994
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:1995
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('1-amino-2-propanol')
# loadmol.m:1996
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if 40 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(7948.403 / 1000)
# loadmol.m:1999
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(3640.57 / 1000)
# loadmol.m:2000
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(2747.727 / 1000)
# loadmol.m:2001
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(1.5 / 1000)
# loadmol.m:2003
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(3.84 / 1000)
# loadmol.m:2004
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0.51 / 1000)
# loadmol.m:2005
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(3.23 / 1000)
# loadmol.m:2006
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0.163 / 1000)
# loadmol.m:2007
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:2009
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:2010
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:2011
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('2-amino-1-propanol conf 1')
# loadmol.m:2012
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if 41 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(6461.62 / 1000)
# loadmol.m:2015
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(4144.442 / 1000)
# loadmol.m:2016
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(3336.163 / 1000)
# loadmol.m:2017
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(- 7.02 / 1000)
# loadmol.m:2019
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(6.35 / 1000)
# loadmol.m:2020
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(1.65 / 1000)
# loadmol.m:2021
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(- 0.034 / 1000)
# loadmol.m:2022
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0.342 / 1000)
# loadmol.m:2023
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:2025
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:2026
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:2027
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('2-amino-1-propanol conf 2')
# loadmol.m:2028
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if 42 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(9769.63045 / 1000)
# loadmol.m:2031
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(868.84588 / 1000)
# loadmol.m:2032
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(818.51877 / 1000)
# loadmol.m:2033
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(24.193 / 1000)
# loadmol.m:2035
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(- 0.8843 / 1000)
# loadmol.m:2036
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(0.04627 / 1000)
# loadmol.m:2037
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(- 0.034 / 1000)
# loadmol.m:2038
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0.342 / 1000)
# loadmol.m:2039
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1.274)
# loadmol.m:2041
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(2.288)
# loadmol.m:2042
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:2043
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('hexanal conf 1')
# loadmol.m:2044
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if 43 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(5399.89397 / 1000)
# loadmol.m:2047
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(1143.248678 / 1000)
# loadmol.m:2048
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(1028.990827 / 1000)
# loadmol.m:2049
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(14.5675 / 1000)
# loadmol.m:2051
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(- 1.64943 / 1000)
# loadmol.m:2052
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.30363 / 1000)
# loadmol.m:2053
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(1.2275 / 1000)
# loadmol.m:2054
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0.064466 / 1000)
# loadmol.m:2055
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(0.515)
# loadmol.m:2057
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(2.292)
# loadmol.m:2058
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1.012)
# loadmol.m:2059
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('hexanal conf 2')
# loadmol.m:2060
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if 44 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(8975.4925 / 1000)
# loadmol.m:2063
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(933.43862 / 1000)
# loadmol.m:2064
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(898.08347 / 1000)
# loadmol.m:2065
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(72.48 / 1000000.0)
# loadmol.m:2067
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(- 2.593 / 1000000.0)
# loadmol.m:2068
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0.09094 / 1000000.0)
# loadmol.m:2069
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(- 3.005 / 1000000.0)
# loadmol.m:2070
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(- 0.00256 / 1000000.0)
# loadmol.m:2071
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1.918)
# loadmol.m:2073
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1.651)
# loadmol.m:2074
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(0.877)
# loadmol.m:2075
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('hexanal conf 3')
# loadmol.m:2076
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if 45 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(5995.20639 / 1000)
# loadmol.m:2079
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(1046.73937 / 1000)
# loadmol.m:2080
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(945.97194 / 1000)
# loadmol.m:2081
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(18.06 / 1000)
# loadmol.m:2083
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(- 2.0086 / 1000)
# loadmol.m:2084
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(0.1987 / 1000)
# loadmol.m:2085
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(1.996 / 1000)
# loadmol.m:2086
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0.049058 / 1000)
# loadmol.m:2087
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(0.983)
# loadmol.m:2089
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(2.37)
# loadmol.m:2090
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0.715)
# loadmol.m:2091
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('hexanal conf 4')
# loadmol.m:2092
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if 46 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(6116.50288 / 1000)
# loadmol.m:2095
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(1167.30037 / 1000)
# loadmol.m:2096
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(1059.54145 / 1000)
# loadmol.m:2097
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(17.889 / 1000)
# loadmol.m:2099
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(- 2.5335 / 1000)
# loadmol.m:2100
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(0.28619 / 1000)
# loadmol.m:2101
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(0.772 / 1000)
# loadmol.m:2102
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0.03319 / 1000)
# loadmol.m:2103
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(0.0461)
# loadmol.m:2105
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(2.251)
# loadmol.m:2106
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(0.833)
# loadmol.m:2107
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('hexanal conf 5')
# loadmol.m:2108
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if 47 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(4667.6175 / 1000)
# loadmol.m:2111
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(1336.76933 / 1000)
# loadmol.m:2112
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(1166.12535 / 1000)
# loadmol.m:2113
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(20.716 / 1000)
# loadmol.m:2115
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(- 5.4158 / 1000)
# loadmol.m:2116
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.8711 / 1000)
# loadmol.m:2117
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(3.324 / 1000)
# loadmol.m:2118
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0.25912 / 1000)
# loadmol.m:2119
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(0.581)
# loadmol.m:2121
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(2.469)
# loadmol.m:2122
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(0.19)
# loadmol.m:2123
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('hexanal conf 6')
# loadmol.m:2124
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if 48 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(5455.60826 / 1000)
# loadmol.m:2127
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(1055.75603 / 1000)
# loadmol.m:2128
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(937.27598 / 1000)
# loadmol.m:2129
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(41.404 / 1000)
# loadmol.m:2131
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(- 6.164 / 1000)
# loadmol.m:2132
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(0.50355 / 1000)
# loadmol.m:2133
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(2.323 / 1000)
# loadmol.m:2134
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0.118903 / 1000)
# loadmol.m:2135
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:2137
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:2138
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:2139
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('hexanal conf 7')
# loadmol.m:2140
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if 49 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(4827.91033 / 1000)
# loadmol.m:2143
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(1240.84154 / 1000)
# loadmol.m:2144
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(1159.91361 / 1000)
# loadmol.m:2145
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(40.213 / 1000)
# loadmol.m:2147
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(- 9.3475 / 1000)
# loadmol.m:2148
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(1.00661 / 1000)
# loadmol.m:2149
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(1.62 / 1000)
# loadmol.m:2150
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0.16839 / 1000)
# loadmol.m:2151
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:2153
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:2154
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:2155
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('hexanal conf 8')
# loadmol.m:2156
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if 50 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(12969.7951 / 1000)
# loadmol.m:2159
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(775.68441 / 1000)
# loadmol.m:2160
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(763.26201 / 1000)
# loadmol.m:2161
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DK'] = copy(0 / 1000)
# loadmol.m:2163
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJK'] = copy(- 7.2775 / 1000)
# loadmol.m:2164
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['DJ'] = copy(0.07102 / 1000)
# loadmol.m:2165
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaK'] = copy(1.62 / 1000)
# loadmol.m:2166
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['deltaJ'] = copy(0.16839 / 1000)
# loadmol.m:2167
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:2169
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:2170
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:2171
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('hexanal conf 9')
# loadmol.m:2172
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if 51 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(5461.5546 / 1000)
# loadmol.m:2175
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(1149.07728 / 1000)
# loadmol.m:2176
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(1102.89081 / 1000)
# loadmol.m:2177
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DK'] = copy(37.03 / 1000)
# loadmol.m:2179
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJK'] = copy(- 4.2407 / 1000)
# loadmol.m:2180
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['DJ'] = copy(0.51927 / 1000)
# loadmol.m:2181
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaK'] = copy(0 / 1000)
# loadmol.m:2182
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['deltaJ'] = copy(0.0936 / 1000)
# loadmol.m:2183
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:2185
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1)
# loadmol.m:2186
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(1)
# loadmol.m:2187
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('hexanal conf 10')
# loadmol.m:2188
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if 52 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(3961.10569 / 1000)
# loadmol.m:2191
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(1400.19125 / 1000)
# loadmol.m:2192
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(1158.63001 / 1000)
# loadmol.m:2193
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DK'] = copy(25.561 / 1000)
# loadmol.m:2195
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJK'] = copy(- 10.948 / 1000)
# loadmol.m:2196
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['DJ'] = copy(2.4272 / 1000)
# loadmol.m:2197
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaK'] = copy(4.647 / 1000)
# loadmol.m:2198
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['deltaJ'] = copy(0.70955 / 1000)
# loadmol.m:2199
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:2201
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:2202
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:2203
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('hexanal conf 11')
# loadmol.m:2204
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if 53 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(5439.6534 / 1000)
# loadmol.m:2207
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(1098.76209 / 1000)
# loadmol.m:2208
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(1050.33986 / 1000)
# loadmol.m:2209
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DK'] = copy(0 / 1000)
# loadmol.m:2211
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJK'] = copy(- 8.88272 / 1000)
# loadmol.m:2212
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['DJ'] = copy(0.6234 / 1000)
# loadmol.m:2213
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaK'] = copy(0 / 1000)
# loadmol.m:2214
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['deltaJ'] = copy(0.1283 / 1000)
# loadmol.m:2215
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:2217
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:2218
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:2219
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('hexanal conf 12')
# loadmol.m:2220
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if 54 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(34891.731 / 1000)
# loadmol.m:2222
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(9350.653 / 1000)
# loadmol.m:2223
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(8135.216 / 1000)
# loadmol.m:2224
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    #         molstats['DK'] = 0/1000;
#         molstats['DJK'] = -8.88272/1000;
#         molstats['DJ'] = 0.6234/1000;
#         molstats['deltaK'] = 0/1000;
#         molstats['deltaJ'] = 0.1283/1000;
#
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(0.046)
# loadmol.m:2232
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1.438)
# loadmol.m:2233
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(0)
# loadmol.m:2234
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('ethanol')
# loadmol.m:2235
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if 55 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(30209.04 / 1000)
# loadmol.m:2237
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(9239.112 / 1000)
# loadmol.m:2238
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(7930.497 / 1000)
# loadmol.m:2239
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        #         molstats['DK'] = 0/1000;
#         molstats['DJK'] = -8.88272/1000;
#         molstats['DJ'] = 0.6234/1000;
#         molstats['deltaK'] = 0/1000;
#         molstats['deltaJ'] = 0.1283/1000;
#
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(0.067)
# loadmol.m:2247
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(1.519)
# loadmol.m:2248
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(0.083)
# loadmol.m:2249
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('Chiral D-ethanol')
# loadmol.m:2250
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if 'benzonitrile' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #         A (MHz) 5655.2654 (72)
# B (MHz) 1546.875864 (66)
# C (MHz) 1214.40399 (10)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(5655.2654 / 1000)
# loadmol.m:2255
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(1546.875864 / 1000)
# loadmol.m:2256
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(1214.40399 / 1000)
# loadmol.m:2257
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:2258
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(0)
# loadmol.m:2259
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(0)
# loadmol.m:2260
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('Benzonitrile')
# loadmol.m:2261
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if 'benzonitrile2' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                #         A (MHz) 5655.2654 (72)
# B (MHz) 1546.875864 (66)
# C (MHz) 1214.40399 (10)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(4655.2654 / 1000)
# loadmol.m:2267
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(1546.875864 / 1000)
# loadmol.m:2268
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(1214.40399 / 1000)
# loadmol.m:2269
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:2270
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(0)
# loadmol.m:2271
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(0)
# loadmol.m:2272
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('Benzonitrile')
# loadmol.m:2273
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if 57 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    # A'] = 1347.7899(12) MHz, B'] = 1006.02030(94) MHz, C'] = 719.81749(24) MHz.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['a'] = copy(1347.7899 / 1000)
# loadmol.m:2277
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['b'] = copy(1006.0203 / 1000)
# loadmol.m:2278
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['c'] = copy(719.81749 / 1000)
# loadmol.m:2279
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    #         molstats['DK'] = 0/1000; # in MHz
#         molstats['DJK'] = -8.88272/1000;
#         molstats['DJ'] = 0.6234/1000;
#         molstats['deltaK'] = 0/1000;
#         molstats['deltaJ'] = 0.1283/1000;
#
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mua'] = copy(1)
# loadmol.m:2287
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['mub'] = copy(1)
# loadmol.m:2288
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['muc'] = copy(1)
# loadmol.m:2289
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    molstats['molname'] = copy('Argon-Benzonitrile')
# loadmol.m:2290
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    if 58 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['a'] = copy(800)
# loadmol.m:2292
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['b'] = copy(10.5)
# loadmol.m:2293
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['c'] = copy(10.5)
# loadmol.m:2294
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mua'] = copy(1)
# loadmol.m:2296
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['mub'] = copy(0)
# loadmol.m:2297
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['muc'] = copy(0)
# loadmol.m:2298
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        molstats['molname'] = copy('Diatomic CaF avbout')
# loadmol.m:2299
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if 59 == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['a'] = copy(15272.17 / 1000)
# loadmol.m:2301
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['b'] = copy(1161.46 / 1000)
# loadmol.m:2302
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['c'] = copy(1119.93 / 1000)
# loadmol.m:2303
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mua'] = copy(1)
# loadmol.m:2305
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['mub'] = copy(1)
# loadmol.m:2306
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['muc'] = copy(1)
# loadmol.m:2307
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            molstats['molname'] = copy('1pent_guess')
# loadmol.m:2308
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            if 'isoprene' == molid:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['a'] = copy(dot(q,15272.17) / 1000)
# loadmol.m:2310
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['b'] = copy(1161.46 / 1000)
# loadmol.m:2311
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['c'] = copy(1119.93 / 1000)
# loadmol.m:2312
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mua'] = copy(1)
# loadmol.m:2314
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['mub'] = copy(1)
# loadmol.m:2315
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['muc'] = copy(1)
# loadmol.m:2316
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats['molname'] = copy('1pent_guess')
# loadmol.m:2317
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                molstats=0
# loadmol.m:2319
    

    if type(molstats) is dict:
        molstats['molid'] = copy(molid)
# loadmol.m:2322
        molstats['theory'] = copy(1)
# loadmol.m:2323
        if molstats['a'] < 50:
            molstats['a'] = copy(dot(molstats['a'],1000))
# loadmol.m:2325
            molstats['b'] = copy(dot(molstats['b'],1000))
# loadmol.m:2326
            molstats['c'] = copy(dot(molstats['c'],1000))
# loadmol.m:2327

            if 'DK' in molstats:
                molstats['DK'] = copy(dot(molstats['DK'],1000))
# loadmol.m:2329
                molstats['DJK'] = copy(dot(molstats['DJK'],1000))
# loadmol.m:2330
                molstats['DJ'] = copy(dot(molstats['DJ'],1000))
# loadmol.m:2331
                molstats['deltaK'] = copy(dot(molstats['deltaK'],1000))
# loadmol.m:2332
                molstats['deltaJ'] = copy(dot(molstats['deltaJ'],1000))
# loadmol.m:2333

        if 'mua' not in molstats:
            molstats['mua'] = copy(1)
# loadmol.m:2337
            molstats['mub'] = copy(1)
# loadmol.m:2338
            molstats['muc'] = copy(1)
# loadmol.m:2339

        if 'molname' not in molstats:
            molstats['molname'] = copy(molid)
# loadmol.m:2342
        molstats=updatemolstats(molstats)
# loadmol.m:2344
    return molstats, allcases
    