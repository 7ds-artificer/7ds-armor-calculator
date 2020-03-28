from constants import ITEM_HEADER, VALUE_HEADER, STAT_HEADER
from collections import OrderedDict

def subtract_lists(A, B):
    C = A
    for b in B:
        if b in C:
            C.remove(b)
    return C

def get_rows_by_armor(armor, rows):
    filtered_rows = []
    for row in rows:
        if row[ITEM_HEADER] == armor:
            filtered_rows.append(row)
    return filtered_rows

def csv_sort(rows):
    return sorted(rows, key=lambda item: item['value'], reverse=True)

def calculate_best_armor_sets(atk_csv, def_csv, hp_csv, prio_csv, items_csv):
    atk_def = []
    hp_def = []
    used = []

    for each_armor_piece in items_csv:
        for each_unit in prio_csv:
            dummy_val = OrderedDict()

            try:
                stat_label = each_unit[STAT_HEADER]
            except KeyError as e:
                print(f'Failed to find key: {STAT_HEADER}. Available: {each_unit.keys()}')
                raise e

            try:
                armor_label = each_armor_piece[ITEM_HEADER]
            except KeyError as e:
                print(f'Failed to find key: {ITEM_HEADER}. Available: {each_armor_piece.keys()}')
                raise e

            if stat_label == 'atk':
                A = get_rows_by_armor(armor_label, atk_csv)
                D = get_rows_by_armor(armor_label, def_csv)
                AD = csv_sort(A + D)
                diff = subtract_lists(AD, used)
                if not diff:
                    dummy_val[ITEM_HEADER] = armor_label
                    dummy_val[VALUE_HEADER] = 0
                armor_value = diff[0] if diff else dummy_val
                atk_def.append(armor_value)
                used.append(armor_value)
            elif stat_label == 'hp':
                H = get_rows_by_armor(armor_label, hp_csv)
                D = get_rows_by_armor(armor_label, def_csv)
                HD = csv_sort(H + D)
                diff = subtract_lists(HD, used)
                if not diff:
                    dummy_val[ITEM_HEADER] = armor_label
                    dummy_val[VALUE_HEADER] = 0
                armor_value = diff[0] if diff else dummy_val
                hp_def.append(armor_value)
                if armor_value:
                    used.append(armor_value)
            else:
                raise ValueError(f'Invalid value for column {STAT_HEADER} in the priority file. Valid values: atk, hp')

    return atk_def, hp_def
