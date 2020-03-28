from file_utils import load_csv, write_csv
from armor_calculator import calculate_best_armor_sets

def main():
    #load user data
    atk_csv = load_csv('user_data/atk.csv')
    for row in atk_csv:
        print(row)
    def_csv = load_csv('user_data/def.csv')
    for row in def_csv:
        print(row)
    hp_csv = load_csv('user_data/hp.csv')
    for row in hp_csv:
        print(row)
    prio_csv = load_csv('user_data/priority.csv')
    for row in prio_csv:
        print(row)

    # load reference data
    items_csv = load_csv('reference_data/items.csv')

    # calculate best armor sets
    atk_def_sets, hp_def_sets = calculate_best_armor_sets(atk_csv, def_csv, hp_csv, prio_csv, items_csv)

    # write output to files
    write_csv(atk_csv[0].keys(), atk_def_sets, 'output/atk_def_sets.csv')
    write_csv(hp_csv[0].keys(), hp_def_sets, 'output/hp_def_sets.csv')

main()
