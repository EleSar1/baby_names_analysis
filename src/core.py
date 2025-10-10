from .file_manager import read_file
from .analysis import popular_names, name_diversity, name_length, name_endings_analysis, name_popularity_over_decades
from .visualization import visualize_popular_names, visualize_name_diversity, visualize_name_length, visualize_top_5_base_form_names, visualize_top_names_per_decade

def main():

    data = read_file("file/data.csv")

    print("\nTop 10 names for a specified year:\n")
    top_10_names = popular_names(data, year="2000")
    visualize_popular_names(top_10_names)

    print("\nTop 5 unique male and female names for year:\n")
    unique_names = name_diversity(data)
    visualize_name_diversity(unique_names)

    print("\nAverage male and female name length for each year:\n")
    avg_name_length = name_length(data)
    visualize_name_length(avg_name_length)

    print("\nTop 5 base form names (without the last letter):\n")
    name_endings = name_endings_analysis(data)
    visualize_top_5_base_form_names(name_endings)

    print("\nTop 5 male and female names over decades:\n")
    name_decades = name_popularity_over_decades(data)
    visualize_top_names_per_decade(name_decades)