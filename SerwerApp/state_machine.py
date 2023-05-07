# Enum kierunków ruchu:
class WhereDrive():

    ERROR = 0
    GO_LEFT = 1
    GO_RIGHT = 2
    GO_STRAIGHT = 3
    DESTINATION = 4

class StateMachine:

    class State:

        INITIAL_STRAIGHT = 1
        TURN_LEFT = 2
        AFTER_TURN = 3
        TURN_RIGHT = 4
        PARKED = 5

    current_state = 1
    distance_thresholds = [10, 30, 10, 5]

    def stateAction(self, distance_cm: int) -> WhereDrive:

        if self.current_state < 5 and self.ifNextState(distance_cm):
            self.current_state += 1

        if self.current_state == 1:
            return WhereDrive.GO_STRAIGHT

        elif self.current_state == 2:
            return WhereDrive.GO_LEFT

        elif self.current_state == 3:
            return WhereDrive.GO_STRAIGHT

        elif self.current_state == 4:
            return WhereDrive.GO_RIGHT

        elif self.current_state == 5:
            return WhereDrive.DESTINATION

    def ifNextState(self, distance_cm: int) -> bool:

        if self.current_state == 1:
            if distance_cm < self.distance_thresholds[0]:
                return True

        elif self.current_state == 2:
            if distance_cm > self.distance_thresholds[1]:
                return True

        elif self.current_state == 3:
            if distance_cm < self.distance_thresholds[2]:
                return True

        elif self.current_state == 4:
            if distance_cm < self.distance_thresholds[3]:
                return True

        return False
