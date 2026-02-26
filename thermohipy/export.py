import numpy as np
import os
import pandas as pd
from .thermoanalysis import KineticAnalysis

class ExportData:
    """
    ExportData
    ----------
    
        A utility class for exporting kinetic analysis results.
        ExportData(alpha_list, data_objects, analysis)

        Parameters
        ----------
        alpha_list : list of float
            Conversion values, e.g. [α1, α2, α3, ...]
        data_objects : list of DataList
            A list of DataList instances. Each DataList contains the 
            corresponding temperature, heating rate (β), and dα/dT data 
            for a given experimental condition.

        analysis : KineticAnalysis
            An instance of KineticAnalysis used to perform regression 
            and provide activation energy calculation results.
    
        Methods
        -------
        The following methods are available. By default, results are returned 
        as a dictionary. If `save_excel=True`, the results are also saved as 
        an `.xlsx` file and the absolute file path is printed in the terminal.

            1. export_fwo(save_excel=False)
            2. export_kas(save_excel=False)
            3. export_starink(save_excel=False)
            4. export_friedman(save_excel=False)
            5. export_vyazovkin(save_excel=False)

        Returns
        -------
        dict
            A dictionary containing:
                - Kinetic parameters (Ea, k, b, R²) 
                - Fitting or regression data points
        Example
        -------
            >>> from thermohipy import ExportData
            >>> exporter = ExportData(alpha, data_object, analysis)
            >>> results = exporter.export_fwo(save_excel=True)
    """
    def __init__(self, alpha_list, data_objects, analysis: KineticAnalysis):
        self.alpha_list = list(alpha_list)
        self.objects_data = list(data_objects)
        self.analysis = analysis
    
    def export_iso_method(self, name_method, analysis_method, save_excel=False):
        # name_method: FWO, KAS, Starink, Friedman 方法名，Vyazovkin因为数据不同需要额外写一个。
        results = analysis_method(return_data=True)
        kinetic_columns = ['Ea (kJ/mol)', 'b(intercept)', 'k(slope)', 'r^2  ']
        kinetic_index = self.alpha_list
        ea, b, k, r2 = [], [], [], []
        for a in results[0]:
            ea.append(results[0][a]['Ea'])
            b.append(results[0][a]['b'])
            k.append(results[0][a]['k'])
            r2.append(results[0][a]['r^2'])
        datas1 = np.array([ea, b, k, r2])
        kinetic_parameters = pd.DataFrame(data = datas1.T, index = kinetic_index, columns=kinetic_columns)
        kinetic_parameters.index.name = 'α'
        x, y = [], []
        for b in results[1]:
            x.append(results[1][b]['x'])
            y.append(results[1][b]['y'])
        datas_x, datas_y = np.array(x), np.array(y)
        beta_x = [f'x_{i+1}' for i in range(datas_x.shape[1])]
        scatte_plots_x = pd.DataFrame(data=datas_x,index=kinetic_index,columns=beta_x)
        scatte_plots_x.index.name = 'α'
        beta_y = [f'y_{i+1}' for i in range(datas_y.shape[1])]
        scatte_plots_y= pd.DataFrame(data = datas_y, index = kinetic_index, columns=beta_y)
        scatte_plots_y.index.name = 'α'
        scatte_plots_xy = pd.concat([scatte_plots_x, scatte_plots_y], axis=1)
        final_results = {
            'Kinetic_Parameters': kinetic_parameters,
            f'{name_method}_Points': scatte_plots_xy
        }
        if save_excel:
            file_name = f'{name_method}_Results.xlsx'
            file_path = os.path.abspath(file_name)
            with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
                final_results['Kinetic_Parameters'].to_excel(writer, sheet_name='Kinetic_Parameters')
                final_results[f'{name_method}_Points'].to_excel(writer, sheet_name=f'{name_method}_Points')
            print(f"{name_method}_Results.xlsx is saved at:\n{file_path}")
        return final_results
    
    def export_fwo(self, save_excel=False):
        return self.export_iso_method('FWO', self.analysis.fwo_ea, save_excel)

    def export_kas(self, save_excel=False):
        return self.export_iso_method('KAS', self.analysis.kas_ea, save_excel)

    def export_starink(self, save_excel=False):
        return self.export_iso_method('Starink', self.analysis.starink_ea, save_excel)

    def export_friedman(self, save_excel=False):
        return self.export_iso_method('Friedman', self.analysis.friedman_ea, save_excel)

    def export_vyazovkin(self, save_excel=False):
        results = self.analysis.vyazovkin_ea(return_data=True)
        kinetic_index = self.alpha_list
        kinetic_columns = ['Ea (kJ/mol)']
        ea =[]
        for i in results[0]:
            ea.append(results[0][i]['Ea'])
        datas1 = np.array([ea]).T
        x, y = [], []
        for i in results[1]:
            x.append(results[1][i]['x'])
            y.append(results[1][i]['y'])
        datas_x, datas_y = np.array(x), np.array(y)
        kinetic_parameters = pd.DataFrame(data = datas1, index = kinetic_index, columns=kinetic_columns)
        kinetic_parameters.index.name = 'α'

        index_x = [f'x(α={i})' for i in kinetic_index]
        curve_plots_x = pd.DataFrame(data=datas_x.T,columns=index_x)
        curve_plots_x .index.name = 'α'

        index_y = [f'y(α={i})' for i in kinetic_index]
        curve_plots_y= pd.DataFrame(data = datas_y.T, columns=index_y)
        curve_plots_y.index.name = 'points'
        curve_plots_xy = pd.concat([curve_plots_x, curve_plots_y], axis=1)
        curve_plots_xy.index.name = 'points'
        final_results = {
            'Kinetic_Parameters': kinetic_parameters,
            'Vyazovkin_Points': curve_plots_xy
        }
        if save_excel:
            file_name = 'Vyazovkin_Results.xlsx'
            file_path = os.path.abspath(file_name)
            with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
                final_results['Kinetic_Parameters'].to_excel(writer, sheet_name='Kinetic_Parameters')
                final_results['Vyazovkin_Points'].to_excel(writer, sheet_name='Vyazovkin_Points')
            print(f"Vyazovkin_Results.xlsx is saved at:\n{file_path}")
        return final_results