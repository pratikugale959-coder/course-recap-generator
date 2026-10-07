# AI & ML Important Questions with Answers — Course Recap

- **Source:** course.pdf — "AI & ML Important Questions with Answers"
- **Format:** Q&A study sheet (10 questions), Microsoft Word / python-docx
- **Pages:** 3
- **Generated:** 2026-10-07

## 1. Course overview

This document is a set of AI & ML important questions with
answers, in Q&A format. It covers learning through problem
solving, the A* algorithm and heuristic path planning, the
difference between uninformed and informed search, state
spaces, the three learning paradigms (supervised,
unsupervised, reinforcement), k-means clustering, k-NN, and
regression for electricity load forecasting. Each question is
self-contained and includes definitions, formulas,
comparisons, and worked examples (robot pathfinding,
warehouse robots, resource allocation, product quality
inspection, load forecasting) — except Q6, which the source
marks as a duplicate of Q4.

## 2. Learning objectives

The source does not state learning objectives verbatim; they
are implied by the question set:

- Explain learning through problem solving with an example (Q1)
- Describe how the A* algorithm is used for efficient robot
  path planning (Q2)
- Compare uninformed and informed search algorithms (Q3)
- Define state space and illustrate it with a
  resource-allocation example (Q4, Q6)
- Explain the core principle of the A* algorithm (Q5)
- Distinguish supervised, unsupervised, and reinforcement
  learning (Q7)
- Explain how k-means clustering helps group products for
  quality inspection (Q8)
- Compare k-NN and k-means (Q9)
- Explain how regression can forecast electricity load demand
  (Q10)

## 3. Module-by-module recap

### Module 1: Q1 — Learning through Problem Solving (page 1)

**Topics:** definition; robot pathfinding example

**Key takeaways:**

- Learning through problem solving is a process where
  knowledge is gained by actively finding solutions to problems
  rather than just memorizing theory (p. 1)
- It improves understanding and develops reasoning ability
  (p. 1)
- Example — a robot finding the shortest path to a
  destination: first attempt tries random paths and reaches
  late; it learns which routes were blocked; second attempt
  avoids those blocked paths and reaches faster (p. 1)
- The robot learns from experience and improves over time
  (p. 1)

### Module 2: Q2 — A* Algorithm for Efficient Robot Path Planning (page 1)

**Topics:** A* formula; working steps; warehouse example

**Key takeaways:**

- A* (A-star) is a popular pathfinding algorithm used for
  robots because it finds the shortest path efficiently (p. 1)
- Formula: f(n) = g(n) + h(n) — g(n) is the cost from the
  start node to the current node; h(n) is the estimated cost
  (heuristic) from the current node to the goal (p. 1)
- Working: start from the initial position; explore
  neighboring nodes; always choose the node with the smallest
  f(n); continue until the goal is reached (p. 1)
- Example — a warehouse robot uses A* to move from the entry
  point to a storage rack: g(n) = distance travelled so far,
  h(n) = straight-line distance to goal; the robot avoids
  unnecessary nodes and reaches in the shortest time (p. 1)
- Note: the outline title reads "A Algorithm" (the asterisk
  is missing from the source bookmark); the body text uses
  "A* (A-star)" (p. 1)

### Module 3: Q3 — Fundamental Difference between Uninformed and Informed Search Algorithms (page 2)

**Topics:** blind vs heuristic search comparison

**Key takeaways:**

- Uninformed search (blind search) explores the state space
  without any extra knowledge, whereas informed search uses
  heuristics to guide the search (p. 2)
- Knowledge used: uninformed uses no extra info; informed
  uses heuristics (p. 2)
- Efficiency: uninformed explores more nodes (slow); informed
  explores fewer nodes (fast) (p. 2)
- Examples: BFS, DFS (uninformed) vs A*, Greedy Best-First
  (informed) (p. 2)

### Module 4: Q4 — State Space in AI Problem Solving (page 2)

**Topics:** state space definition; resource-allocation example

**Key takeaways:**

- State space: the set of all possible states or
  configurations of a problem that can be reached from the
  initial state by applying operators (p. 2)
- Resource-allocation example: 2 tasks (T1, T2) and 2
  machines (M1, M2); possible states (allocations) are
  S1: (T1→M1, T2→M2) and S2: (T1→M2, T2→M1), so the state
  space = {S1, S2} (p. 2)
- The algorithm explores these states to find the best
  allocation (e.g., minimum processing time) (p. 2)

### Module 5: Q5 — Core Principle of the A* Algorithm (page 2)

**Topics:** lowest estimated total cost; admissible heuristic

**Key takeaways:**

- The core principle of A* is to expand the node that has
  the lowest estimated total cost: f(n) = g(n) + h(n) (p. 2)
- g(n): actual cost from start; h(n): heuristic estimate to
  goal (p. 2)
- This ensures optimal and efficient pathfinding if h(n) is
  admissible (p. 2)

