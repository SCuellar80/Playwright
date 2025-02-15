import openpyxl

class ExcelReader:
    def __init__(self, file_path=None): #filepath is optional, when not passed it takes the default defined here.
        if file_path == None:
            file_path = "challenge.xlsx"
        self.file_path = file_path

    def read_excel_data(self):
        # Cargar el archivo de Excel
        workbook = openpyxl.load_workbook(self.file_path)
        sheet = workbook.active

        # Lista para almacenar los datos
        data = []

        # Iterar sobre las filas del archivo de Excel
        for row in sheet.iter_rows(min_row=2, values_only=True):  # if first line is headers, then start from 2
            First_Name = row[0]  # Primera columna
            Last_Name  = row[1]  # Segunda columna
            Company_Name = row[2]  # Tercera columna
            Role_in_Company = row[3]
            Address = row[4]
            Email = row[5]
            Phone_Number = row[6]
            # Agregar los datos a la lista como una tupla
            data.append((First_Name, Last_Name, Company_Name,Role_in_Company,Address,Email,Phone_Number))
        return data

# Ejemplo de uso
if __name__ == "__main__":
    #file_path = "data.xlsx"  # Ruta al archivo de Excel
    #excel_reader = ExcelReader(file_path)
    excel_reader = ExcelReader() # if file_path not specified, it takes the defined in init in the class ExcelReader
    data = excel_reader.read_excel_data()

    # Imprimir los datos leídos
    for item in data:
        print(item)