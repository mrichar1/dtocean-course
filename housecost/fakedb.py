class DB(object):

    """A class to provide a fake database, with helper method to return them."""


    def __init__(self):
        """Initialise dictionary attributes."""

        self.value = {"small": {"scotland": 100000,
                                "england": 250000,
                                "ireland": 200000},
                      "medium": {"scotland": 250000,
                                 "england": 500000,
                                 "ireland": 500000},
                      "large": {"scotland": 1000000,
                                "england": 5000000,
                                "ireland": 3000000}
                      }

        self.density = {"small": {"scotland": 20,
                                  "england": 10,
                                  "ireland": 9},
                        "medium": {"scotland": 5,
                                   "england": 6,
                                   "ireland": 6},
                        "large": {"scotland": 3,
                                  "england": 1,
                                  "ireland": 2}
                      }

        self.build_cost = {"small": {"scotland": 1000 * 20,
                                     "england": 1000 * 5,
                                     "ireland": 1000 * 8},
                           "medium": {"scotland": 5500 * 20,
                                      "england": 5500 * 5,
                                      "ireland": 5500 * 8},
                           "large": {"scotland": 12000 * 20,
                                     "england": 12000 * 5,
                                     "ireland": 12000 * 8}
                      }

    def query(self, table):
        """A helper method which returns dictionary attributes, or None."""

	return getattr(self, table, None)

