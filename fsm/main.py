import fsm_A
import fsm_B
import events

NO_OF_DELIMITERS = 65

def main():
    event = events.Events()

    one = fsm_A.StateMachine_A()
    two = fsm_B.StateMachine_B()

    print NO_OF_DELIMITERS*'-'

    for i in range(0, 17):
        event = one.go(event)
        event = two.go(event)

    print NO_OF_DELIMITERS*'-'


if __name__ == "__main__":
    main()

