import thermohi_hikari as th

## datalist
alpha = [0.1, 0.5, 0.9]
temp_alpha1 = [241.9, 251.85, 263.5, 270.9] # celsius(C)
temp_alpha2 = [556.25, 576.14, 597.74, 612.41] # fahrenheit(F)
temp_alpha3 = [595.05, 606.7, 618.75, 627.35] # kelvin(K)
beta = [5,10,20,30]
dadT_alpha1 = [0.00366, 0.00358, 0.00353, 0.00348]
dadT_alpha2 = [0.01318, 0.01297, 0.01292, 0.01274]
dadT_alpha3 = [0.00942, 0.00927, 0.00925, 0.00914]

data_object = [th.DataList(temp_alpha1, beta, dadT_alpha1),
               th.DataList(temp_alpha2, beta, dadT_alpha2, 'f'),
               th.DataList(temp_alpha3, beta, dadT_alpha3, unit='k')]

## kinetic analysis(fwo,kas,starink,friedman)
analysis = th.KineticAnalysis(alpha, data_object)
plots = th.FittingPlot(alpha,data_object,analysis)
results1 = analysis.fwo_ea()
print(results1)
pic1 = plots.fwoplot()
results2 = analysis.kas_ea()
print(results2)
pic2 = plots.kasplot()
results3 = analysis.starink_ea()
print(results3)
pic1 = plots.starinkplot()
results4 = analysis.friedman_ea()
print(results4)
pic1 = plots.friedmanplot()

## raw data export
# If you want to export the data and draw the graph by yourself
results5, raw_data = analysis.fwo_ea(return_data = True)
for i in raw_data:
    print(raw_data[i]) # {'x': [x1, x2, x3, x4]，'y': [y1, y2, y3, y4]}

## linear fitting function(including r^2)
x_1 = raw_data[alpha[0]].get('x')
y_1 = raw_data[alpha[0]].get('y')
k, b, r2 = th.r_square_xy(x_1,y_1)
print(f"The regression equation is y = {k:.4f} * x + {b:.4f}, r^2 is {r2:.4f}.")




