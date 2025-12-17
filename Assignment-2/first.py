from enum import Enum


class DoorState(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


class Elevator:
    def __init__(self, e_id: int, current_floor: int = 0, min_floor: int = 0, max_floor: int = 10):
        self.e_id = e_id
        self.current_floor = current_floor
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.door = DoorState.CLOSED
        self.emergency_mode = False

    def open_door(self):
        if self.emergency_mode:
            print("Emergency: doors already managed")
            return
        if self.door == DoorState.OPEN:
            print("Door already open")
        else:
            self.door = DoorState.OPEN
            print("Door opened")

    def close_door(self):
        if self.door == DoorState.CLOSED:
            print("Door already closed")
        else:
            self.door = DoorState.CLOSED
            print("Door closed")

    def go_up(self):
        if self.door == DoorState.OPEN:
            print("Close doors before moving")
            return
        if self.current_floor >= self.max_floor:
            print("Already at top floor")
            return
        self.current_floor += 1
        print(f"Moved up -> floor {self.current_floor}")

    def go_down(self):
        if self.door == DoorState.OPEN:
            print("Close doors before moving")
            return
        if self.current_floor <= self.min_floor:
            print("Already at bottom floor")
            return
        self.current_floor -= 1
        print(f"Moved down -> floor {self.current_floor}")

    def go_to_floor(self, floor: int):
        if not (self.min_floor <= floor <= self.max_floor):
            print("Requested floor out of range")
            return
        if self.emergency_mode:
            print("Cannot move: emergency mode")
            return
        while self.current_floor < floor:
            self.go_up()
        while self.current_floor > floor:
            self.go_down()
        print(f"Arrived at floor {self.current_floor}")

    def emergency(self, reason: str = ""):
        self.emergency_mode = True
        self.door = DoorState.OPEN
        print(f"EMERGENCY triggered{': ' + reason if reason else ''} — doors opened")

    def reset_emergency(self):
        self.emergency_mode = False
        self.door = DoorState.CLOSED
        print("Emergency cleared")

    def status(self):
        return {
            "id": self.e_id,
            "floor": self.current_floor,
            "door": self.door.value,
            "emergency": self.emergency_mode,
        }


# --- Example ---
if __name__ == "__main__":
    e = Elevator(e_id=1, current_floor=0, max_floor=5)
    print(e.status())
    e.open_door()
    e.close_door()
    e.go_to_floor(3)
    e.emergency("fire alarm")
    e.go_to_floor(1)   # blocked by emergency
    e.reset_emergency()
    e.go_to_floor(1)
    print(e.status())
