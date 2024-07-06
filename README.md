# Run 
``` python3 ./src/main.py```

# Results
## Deterministic Algorithms
For nodes upto the range of 200-1000 deterministic algorithms provide a solution within 30% range of the MST bound. For smaller number of nodes (~20), the efficacy is much worse due to no observable patterns in graph.
The node values should be in a large value range for MST lower_bound to accurately depit the optimal tsp cost.
## Genetic Algorithm 
For large values, it is infeasable to run genetic algorithm, (~2 minutes for 20 nodes). 
However, in this range (upto 20 nodes), performs much better than deterministic ones within 20-25% of the MST lower_bound.   
