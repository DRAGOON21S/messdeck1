import pandas as pd
#from django import path

def convert_excel_to_csv(excel_file, csv_file):
    try:
        df = pd.read_excel(excel_file)

        df.to_csv(csv_file, index=False)

        print(f"Conversion successful! {excel_file} has been converted to {csv_file}")
    except Exception as e:
        print(f"Error: {e}")

convert_excel_to_csv('Z:/sutt task 3/virtuall/mess_sutt/messdeck/mess menu/Mess_Menu.xlsx', 'messmenu.csv')
