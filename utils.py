import csv
import json


CSV_PATH_FOR_ADS = "datasets/ads.csv"
JSON_PATH_FOR_ADS = "ads.json"
MODEL_FOR_ADS = "ads.ad"

CSV_PATH_FOR_CAT = "datasets/categories.csv"
JSON_PATH_FOR_CAT = "categories.json"
MODEL_FOR_CAT = "ads.category"


def csv_to_json_for_ads() -> None:

    """Open csv"""
    with open(CSV_PATH_FOR_ADS, encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        result = []

        """Change csv file"""
        for row in csv_reader:

            to_add = {"model": MODEL_FOR_ADS, "pk": int(row['Id'])}
            del row['Id']
            if row['is_published'] == "TRUE":
                row['is_published'] = True
            else:
                row['is_published'] = False
            row['price'] = int(row['price'])
            to_add['fields'] = row

            result.append(to_add)

    """Write in json"""
    with open(JSON_PATH_FOR_ADS, 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(result, indent=4, ensure_ascii=False))


def csv_to_json_for_categories() -> None:

    """Open csv"""
    with open(CSV_PATH_FOR_CAT, encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        result = []

        """Change csv file"""
        for row in csv_reader:

            to_add = {"model": JSON_PATH_FOR_CAT, "pk": int(row['id'])}
            del row['id']
            to_add['fields'] = row

            result.append(to_add)

    """Write in json"""
    with open(MODEL_FOR_CAT, 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(result, indent=4, ensure_ascii=False))


# csv_to_json_for_ads()
# csv_to_json_for_categories()
