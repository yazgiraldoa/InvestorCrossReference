import gspread
import json
from time import sleep


def connect():
    """Function that connects to Google Sheets"""
    gc = gspread.service_account(filename="/Users/yazmingiraldo/Documents/phantomData/credentials.json")
    sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1EYKGkNtVmbk_aQQdSLinu5dsmapqyfOticRswseOsE4/edit?usp=sharing")
    print("Connected to Google Sheets")
    return sh


def techstars_investors():
    with open("investors.json", "r") as f:
        investors = json.load(f)

    return investors


def update_company_info_column(sh, address, companies, i):
    if companies == "":
        companies = "No companies reported"

    sh.sheet1.update(f"{address[:-1]}{i}", companies)


def update_verification_column(sh, techstars_investors):
    sh.sheet1.add_cols(2)
    last_head_col = len(sh.sheet1.row_values(1))
    last_cell = sh.sheet1.find('**END_OF_RECORDS**', in_column=0)
    address1 = gspread.utils.rowcol_to_a1(1, last_head_col + 1)
    address2 = gspread.utils.rowcol_to_a1(1, last_head_col + 2)
    sh.sheet1.update(address1, "Invested in Techstars company")
    sh.sheet1.update(address2, "Techstars companies invested")

    for i in range(358, last_cell.row + 1):
        investor_name = sh.sheet1.cell(i, 2).value
        companies_invested = techstars_investors.get(investor_name)

        if companies_invested:
            sh.sheet1.update(f"{address1[:-1]}{i}", "Yes")
            update_company_info_column(sh, address2, companies_invested, i)
        else:
            sh.sheet1.update(f"{address1[:-1]}{i}", "No")

        if i % 10 == 0:
            sleep(60)


if __name__ == '__main__':
    investors = techstars_investors()
    sh = connect()
    update_verification_column(sh, investors)
