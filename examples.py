import thermohipy as th

# Validation 数据验证：
# th.Datalist(T_list, heating_rate_list, dadT_list, unit)
alpha = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
beta = [5, 10, 30]
data_object = [th.DataList([264.8, 269.75, 284.65], [5, 10, 30], 
                        [0.00271, 0.00257, 0.00246], unit='c'),
               th.DataList([294.65, 301.15, 317.5], beta, 
                        [0.00394, 0.00375, 0.00359], unit='c'),
               th.DataList([317.9, 325.6, 343], beta, 
                        [0.00459, 0.00437, 0.0042], unit='c'),
               th.DataList([612.15, 620.90, 639.15], beta, 
                        [0.00483, 0.0046, 0.00444], unit='k'),
               th.DataList([632.95, 642.70, 661.70], beta, 
                        [0.00475, 0.00453, 0.00439], unit='k'),         
               th.DataList([654.75, 665.50, 685.15], beta, 
                        [0.00438, 0.0042, 0.0041], unit='k'),
               th.DataList([761.00, 783.96, 820.40], beta, 
                        [0.00376, 0.00363, 0.00357], unit='f'),         
               th.DataList([816.98, 841.93, 876.65], beta, 
                        [0.00289, 0.00282, 0.00283], unit='f'),
               th.DataList([895.28, 919.31, 954.05], beta, 
                        [0.00175, 0.00176, 0.00185], unit='f')]


analysis = th.KineticAnalysis(alpha, data_object)    # 表明，数据已传入热分析类中
picplot = th.FittingPlot(alpha, data_object, analysis)
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




