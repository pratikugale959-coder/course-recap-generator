# Key Concepts — AI Unit 2 (Problem Solving)

Source: `work/course-content.json` (extracted from input/course.pdf,
"AI – Unit 2 (Problem Solving) - Notes", SPPU AI, 19 pages)

| Concept | Definition | Source page(s) | Why it matters |
| --- | --- | --- | --- |
| search | A step-by-step procedure to solve a search problem in a given search space | 3 | Core abstraction of the unit |
| search-problem-factors | Search space, start state, goal test, search tree, actions, transition model, path cost, solution, optimal solution | 3 | Defines what the agent must formulate before searching |
| completeness | A search algorithm is complete if it guarantees to return a solution if at least any solution exists | 4 | Property used to evaluate search algorithms |
| optimality | A solution is optimal if it is guaranteed to be the best (lowest path cost) among all other solutions | 4 | Property used to evaluate search algorithms |
| time-space-complexity | Time complexity: measure of time for an algorithm to complete its task; space complexity: maximum storage space required at any point during the search | 4 | Properties used to compare search algorithms |
| uninformed-search | Search with no domain knowledge (e.g., closeness or location of the goal); brute-force traversal that examines each node until the goal node is achieved; also called blind search | 6 | One of the two search-strategy families |
| informed-search | Search that uses domain knowledge to guide the search and find solutions more efficiently than uninformed search; also called heuristic search | 7 | The second strategy family; solves more complex problems |
| breadth-first-search | Breadthwise traversal from the root node, expanding all successors at the current level before the next level; FIFO queue; time O(b^d), space O(bd); complete; optimal if path cost is non-decreasing in depth | 8–11 | Detailed uninformed algorithm; guarantees the minimal-step solution |
| depth-first-search | Recursive traversal that follows each path to its greatest depth node before moving to the next path; stack; low memory; time O(n^m); complete in finite state space; non-optimal | 12–16 | Detailed uninformed algorithm; memory-efficient but may loop |
| uniform-cost-search | Search on weighted trees/graphs that expands nodes by path cost from the root using a priority queue; finds the lowest cumulative cost path; worst-case time O(b^(1+[C*/ε])); complete; always optimal | 17–19 | Detailed uninformed algorithm for weighted graphs; equivalent to BFS when all edge costs are equal |
