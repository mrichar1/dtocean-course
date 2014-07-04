"""Return the cost and profit from the house-building database."""

import fakedb


def profit(size, region):
    """ Return the profit for building houses of a certain size in a region."""

    db = fakedb.DB()
    nums = {}
    for table in ("build_cost", "value", "density"):
        nums[table] = db.query(table)[size][region]

    # nums = {'build_cost': x, 'value': y, 'density': z}

    return (nums['value'] * nums['density']) - (nums['build_cost'] * nums['density'])
