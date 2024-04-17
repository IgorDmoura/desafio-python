from typing import List


class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)

    def to_dict(self):
        return {
            'id': self.id,
            'debt': self.debt
        }


open_contracts = [Contract(1, 50000),
                  Contract(2, 7000),
                  Contract(3, 9000),
                  Contract(4, 3500),
                  Contract(5, 12500),
                  Contract(6, 800)]


renegotiated_contracts = [2, 3]
top_n = 3


class Contracts:
    def get_top_n_open_contracts(self, open_contracts,
                                 renegotiated_contracts, top_n) -> List[int]:
        """
        Retrieve the top N open contracts with the highest debt,
        excluding renegotiated contracts.

        This method filters out the renegotiated contracts
        from the list of open contracts, sorts the
        remaining contracts by their debt in descending order,
        and returns the IDs of the top N contracts.

        Args:
            open_contracts (List[Contract]): A list of
            open contracts.
            renegotiated_contracts (List[int]): A list of IDs
            of renegotiated contracts.
            top_n (int): The number of top contracts to retrieve.

        Returns:
            List[int]: A list containing the IDs of the top N open
            contracts with the highest debt.

        Example:
            >>> contracts = Contracts()
            >>> contracts.get_top_n_open_contracts([Contract(1, 100),
            Contract(2, 200)], [2], 1)
            [1]
        """

        unpaid_contracts = [contract.to_dict() for contract in open_contracts
                            if contract.id not in renegotiated_contracts]
        unpaid_contracts = sorted(unpaid_contracts, key=lambda x: x['debt'],
                                  reverse=True)
        return [contract['id'] for contract in unpaid_contracts[:top_n]]


contracts = Contracts()
result = contracts.get_top_n_open_contracts(open_contracts,
                                            renegotiated_contracts, top_n)
print(result)
