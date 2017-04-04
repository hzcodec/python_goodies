import fsm_A
import fsm_B
import events

def main():
    ev = events.Events()

    one = fsm_A.StateMachine_A()
    two = fsm_B.StateMachine_B()

    for i in range(0, 12):
        ev = one.go(ev)
	print '----> SKIP:%d, RUN:%d, STOP:%d' % (ev.SKIP, ev.RUN, ev.STOP)
        ev = two.go(ev)
	print '----> SKIP:%d, RUN:%d, STOP:%d' % (ev.SKIP, ev.RUN, ev.STOP)

    print 40*'-'


if __name__ == "__main__":
    main()

