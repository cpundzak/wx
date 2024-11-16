class wSetGet:
    _CDate = []
    _CTime = []
    _OutTemp = []
    _HighTempIndex = 0
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
    def __init__(self,cdate,ctime,outTemp,dewPoint,humidity,rainRate,todayRain,windDir,windSpd,SLP,strikeToday,strikeDist,strikeFreq):
       self._CDate.append(cdate)
       self._CTime.append(ctime)
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
    def getHighTempIndex(self):
           return self._HighTempIndex
    def getDew(self,i):
            return self._Dew[i]
    def getHum(self, i):
            return self._Hum[i]
    def getRainRate(self,i):
            return self._RainRate[i]
    def getTodayRain(self,i):
            return _TodayRain[i]
    def getWindDir(self,i):
            return self._WindDir[i]
    def getWindSpeed(self,i):
            return self._WindSpeed[i]
    def getSLP(self,i): 
            return _SLP[i]
    def getStrikeToday(self,i):
            return _StrikeToday[i]
    def getStrikeDest(self,i):
            return _StrikeDist[i]
    def getStrikeFreq(self,i):
            return _StrikeFreq[i] 
    def getLen(self):
            return len(self._OutTemp)
    def setHighTempIndex(self, i):
           self._HighTempIndex = i
    def setLowTempIndex(self, i):
           self._LowTempIndex