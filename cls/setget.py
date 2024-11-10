
class wSetGet:
    _CTime = []
    _OutTemp = []
    _Dew = []
    _Hum = []
    _RainRate = []
    _TodayRain = []
    _WindDir = []
    _WindSpeed = []
    _SLP = []
    _StrikeToday = []
    _StrikeDist = []
    _StrikeFreq = []
    def __init__(self,curtime,outTemp,dewPoint,humidity,rainRate,todayRain,windDir,windSpd,SLP,strikeToday,strikeDist,strikeFreq):
       self._CTime.append(curtime)
       self._OutTemp.append(outTemp)
       self._Dew.append(dewPoint)
       self._Hum.append(humidity)
       self._RainRate.append(rainRate)
       self._TodayRain.append(todayRain)
       self._WindDir.append(windDir)
       self._WindSpeed.append(windSpd)
       self._SLP.append(SLP)
       self._StrikeToday.append(strikeToday)
       self._StrikeDist.append(strikeDist)
       self._StrikeFreq.append(strikeFreq)
    def getTime(self,i):
            return self._CTime[i]
    def getOutTemp(self,i):
            return self._OutTemp[i]
    def getDew(self,i):
            return self._Dew[i]
    def getHum(self):
            return self._Hum[i]
    def getRainRate(self):
            return self._RainRate[i]
    def getTodayRain(self):
            return _TodayRain[i]
    def getWindDir(self):
            return self._WindDir[i]
    def getWindSpeed(self):
            return self._WindSpeed[i]
    def getSLP(self): 
            return _SLP[i]
    def getStrikeToday(self):
            return _StrikeToday[i]
    def getStrikeDest(self):
            return _StrikeDist[i]
    def getStrikeFreq(self):
            return _StrikeFreq[i] 