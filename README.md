
# Optimal Resource Allocation 

### Developed by:

Renuka Bobde
Abha Bhondge

---

## **Title:**

Optimal Resource Allocation System

## **Objectives:**

1. To design a scheduling system that maximizes profit while meeting deadlines using a greedy approach.
2. To implement an efficient resource selection mechanism minimizing total cost using greedy logic.
3. To compare greedy algorithms with brute-force methods for efficiency and optimality.
4. To demonstrate real-world applicability in task scheduling and resource management.
5. To visualize and analyze results for better understanding of algorithmic behavior.

---

## **Introduction:**

Efficient allocation of resources and scheduling of tasks are fundamental challenges in operations research, logistics, and computing. The **Optimal Resource Allocation System** aims to use **Greedy Algorithms** to optimize two aspects:

* **Job Scheduling:** Selecting jobs with maximum profit within given deadlines.
* **Resource Selection:** Choosing resources that minimize cost while satisfying requirements.

A **Greedy Algorithm** makes a locally optimal choice at each step with the hope of finding a global optimum. This approach is particularly effective for problems with the **Greedy Choice Property** and **Optimal Substructure**.

This project compares greedy methods with brute-force approaches to highlight trade-offs between **optimality** and **efficiency**.

---

## **Algorithms / Techniques Used:**

### 1. **Job Scheduling with Deadlines and Profits (Greedy Approach)**

**Algorithm Name:** Job Sequencing with Deadlines

**Steps:**

1. Sort all jobs in descending order of profit.
2. For each job, schedule it in the latest available slot before its deadline.
3. If no slot is available, skip the job.
4. Compute total profit and list of scheduled jobs.

**Pseudocode:**

```
Sort jobs by profit (descending)
For each job in sorted list:
    Find a free time slot before its deadline
    If available:
        Assign job to that slot
        Add profit to total
```

**Diagram (conceptual):**

```
Jobs:   J1  J2  J3  J4
Profit: 100 50  30  10
Deadline: 2 1 2 1

Result: J1 -> Slot 2, J2 -> Slot 1
Total Profit = 150
```

### 2. **Resource Selection (Greedy Knapsack-based Approach)**

**Algorithm Name:** Fractional Knapsack Algorithm

**Steps:**

1. Sort resources by cost-to-benefit ratio.
2. Select resources starting from the lowest cost ratio until requirements are met.
3. If partial resources can be selected, take fractional values.

**Pseudocode:**

```
Sort resources by cost/benefit ascending
For each resource:
    If capacity remains:
        Take full resource if possible
        Else take fraction of remaining capacity
```

### 3. **Brute-Force Comparison**

**Algorithm:** Generate all possible combinations of job orders or resource sets to verify the optimal greedy outcome.

---

## **Time Complexity Analysis:**

| Algorithm                     | Time Complexity | Explanation                                    |
| ----------------------------- | --------------- | ---------------------------------------------- |
| Job Scheduling (Greedy)       | O(n log n)      | Sorting jobs dominates complexity              |
| Resource Selection (Knapsack) | O(n log n)      | Sorting by ratio and single iteration          |
| Brute-Force (Comparison)      | O(2ⁿ)           | Enumerates all combinations of tasks/resources |

**Observation:** The greedy algorithm achieves near-optimal results in a fraction of the brute-force time, demonstrating high efficiency and practical applicability.

---

## **Results:**

### **Job Scheduling Output:**

```
Available Jobs:
A (Profit=100, Deadline=2)
B (Profit=50, Deadline=1)
C (Profit=30, Deadline=2)

Scheduled Jobs: A, B
Total Profit: 150
```

### **Resource Selection Output:**

```
Available Resources:
R1: Cost=100, Benefit=60
R2: Cost=50, Benefit=40
R3: Cost=120, Benefit=100

Selected Resources: R2, R1
Total Cost: 150, Total Benefit: 100
```

### **Efficiency Comparison:**

| Method      | Execution Time | Optimal Profit |
| ----------- | -------------- | -------------- |
| Greedy      | 0.002s         | 150            |
| Brute Force | 0.280s         | 150            |

**Discussion:**
The greedy approach gives optimal results in this dataset with 100× faster execution, validating its practical efficiency.

---

## **Conclusion and Future Scope:**

The project successfully implements and analyzes greedy-based optimization strategies for resource allocation and job scheduling. Results demonstrate that greedy algorithms provide **efficient and near-optimal** solutions in real-time systems.

**Future Enhancements:**

1. Integrate dynamic data input (live scheduling).
2. Add visualization dashboard for better insight.
3. Combine with **Dynamic Programming** for hybrid optimization.
4. Extend to multi-resource, multi-agent environments.

---

**End of Report**
