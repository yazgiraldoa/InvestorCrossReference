import gspread
import pandas as pd


def connect():
    """Function that connects to Google Sheets"""
    gc = gspread.service_account(filename="/Users/yazmingiraldo/Documents/phantomData/credentials.json")
    sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1EYKGkNtVmbk_aQQdSLinu5dsmapqyfOticRswseOsE4/edit?usp=sharing")
    print("Connected to Google Sheets")
    return sh


def create(sh):
    excel = "/Users/yazmingiraldo/Downloads/talisman.xlsx"
    df = pd.read_excel(excel, skiprows=7, header=1)
    df = df.fillna('')
    sh.sheet1.update([df.columns.values.tolist()] + df.values.tolist())
    print("Created successfully")


def update(sh):
    excel = "/Users/yazmingiraldo/Downloads/rookmotion2.xlsx"
    df = pd.read_excel(excel, skiprows=9)
    df = df.fillna('')
    sh.sheet1.append_rows([df.columns.values.tolist()] + df.values.tolist())
    print("Updated successfully")


if __name__ == '__main__':
    sh = connect()
    create(sh)
