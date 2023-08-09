import time
from typing import List, Optional
from threading import Thread, Lock


class Dungeon:
    def __init__(self, reward: int, *args, **kwargs):
        self._reward: int = reward
        self._field_lock: Lock = Lock()
        self.is_character_banned: bool = False
        self.entered_character: Optional['Character'] = None

    def get_reward(self) -> int:
        return self._reward

    def get_lock(self) -> Lock:
        return self._field_lock


class Character:
    def __init__(self, power: int, *args, **kwargs):
        self._gold: int = 0
        self._work_count: int = 0
        self._work_lock: Lock = Lock()
        self._power: int = power

    def work(self, gold: int) -> None:
        self._work_lock.acquire()
        self._gold += gold
        self._work_count += 1
        self._work_lock.release()
        if self._work_count % 1000000 == 0:
            time.sleep(0.3)

    def show_power(self) -> int:
        return self._power

    def show_gold(self) -> int:
        return self._gold

    def work_multiple_times(self, times: int, gold: int) -> None:
        for _ in range(times):
            self.work(gold)

    def hunt_multiple_times_in_dungeons(self, dungeons: List[Dungeon], times: int):
        for i in range(len(dungeons)):
            other_charater = dungeons[i].entered_character
            if other_charater is not None:
                if self.show_power() > other_charater.show_power():
                    dungeons[i].is_character_banned = True

            dungeons[i].get_lock().acquire()
            dungeons[i].entered_character = self
            for _ in range(times):
                if dungeons[i].is_character_banned == True:
                    dungeons[i].is_character_banned = False
                    dungeons[i].entered_character = None
                    dungeons[i].get_lock().release()
                    time.sleep(0.1)
                    dungeons[i].get_lock().acquire()
                    dungeons[i].entered_character = self
                self.work(dungeons[i].get_reward())
            dungeons[i].entered_character = None
            dungeons[i].get_lock().release()


my_charater = Character(10)
other_charater = Character(5)
dungeons = [Dungeon(10), Dungeon(15)]

hunting_my_charater = Thread(target=my_charater.hunt_multiple_times_in_dungeons,
                             kwargs={"dungeons": [dungeons[0], dungeons[1]], "times": 5000000})

hunting_other_charater = Thread(target=other_charater.hunt_multiple_times_in_dungeons,
                                kwargs={"dungeons": [dungeons[1], dungeons[0]], "times": 5000000})
start_time = time.time()
hunting_my_charater.start()
time.sleep(1)
hunting_other_charater.start()

hunting_my_charater.join()
print("my_charater", time.time()-start_time)
hunting_other_charater.join()
print("other_charater", time.time()-start_time)
print("my_charater", my_charater.show_gold())
print("other_charater", other_charater.show_gold())
