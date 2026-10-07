# Key Concepts — AI & ML Important Questions with Answers

Source: `work/course-content.json` (extracted from input/course.pdf,
"AI & ML Important Questions with Answers", 3 pages)

| Concept | Definition | Source page(s) | Why it matters |
| --- | --- | --- | --- |
| learning-through-problem-solving | A process where knowledge is gained by actively finding solutions to problems rather than just memorizing theory; improves understanding and develops reasoning ability | 1 | The document's opening concept, illustrated by the robot pathfinding example |
| a-star-algorithm | Popular pathfinding algorithm that finds the shortest path efficiently; formula f(n) = g(n) + h(n); working: start from the initial position, explore neighboring nodes, always choose the node with the smallest f(n), continue until the goal is reached | 1–2 | Used for efficient robot path planning (warehouse example); its core principle is Q5 |
| heuristic-function | h(n): the estimated cost (heuristic) from the current node to the goal; A* ensures optimal and efficient pathfinding if h(n) is admissible | 1–2 | The guide that lets informed search explore fewer nodes than uninformed search |
| uninformed-search | Blind search: explores the state space without any extra knowledge; explores more nodes (slow); examples BFS, DFS | 2 | One half of the Q3 comparison |
| informed-search | Uses heuristics to guide the search; explores fewer nodes (fast); examples A*, Greedy Best-First | 2 | The other half of the Q3 comparison; more efficient than uninformed search |
| state-space | The set of all possible states or configurations of a problem reachable from the initial state by applying operators; illustrated with 2 tasks × 2 machines (states S1, S2) | 2 | What search algorithms explore; basis of the resource-allocation example |
| supervised-learning | Model learns from labeled data (input-output pairs); example: predicting house price | 2 | One of the three learning paradigms in Q7 |
| unsupervised-learning | Model finds patterns in unlabeled data; example: customer segmentation | 2–3 | The paradigm behind k-means (Q8, Q9) |
| reinforcement-learning | Agent learns by interacting with the environment and receiving rewards/penalties; example: a robot learning to navigate a maze | 3 | The third learning paradigm in Q7 |
| k-means-clustering | Unsupervised clustering algorithm that groups similar items by minimizing distance from centroids; needs iterative training; in manufacturing, groups products by weight, size, and defect count into good / minor-defect / major-defect clusters | 3 | Helps the quality team focus on defective products quickly |
| k-nearest-neighbors | Supervised algorithm that assigns a label based on nearest neighbors; used for classification/regression; lazy learner (no explicit training); use case: handwriting recognition | 3 | Contrasted with k-means in Q9 |
| regression | Predicts continuous values based on historical data; example model: Load = a + b1(Temperature) + b2(Hour) + b3(Day) | 3 | Forecasts electricity load (MW) so power companies can plan generation schedules and avoid shortages |
