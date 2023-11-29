class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        position = sorted(
            list(zip(position, speed)),
            key= lambda car: car[0],
            reverse = True
        )

        fleet_number = 0
        next_fleet_time = float('-inf')
        for car in position:
            car_position = car[0]
            car_speed = car[1]

            car_time = (target - car_position) / car_speed

            if car_time > next_fleet_time:
                fleet_number += 1
                next_fleet_time = car_time

        return fleet_number
