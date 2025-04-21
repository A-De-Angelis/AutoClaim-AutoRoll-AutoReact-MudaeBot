token = ''
channelId = ''     
serverId = ''

rollCommand= 'wa' # possible values: wa, ha, wg, hg, wx, hx. Set one only.
desiredKakeras = ['kakeraP','kakeraY','kakeraO','kakeraR','kakeraW','kakeraL']
desiredSeries = ['One Piece','Dragon Ball Z','Dumbbell Nan Kilo Moteru?'] # Characters from these series will be claimed instantly
kakeraClaim = '200' #Set this to 0 to disable claiming any character with this minimum kakera threshold and instead only claim cards from desired series.
# If kakeraClaim is set above 0, desired series will still be claimed even if those cards are below the threshold.

pokeRoll = True #Set this to False to disable pokeRolls
repeatMinute = '25' # 00 to 59 are valid minute values