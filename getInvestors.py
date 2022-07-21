import json


def get_investors():
    f = open("/airtableResult.json")
    result = json.load(f)

    investors_dict = {}
    try:
        table = result.get("data").get("tableDatas")[0].get("rows")

        for record in table:
            companies = ""
            investor_name = record.get('cellValuesByColumnId').get('fldp5n7uGNyg5ItNP')
            companies_list = record.get('cellValuesByColumnId').get('fld1c3RtJaHjFRuLs')
            if companies_list:
                for company in companies_list:
                    companies += f"{company.get('foreignRowDisplayName')}, "
            investors_dict[investor_name] = companies

    except Exception as e:
        print(e.__str__())

    f.close()

    return investors_dict


def save_investors(investors_dict):

    out_file = open("investors.json", "w")

    json.dump(investors_dict, out_file, indent=6)

    out_file.close()


if __name__ == '__main__':
    dict = get_investors()
    save_investors(dict)
