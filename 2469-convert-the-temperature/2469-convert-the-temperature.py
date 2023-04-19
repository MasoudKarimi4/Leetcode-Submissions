class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        
        others = []
        
        others.append(celsius+273.15)
        
        fahrenheit = (9*(celsius))/5
        fahrenheit += 32
        others.append(fahrenheit)
        
        return others 