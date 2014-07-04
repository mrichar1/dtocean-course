"""A simple script to calculate the best options for property development."""

from housecost import calculate


def get_profits(sizes, regions):
    """Build a dictionary of profit for sizes and regions using calculate."""

    profits = {}

    for size in sizes:
        profits[size] = {}
        for region in regions:
            profits[size][region] = calculate.profit(size, region)

    return profits


def print_profits(profits):
    """Print out a profit dictionary as a table using string formatting."""

    title = "|{:^7}| {:^9}|{:^10}|".format("Size", "Region", "Profit")
    print title
    # Print a row of dashes the same length as the title field
    print "-" * len(title)
    for size, regions in profits.items():
        for region, profit in regions.items():
            print "|{:<7}| {:<9}|{:>10,}|".format(size,
                                                  region.capitalize(),
                                                  profit)

if __name__ == "__main__":

    regions = ("england", "scotland", "ireland")
    sizes = ("small", "medium", "large")

    profit_dict = get_profits(sizes, regions)
    print_profits(profit_dict)
