class DataList:
    """
        A class for storing thermal analysis data at a specific conversion level (α).
        Datalist(temperature, beta, dadT, unit = "c")

        Parameters
        ----------
        temperature : list[float]
            Temperature list corresponding to each heating rate point.
                beta : list[float]
            Heating rate list (β), typically in K/min.
        dadT : list[float]
            Reaction rate list (dα/dt), corresponding to the same temperatures.
        unit : str, optional
            Temperature unit indicator:
                - 'c' : data collected in Celsius
                - 'f' : data collected in Fahrenheit
                - 'k' : data already in Kelvin
                - Default is 'c'. 
                - If 'unit' is not entered, the temperature will be assumed to be in Celsius 
                    and converted to Kelvin for calculations.
        Example
        -------
            >>> from thermohipy import DataList
            >>> alpha_list = [0.1, 0.3, 0.5] #(0 < alpha < 1)
            >>> beta = [1, 2, 5, 10]
            >>> t_a1, t_a2,t_a3 = [T1, T2, T3, T4],[T5, T6, T7, T8], [T9, T10, T11, T12]
            >>> dadT1, dadT2, dadT3 = [a, b, c, d], [e, f, g, h], [i, j, k, l]
            >>> data1 = DataList(t_a1, beta, dadT1)
            >>> data2 = DataList(t_a2, beta, dadT2)
            >>> data3 = DataList(t_a3, beta, dadT3)
            >>> data_object =[data1, data2, data3]
                      
    """
    #class 2 数据列表化，将单一的温度，升温速率和dadT生成列表
    def __init__(self,temperature, beta, dadT, unit = "c"):    
        self.temperature = list(temperature)    # 对应温度列表
        if unit is not None and unit.lower() == "c":
            self.temperature= [ t + 273.15 for t in self.temperature]
        if unit is not None and unit.lower() == "f":
            self.temperature= [ (t - 32) / 1.8 + 273.15 for t in self.temperature]
        elif unit not in (None, "c", "C", "k", "K",'f','F'):
            raise ValueError("unit 参数只能是 'c' 或 'k'")
        self.beta = list(beta)  #对应升温速率列表
        self.dadT = list(dadT)  #对应da/dT列表
