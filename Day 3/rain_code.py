from rain import Sky
import random

def build_schedule_1(): #[[0],[1],...]
        schedule=[]
        for i in range(1000):
                schedule.append([i])
        return schedule

def combine_schedules(schedule_1,schedule_2):
        combined_schedule=[]
        for i in range(max(len(schedule_1),len(schedule_2))):
                new_round=[]
                if i<len(schedule_1):
                        new_round+=schedule_1[i]
                if i<len(schedule_2):
                        new_round+=schedule_2[i]
                combined_schedule.append(new_round)
        return combined_schedule

def time_delay_schedule(schedule,delay):
        return delay*[[]]+schedule

def random_schedule(schedule_length,drops_per_time_step):
        schedule=[]
        for i in range(schedule_length):
                new_round=[]
                for j in range(drops_per_time_step):
                        new_round.append(random.randint(0,999))
                schedule.append(new_round)
        return schedule                         

sky=Sky()
schedule=random_schedule(100,15)
sky.set_raindrop_schedule(schedule)
sky.start_rain()
