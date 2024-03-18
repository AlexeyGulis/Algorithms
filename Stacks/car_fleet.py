from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 1
        time = []
        my_dict = {position[i]: speed[i] for i in range(len(position))}
        my_dict = dict(sorted(my_dict.items(), reverse=True))
        new_position = list(my_dict.keys())
        new_speed = list(my_dict.values())
        for i in range(len(new_position)):
            time.append((target - new_position[i]) / new_speed[i])

        if len(position) > 0:
            ans = 1
        for i in range(len(new_position) - 1):
            if time[i + 1] <= time[i]:
                time[i + 1] = time[i]
            else:
                ans += 1

        # while car_finished < len(position):
        #     car_fleet = []
        #     for i in range(len(new_position)):
        #         if position_list_queue[i] >= target:
        #             continue
        #         if position_list_queue[i] < target:
        #             position_list_queue[i] += new_speed[i]
        #         if i != 0:
        #             if position_list_queue[i - 1] < target:
        #                 if position_list_queue[i - 1] <= position_list_queue[i]:
        #                     position_list_queue[i] = position_list_queue[i - 1]
        #                     new_speed[i] = new_speed[i - 1]
        #         if position_list_queue[i] >= target:
        #             car_finished += 1
        #             if len(car_fleet) == 0:
        #                 car_fleet.append(i)
        #             else:
        #                 t1 = (target - (position_list_queue[i - 1] - new_speed[i - 1])) / new_speed[i - 1]
        #                 t2 = (target - (position_list_queue[i] - new_speed[i])) / new_speed[i]
        #                 if t2 > t1:
        #                     car_fleet.append(i)
        #     ans += len(car_fleet)
        return ans


s = Solution()
print(s.carFleet(target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]))
