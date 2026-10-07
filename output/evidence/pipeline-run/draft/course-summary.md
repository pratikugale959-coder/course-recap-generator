# AI – Unit 2 (Problem Solving) — Course Recap

- **Source:** course.pdf — "AI – Unit 2 (Problem Solving) - Notes"
- **Course:** SPPU Computer Engineering, 3rd year TE, Semester 6 (2019 pattern)
- **Pages:** 19
- **Generated:** 2026-10-07

## 1. Course overview

This unit of the SPPU Artificial Intelligence course covers problem
solving through search. It defines search and the factors of a search
problem (search space, start state, goal test, search tree, actions,
transition model, path cost, solution, optimal solution), then
introduces the properties used to evaluate search algorithms
(completeness, optimality, time and space complexity). The unit then
divides search algorithms into uninformed (blind) and informed
(heuristic) strategies. Finally it examines three algorithms in
detail — breadth-first search, depth-first search, and uniform-cost
search — including their implementations, worked examples,
complexities, completeness, and optimality.

## 2. Learning objectives

The source does not state learning objectives verbatim. Objectives
implied by the unit's section structure:

- Formulate a problem as a search problem with its defining factors
  (p. 3)
- Explain the properties used to evaluate search algorithms:
  completeness, optimality, time complexity, space complexity (p. 4)
- Distinguish uninformed (blind) search from informed (heuristic)
  search (pp. 6–7)
- Describe breadth-first, depth-first, and uniform-cost search,
  including data structures, advantages, disadvantages, and
  complexities (pp. 8–19)
- Judge the completeness and optimality of each algorithm
  (pp. 11, 15–16, 19)

## 3. Module-by-module recap

### Module 1: Introduction and Problem Solving (slides 1–3, pages 1–3)

**Topics:** unit introduction; search definition; search problem factors

**Key takeaways:**

- Search is a step-by-step procedure to solve a search problem in a
  given search space (p. 3)
- A search problem's factors: search space (a set of possible
  solutions), start state (where the agent begins the search), goal
  test (function that observes the current state and returns whether
  the goal state is achieved), search tree (tree representation of the
  problem, rooted at the initial state), actions, transition model,
  path cost (numeric cost assigned to each path), solution (action
  sequence from start node to goal node), and optimal solution (lowest
  cost among all solutions) (p. 3)

### Module 2: Properties of Search Algorithms (slide 4, page 4)

**Topics:** completeness; optimality; time complexity; space complexity

**Key takeaways:**

- Completeness: a search algorithm is complete if it guarantees to
  return a solution if at least any solution exists for any random
  input (p. 4)
- Optimality: a solution is optimal if it is guaranteed to be the
  best solution (lowest path cost) among all other solutions (p. 4)
- Time complexity is a measure of time for an algorithm to complete
  its task; space complexity is the maximum storage space required at
  any point during the search (p. 4)

### Module 3: Types of Search Algorithms (slides 5–7, pages 5–7)

**Topics:** uninformed/blind search; informed/heuristic search

**Key takeaways:**

- Uninformed (blind) search contains no domain knowledge such as
  closeness or the location of the goal; it operates in a brute-force
  way, searching the tree without information about the search space
  and examining each node until it achieves the goal node (p. 6)
- Uninformed algorithms listed: breadth-first search, uniform cost
  search, depth-first search, iterative deepening depth-first search,
  bidirectional search (p. 6)
- Informed search algorithms use domain knowledge that can guide the
  search and find a solution more efficiently than an uninformed
  strategy; informed search is also called heuristic search (p. 7)
- A heuristic is a way which might not always be guaranteed to give
  the best solutions but is guaranteed to find a good solution in
  reasonable time (p. 7)
- Informed algorithms listed: greedy search, A* search (p. 7)

### Module 4: Breadth-First Search (slides 8–11, pages 8–11)

**Topics:** definition; FIFO queue; advantages; disadvantages;
example; complexity; completeness; optimality

**Key takeaways:**

- BFS is the most common search strategy for traversing a tree or
  graph; it searches breadthwise, starting from the root node and
  expanding all successor nodes at the current level before moving to
  nodes of the next level; it is implemented using a FIFO queue
  (p. 8)
- Advantages: BFS will provide a solution if any solution exists;
  with more than one solution, it provides the minimal solution
  requiring the least number of steps (p. 9)
- Disadvantages: it requires lots of memory (each level of the tree
  must be saved to expand the next level) and needs lots of time if
  the solution is far away from the root node (p. 9)
- Worked example: traversal from root node S to goal node K follows
  S→A→B→C→D→G→H→E→F→I→K (p. 10)
