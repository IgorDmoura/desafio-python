requests = [70, 30, 25, 1, 15, 1, 18]
n_max = 100
limit_per_trip = 2


class Orders:
    def combine_orders(self, requests, n_max, limit_per_trip) -> int:
        """
        Combine orders in the list 'requests' as much as possible,
        given the maximum order size 'n_max'.

        This method iterates through the list of orders 'requests'
        and combines adjacent orders if their sum
        does not exceed the maximum order size 'n_max'. It returns
        the total number of combined orders.

        Args:
            requests (List[int]): A list of integers
            representing individual orders.
            n_max (int): The maximum size allowed
            for each combined order.

        Returns:
            int: The total number of combined orders.

        Example:
            >>> orders = Orders()
            >>> orders.combine_orders([1, 2, 3, 4], 100, 2)
            2
        """

        requests.sort(reverse=True)
        trips = []

        while requests:
            current_trip = []
            current_sum = 0
            temp_requests = requests.copy()

            for request in temp_requests:
                if current_sum + request <= n_max and \
                   len(current_trip) < limit_per_trip:
                    current_trip.append(request)
                    current_sum += request
                    requests.remove(request)

            if current_trip:
                trips.append(current_trip)

        return len(trips)


order = Orders()
result = order.combine_orders(requests, n_max, limit_per_trip)
print(result)
