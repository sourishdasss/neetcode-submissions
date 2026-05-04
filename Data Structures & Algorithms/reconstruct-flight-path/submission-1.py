class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = defaultdict(list)
        
        for t in tickets:
            start = t[0]
            end = t[1]
            flights[start].append(end)

        # account for lexicographically smaller flights
        for k in flights.keys():
            flights[k].sort(reverse=True)

        stack = ["JFK"]
        route = []
        while stack:
            if flights[stack[-1]]:
                destination = flights[stack[-1]].pop()
                stack.append(destination)
            else:
                start = stack.pop()
                route.append(start)

        print(route)
        return route[::-1]
