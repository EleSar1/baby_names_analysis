from tabulate import tabulate                                                   


def visualize_top_names_per_decade(top_names):

    for decade, genders in top_names.items():
        print(f"\nDecade: {decade}")
        for gender, names in genders.items():
            print(f"\n{'Male' if gender=='m' else 'Female'}:")
            print(tabulate(names, headers=["Name", "Count"]))


def visualize_popular_names(popular_names):

    print(tabulate(popular_names, headers="keys"))


def visualize_name_diversity(unique_names):

    for year, gender in unique_names.items():
        print(f"\nYear {year}:")
        print(tabulate(gender.items(), headers=["Gender", "Count"]))


def visualize_name_length(avg_names):

    for year, gender in avg_names.items():
        print(f"\nYear {year}:")
        print(tabulate(gender.items(), headers=["Gender", "Average length"]))


def visualize_top_5_base_form_names(base_form_names):

    print(tabulate(base_form_names, headers=["Name", "Count"]))