### Module 6: Q6 — State Space in AI Problem Solving (page 2)

**Topics:** duplicate of Q4

**Key takeaways:**

- The source marks this question as a duplicate: "Same as Q4
  — refer to Q4 for solution" (p. 2)

### Module 7: Q7 — Supervised, Unsupervised, and Reinforcement Learning (pages 2–3)

**Topics:** the three learning paradigms

**Key takeaways:**

- Supervised learning: the model learns from labeled data
  (input-output pairs); example: predicting house price (p. 2)
- Unsupervised learning: the model finds patterns in
  unlabeled data; example: customer segmentation (p. 2)
- Reinforcement learning: the agent learns by interacting
  with the environment and receiving rewards/penalties;
  example: a robot learning to navigate a maze (p. 3)

### Module 8: Q8 — K-Means Clustering for Product Quality Inspection (page 3)

**Topics:** k-means definition; manufacturing application

**Key takeaways:**

- K-means is an unsupervised clustering algorithm that groups
  similar items together (p. 3)
- In manufacturing: input features are weight, size, and
  defect count; the algorithm groups products into k clusters
  — Cluster 1: good quality, Cluster 2: minor defects,
  Cluster 3: major defects (p. 3)
- This helps the quality team focus on defective products
  quickly (p. 3)

### Module 9: Q9 — Comparing k-NN and k-Means (page 3)

**Topics:** supervised vs unsupervised; training; use cases

**Key takeaways:**

- k-NN (k-Nearest Neighbors): supervised algorithm; assigns
  a label based on nearest neighbors; used for
  classification/regression (p. 3)
- k-Means: unsupervised algorithm; divides data into k
  clusters by minimizing distance from centroids; used for
  clustering (p. 3)
- Training: k-NN is a lazy learner (no explicit training);
  k-Means needs iterative training (p. 3)
- Use cases: k-NN → handwriting recognition; k-Means →
  market segmentation (p. 3)

### Module 10: Q10 — Regression for Electricity Load Forecasting (page 3)

**Topics:** regression definition; load forecasting example

**Key takeaways:**

- Regression is used to predict continuous values based on
  historical data (p. 3)
- Example: inputs are hour of day, temperature, and day type
  (weekday/holiday); output is the predicted electricity load
  (MW) (p. 3)
- The model learns the relationship: Load = a +
  b1(Temperature) + b2(Hour) + b3(Day) (p. 3)
- This forecast helps power companies plan generation
  schedules and avoid shortages (p. 3)

## 4. Glossary

| Term | Definition | Source page(s) |
| --- | --- | --- |
| Learning through problem solving | A process where knowledge is gained by actively finding solutions rather than memorizing theory | 1 |
| A* algorithm | Pathfinding algorithm that finds the shortest path efficiently; f(n) = g(n) + h(n) | 1–2 |
| Heuristic (h(n)) | Estimated cost from the current node to the goal; A* is optimal and efficient if h(n) is admissible | 1–2 |
| Uninformed (blind) search | Search that explores the state space without any extra knowledge | 2 |
| Informed search | Search that uses heuristics to guide the search | 2 |
| State space | The set of all possible states or configurations reachable from the initial state by applying operators | 2 |
| Supervised learning | Model learns from labeled data (input-output pairs) | 2 |
| Unsupervised learning | Model finds patterns in unlabeled data | 2 |
| Reinforcement learning | Agent learns by interacting with the environment and receiving rewards/penalties | 3 |
| K-means | Unsupervised clustering algorithm that groups similar items by minimizing distance from centroids | 3 |
| k-NN | Supervised algorithm that assigns a label based on nearest neighbors | 3 |
| Regression | Predicts continuous values based on historical data | 3 |

## 5. Self-check questions

1. What is learning through problem solving, and how does the
   robot example illustrate it? (p. 1)
2. What is the A* formula, and what do g(n) and h(n)
   represent? (pp. 1–2)
3. How do uninformed and informed search differ in knowledge
   used, efficiency, and examples? (p. 2)
4. What is a state space? Illustrate it with the
   resource-allocation example. (p. 2)
5. What is the core principle of A*, and when does it
   guarantee optimal pathfinding? (p. 2)
6. How do supervised, unsupervised, and reinforcement learning
   differ? (pp. 2–3)
7. How does k-means help group products for quality
   inspection? (p. 3)
8. How do k-NN and k-means compare in training and use cases?
   (p. 3)
9. How can regression forecast electricity load demand? (p. 3)

---

*Fidelity note: every section cites the source pages it was
derived from. All 3 pages extracted cleanly (no scanned-page
warnings). Q6 is a duplicate of Q4 in the source ("Same as
Q4 — refer to Q4 for solution") and is represented as such.
Q7's answer spans pages 2–3. The outline's Q2 bookmark title
omits the asterisk ("A Algorithm"); the body text uses
"A* (A-star)". Learning objectives are not stated verbatim in
the source and are listed as implied by the question set.*
