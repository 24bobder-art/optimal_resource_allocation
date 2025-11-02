# job_scheduling.py
from typing import List, Tuple, Dict
import math

class Job:
    def __init__(self, job_id: str, profit: int, deadline: int):
        self.job_id = job_id
        self.profit = profit
        self.deadline = deadline

    def __repr__(self):
        return f"Job({self.job_id}, profit={self.profit}, deadline={self.deadline})"

def greedy_job_sequencing(jobs: List[Job]) -> Tuple[List[str], int]:
    """Greedy job sequencing to maximize profit with deadlines.
    Returns (scheduled_job_ids_in_slot_order, total_profit)
    """
    # sort by descending profit
    jobs_sorted = sorted(jobs, key=lambda j: j.profit, reverse=True)
    max_deadline = max((j.deadline for j in jobs_sorted), default=0)
    slots = [None] * max_deadline  # slots[i] is job id at time i (0-indexed)
    total_profit = 0
    for job in jobs_sorted:
        # try to place job in the latest free slot before deadline
        for t in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slots[t] is None:
                slots[t] = job.job_id
                total_profit += job.profit
                break
    scheduled = [s for s in slots if s is not None]
    return scheduled, total_profit

def reconstruct_schedule_from_assignment(assignment):
    return assignment

if __name__ == '__main__':
    demo_jobs = [Job('J1', 100, 2), Job('J2', 19, 1), Job('J3', 27, 2),
                 Job('J4', 25, 1), Job('J5', 15, 3)]
    sched, profit = greedy_job_sequencing(demo_jobs)
    print('Greedy schedule slots:', sched)
    print('Total profit:', profit)
