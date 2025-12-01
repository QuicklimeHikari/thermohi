import thermohipy as th

# th.Datalist(T_list, heating_rate_list, dadT_list, unit)
# unit = 'c' means Celcisus, unit = 'f' means Fahrenheit, unit = 'k' or blank means Kelvin

alpha = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]   # conversion value
beta = [5, 10, 30]  # heating rates
data_object = [th.DataList([264.8, 269.75, 284.65], beta, 
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
analysis = th.KineticAnalysis(alpha, data_object)
<<<<<<< HEAD

# plots drawing
# picplot = th.FittingPlot(alpha, data_object, analysis)
# pic1 = picplot.fwoplot()
# pic2 = picplot.kasplot()
# pic3 = picplot.starinkplot()
# pic4 = picplot.friedmanplot()
# pic5 = picplot.vyazovkinplot()

# show the results only (return data = True, except Vyazovkin method)
results1 = analysis.fwo_ea(return_data = False)
print(type(results1))   # <class 'dict'>
print("_" *15, "return_data = False", "_" *15)
print("alpha Ea         k           b      r^2")
print("_"*50)
for key in results1:
    ea = results1[key]['Ea = '] # class of results1[key] is also 'dict'
    k = results1[key]['k = ']
    b = results1[key]['b = ']
    r2 = results1[key]['r^2 = ']
    print(key, f"{ea:.2f}, {k:.4f}, {b:.4f}, {r2:.4f}")
print("_"*25,"end","_"*25,"\n")


# show the results and plotting data （return data = True, except Vyazovkin method）
# if return_data is True the results is a tuple(results, raw data for plotting)) consists of 2 dict.
results2 = analysis.fwo_ea(return_data = True)
=======

# plots drawing
picplot = th.FittingPlot(alpha, data_object, analysis)
pic1 = picplot.fwoplot()
pic2 = picplot.kasplot()
pic3 = picplot.starinkplot()
pic4 = picplot.friedmanplot()
pic5 = picplot.vyazovkinplot()

# show the results only
results1 = analysis.fwo_ea(return_data = False)
print(type(results1))   # <class 'dict'>
print("_" *15, "return_data = False", "_" *15)
print("alpha Ea         k           b      r^2")
print("_"*50)
for key in results1:
    ea = results1[key]['Ea = '] # class of results1[key] is also 'dict'
    k = results1[key]['k = ']
    b = results1[key]['b = ']
    r2 = results1[key]['r^2 = ']
    print(key, f"{ea:.2f}, {k:.4f}, {b:.4f}, {r2:.4f}")
print("_"*25,"end","_"*25,"\n")


# show the results and plotting data
# if return_data is True the results is a tuple(results, raw data for plotting)) consists of 2 dict.
results2 = analysis.kas_ea(return_data = True)
>>>>>>> fix-detached
results2_data = results2[0] # Ea, k, b, and r2
results2_raw_data = results2[1] # plot points
print("_" *15, "return_data = True", "_" *15)
print("alpha Ea         k           b      r^2")
print("_"*50)
for key in results2_data:
    ea = results2_data[key]['Ea = '] # class of results1[key] is also 'dict'
    k = results2_data[key]['k = ']
    b = results2_data[key]['b = ']
    r2 = results2_data[key]['r^2 = ']
    print(key, f"{ea:.2f}, {k:.4f}, {b:.4f}, {r2:.4f}")
print("_"*25,"end","_"*25,"\n")

print("_" *25, "points for linear fitting -x", "_" *25) 
for key in results2_raw_data:
    print(key, results2_raw_data[key]['x'])
print("_" *25, "points for linear fitting -y", "_" *25) 
for key in results2_raw_data:
    print(key, results2_raw_data[key]['y'])
# Note that for all methods except the Vyazovkin method, the returned raw data is intended for scatter plots (depending on the number of heating). 


### Vyazovkin method ###
# return data structure(tuple): ({'alpha':{'Ea = ': value}, ...}, {'alpha':{'x': value, 'y': value},...})
# For the Vyazovkin method, the returned raw data is intended for curve plots (with 100 points).
<<<<<<< HEAD
results3 = analysis.vyazovkin_ea(return_data = True)
results3_data = results3[0] # tuple[0] = {'alpha':{'Ea = ': value}, 'alpha2':{'Ea = ': value}, ...}
results3_raw_data = results3[1] # tuple[1] = {'alpha1':{'x': value, 'y': value}, 'alpha2':{'x': value, 'y': value}...}
print("_" *15, "Vyazovkin method", "_" *15)
for key in results3_data:
    ea = results3_data[key]['Ea = '] 
    print(key, f"{ea:.2f}")
print("_"*25,"end","_"*25,"\n")

print("_" *25, "points for linear fitting -x", "_" *25) 
for key in results3_raw_data:
    print(key, results3_raw_data[key]['x'])
print("_" *25, "points for linear fitting -y", "_" *25) 
for key in results3_raw_data:
    print(key, results3_raw_data[key]['y'])
print("_"*25,"end","_"*25,"\n")
=======



>>>>>>> fix-detached




