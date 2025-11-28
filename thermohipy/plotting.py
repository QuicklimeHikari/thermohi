import numpy as np
import matplotlib.pyplot as plt   
from .thermoanalysis import KineticAnalysis
class FittingPlot:
    """
A class for plotting scatter data and fitted regression curves 
based on kinetic analysis results.

Parameters
----------
alpha_list : list[float]
List of conversion fractions (α values).
data_objects : list[DataList]
List of `DataList` instances, each containing temperature, 
heating rate (β), and reaction rate (dα/dt) data for a specific α.
analysis : KineticAnalysis
An instance of `KineticAnalysis` used to perform the fitting 
and provide the regression results.
"""
    def __init__(self, alpha_list, data_objects, analysis: KineticAnalysis):
        self.alpha_list = list(alpha_list)
        self.objects_data = list(data_objects)
        self.analysis = analysis

    def fwoplot(self):
        results = self.analysis.fwo_ea(return_data = True)
        figure = plt.figure(figsize= (8,6))
        axes = plt.subplot(1,1,1)
        axes.set_xlabel("1/T",fontsize = 14, fontname = 'arial')
        axes.set_ylabel('ln(β)',fontsize = 14, fontname = 'arial')
        scatterdata = results[1]
        plotdata = results[0]
        for key1,key2 in zip(scatterdata,plotdata):
            x = scatterdata[key1].get('x')
            y = scatterdata[key1].get('y')
            x_min, x_max = np.min(x), np.max(x)
            x_plot = np.linspace(x_min, x_max,10)
            axes.scatter(x,y)
            axes.plot(x_plot, plotdata[key2].get('k = ') * x_plot + plotdata[key2].get('b = ' ))
            plt.draw()   # 刷新绘图
            plt.pause(0.2)  # 暂停 0.3 秒，看清楚每条线
        plt.ioff()  # 关闭交互模式
        plt.show()

    def kasplot(self):
        results = self.analysis.kas_ea(return_data = True)
        figure = plt.figure(figsize= (8,6))
        axes = plt.subplot(1,1,1)
        axes.set_xlabel("1/T",fontsize = 14, fontname = 'arial')
        axes.set_ylabel('ln(β/T$^{2}$)',fontsize = 14, fontname = 'arial')
        scatterdata = results[1]
        plotdata = results[0]
        for key1,key2 in zip(scatterdata,plotdata):
            x = scatterdata[key1].get('x')
            y = scatterdata[key1].get('y')
            x_min, x_max = np.min(x), np.max(x)
            x_plot = np.linspace(x_min, x_max,10)
            axes.scatter(x,y)
            axes.plot(x_plot, plotdata[key2].get('k = ') * x_plot + plotdata[key2].get('b = ' ))
            plt.draw()   # 刷新绘图
            plt.pause(0.2)  # 暂停 0.3 秒，看清楚每条线
        plt.ioff()  # 关闭交互模式
        plt.show()
    
    def starinkplot(self):
        results = self.analysis.starink_ea(return_data = True)
        figure = plt.figure(figsize= (8,6))
        axes = plt.subplot(1,1,1)
        axes.set_xlabel("1/T",fontsize = 14, fontname = 'arial')
        axes.set_ylabel('ln(β/T$^{1.92}$)',fontsize = 14, fontname = 'arial')
        scatterdata = results[1]
        plotdata = results[0]
        for key1,key2 in zip(scatterdata,plotdata):
            x = scatterdata[key1].get('x')
            y = scatterdata[key1].get('y')
            x_min, x_max = np.min(x), np.max(x)
            x_plot = np.linspace(x_min, x_max,10)
            axes.scatter(x,y)
            axes.plot(x_plot, plotdata[key2].get('k = ') * x_plot + plotdata[key2].get('b = ' ))
            plt.draw()   # 刷新绘图
            plt.pause(0.2)  # 暂停 0.3 秒，看清楚每条线
        plt.ioff()  # 关闭交互模式
        plt.show()

    def friedmanplot(self):
        results = self.analysis.friedman_ea(return_data = True)
        figure = plt.figure(figsize= (8,6))
        axes = plt.subplot(1,1,1)
        axes.set_xlabel("1/T",fontsize = 14, fontname = 'arial')
        axes.set_ylabel('ln(da/dt)',fontsize = 14, fontname = 'arial')
        scatterdata = results[1]
        plotdata = results[0]
        for key1,key2 in zip(scatterdata,plotdata):
            x = scatterdata[key1].get('x')
            y = scatterdata[key1].get('y')
            x_min, x_max = np.min(x), np.max(x)
            x_plot = np.linspace(x_min, x_max,10)
            axes.scatter(x,y)
            axes.plot(x_plot, plotdata[key2].get('k = ') * x_plot + plotdata[key2].get('b = ' ))
            plt.draw()   # 刷新绘图
            plt.pause(0.2)  # 暂停 0.3 秒，看清楚每条线
        plt.ioff()  # 关闭交互模式
        plt.show()

    def vyazovkinplot(self):
        results = self.analysis.vyazovkin_ea (return_data = True)
        axes = plt.subplot(1,1,1)
        axes.set_xlabel("E(kJ/mol)",fontsize = 14, fontname = 'arial')
        axes.set_ylabel('$\Phi$(E)',fontsize = 14, fontname = 'arial')
        plotdata = results[1]
        for key in plotdata:
            x = plotdata[key].get('x')
            y = plotdata[key].get('y')
            axes.plot(x,y)
            plt.draw()   # 刷新绘图
            plt.pause(0.2)  # 暂停 0.3 秒，看清楚每条线
        plt.draw()
        plt.show()