- Time complexity O(b^d) and space complexity O(bd), where d is the
  depth of the shallowest solution and b is the branching factor
  (p. 11)
- BFS is complete if the shallowest goal node is at some finite
  depth; BFS is optimal if path cost is a non-decreasing function of
  the depth of the node (p. 11)

### Module 5: Depth-First Search (slides 12–16, pages 12–16)

**Topics:** definition; stack; recursion; advantages; disadvantages;
example; completeness; complexity; optimality

**Key takeaways:**

- DFS is a recursive algorithm for traversing a tree or graph; it
  starts from the root node and follows each path to its greatest
  depth node before moving to the next path; it uses a stack data
  structure (p. 12)
- Advantages: DFS requires very little memory (only the stack of
  nodes on the path from root to current node) and takes less time to
  reach the goal node than BFS if it traverses the right path (p. 13)
- Disadvantages: states may keep re-occurring with no guarantee of
  finding a solution, and deep searching may enter an infinite loop
  (p. 13)
- Worked example: from root S, traverse A, then B, then D and E;
  backtrack at E (no other successor, goal not found); then traverse
  C and then G, terminating at G with the goal found (p. 14)
- DFS is complete within finite state space, expanding every node
  within a limited search tree (p. 15)
- Time complexity O(n^m), where m is the maximum depth of any node,
  which can be much larger than d; DFS is non-optimal, as it may
  generate a large number of steps or high cost to reach the goal
  (p. 16)

### Module 6: Uniform-Cost Search (slides 17–19, pages 17–19)

**Topics:** weighted trees/graphs; priority queue; lowest cumulative
cost; advantages; disadvantages; completeness; complexity; optimality

**Key takeaways:**

- Uniform-cost search traverses a weighted tree or graph where a
  different cost is available for each edge; its primary goal is to
  find a path to the goal node with the lowest cumulative cost; it
  expands nodes according to their path cost from the root node and is
  implemented with a priority queue giving maximum priority to the
  lowest cumulative cost (p. 17)
- Uniform-cost search is equivalent to BFS if the path cost of all
  edges is the same (p. 17)
- Advantages: it is optimal because at every state the path with the
  least cost is chosen (p. 18)
- Disadvantages: it does not care about the number of steps, only path
  cost, so it may be stuck in an infinite loop (p. 18)
- UCS is complete: if there is a solution, UCS will find it (p. 19)
- Worst-case time complexity O(b^(1 + [C*/ε])), where C* is the cost
  of the optimal solution and ε is each step to get closer to the goal
  node (p. 19)
- UCS is always optimal, as it only selects a path with the lowest
  path cost (p. 19)

## 4. Glossary

| Term | Definition | Source page(s) |
| --- | --- | --- |
| Search | A step-by-step procedure to solve a search problem in a given search space | 3 |
| Search tree | A tree representation of a search problem; its root corresponds to the initial state | 3 |
| Path cost | A function that assigns a numeric cost to each path | 3 |
| Optimal solution | A solution that has the lowest cost among all solutions | 3 |
| Completeness | A search algorithm is complete if it guarantees to return a solution if at least any solution exists | 4 |
| Optimality | A solution is optimal if it is guaranteed to be the best (lowest path cost) among all other solutions | 4 |
| Uninformed (blind) search | Search without domain knowledge; brute-force traversal until the goal node is achieved | 6 |
| Heuristic | A way that might not always guarantee the best solutions but guarantees a good solution in reasonable time | 7 |
| Breadth-first search | Breadthwise traversal from the root, expanding all successors at the current level first; FIFO queue | 8 |
| Depth-first search | Recursive traversal following each path to its greatest depth before moving to the next path; stack | 12 |
| Uniform-cost search | Search on weighted trees/graphs that expands nodes by path cost from the root using a priority queue | 17 |

## 5. Self-check questions

1. What are the factors that define a search problem? (p. 3)
2. Which four properties are used to evaluate search algorithms?
   (p. 4)
3. How do uninformed and informed search differ, and what is a
   heuristic? (pp. 6–7)
4. Which data structures implement BFS, DFS, and uniform-cost
   search? (pp. 8, 12, 17)
5. Which of the three detailed algorithms is always optimal, and
   under what condition is BFS optimal? (pp. 11, 19)

---

*Fidelity note: every section cites the source pages it was derived
from. Page 2 (Contents) is image-only and was not used. The PDF's
bookmark outline contains only generic "Slide N" markers, so modules
were derived from the per-page text; each module cites its slide
range, which maps to the outline entries. Learning objectives are not
stated verbatim in the source and are marked as implied by the section
structure. Algorithms listed but not covered in detail in the source:
iterative deepening depth-first search and bidirectional search
(p. 6); greedy search and A* search (p. 7).*
