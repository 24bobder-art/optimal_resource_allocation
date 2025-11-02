
import time
from job_scheduling import Job, greedy_job_sequencing
from compare_bruteforce import brute_force_job_sequencing
from resource_selection import fractional_knapsack

def demo_job_comparison(jobs):
    print('\n=== JOB SCHEDULING: Greedy vs Brute-Force ===')
    t0 = time.time()
    sched, profit_greedy = greedy_job_sequencing(jobs)
    t1 = time.time()
    seq_bf, profit_bf = brute_force_job_sequencing(jobs)
    t2 = time.time()
    print('Jobs:', jobs)
    print('Greedy scheduled (slot order):', sched)
    print('Greedy profit:', profit_greedy, 'time:', round(t1-t0,4), 's')
    print('Brute-force best perm:', seq_bf)
    print('Brute-force profit:', profit_bf, 'time:', round(t2-t1,4), 's')
    if profit_greedy == profit_bf:
        print('Greedy achieved optimal profit for this instance.')
    else:
        print('Greedy did NOT achieve optimal profit for this instance.')

def demo_resource_selection():
    print('\n=== RESOURCE SELECTION: Fractional Knapsack (Greedy) ===')
    costs = [10,20,30,40]
    benefits = [60,100,120,200]
    cap = 60
    sel, tc, tb = fractional_knapsack(costs, benefits, cap)
    print('Costs:', costs)
    print('Benefits:', benefits)
    print('Capacity:', cap)
    print('Selected (idx, cost_used, benefit_received, fraction):', sel)
    print('Total cost:', tc, 'Total benefit:', tb)

if __name__ == '__main__':
    jobs = [Job('J1', 100, 2), Job('J2', 19, 1), Job('J3', 27, 2),
            Job('J4', 25, 1), Job('J5', 15, 3)]
    demo_job_comparison(jobs)
    demo_resource_selection()
