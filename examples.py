import thermohipy as th

# Validation 数据验证：
alpha = [0.1, 0.5, 0.9]
data_object = [DataList([241.9, 251.85, 263.5, 270.9], [5,10,20,30], 
                        [0.00366, 0.00358, 0.00353, 0.00348], unit='c'),
               DataList([291.25, 302.3, 314.3, 322.45], [5,10,20,30], 
                        [0.01318, 0.01297, 0.01292, 0.01274], unit='c'),
               DataList([321.9, 333.55, 345.6, 354.2], [5,10,20,30],
                        [0.00942, 0.00927, 0.00925, 0.00914], unit='c')]


analysis = KineticAnalysis(alpha, data_object)    # 表明，数据已传入热分析类中
picplot = FittingPlot(alpha, data_object, analysis)
pic1 = picplot.fwoplot()
pic2 = picplot.kasplot()
pic3 = picplot.starinkplot()
pic4 = picplot.friedmanplot()
pic5 = picplot.vyazovkinplot()

# result5_data = result5[0]
# result5_raw_data = result5[1]
# print(result5_data, result5_raw_data)


# show the results and plotting data
# if return_data is True the results is a tuple(results, raw data for plotting)) consists of 2 dict.
results1 = analysis.fwo_ea(return_data = True)
results2 = analysis.kas_ea(return_data = True)
results3 = analysis.starink_ea(return_data = True)
results4 = analysis.friedman_ea(return_data = True)
results5 = analysis.vyazovkin_ea(return_data = True)

results1_data = results1[0]
results1_raw_data = results1[1]
print(results1_data, results1_raw_data)
# Note that for all methods except the Vyazovkin method, the returned raw data is intended for scatter plots (depending on the number of heating). 
# For the Vyazovkin method, the returned raw data is intended for curve plots (with 100 points).
results5_data = results5[0]
results5_raw_data = results5[1]
print(results5_data, results5_raw_data)




