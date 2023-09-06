# Python-Graph
Python implementation of a graph with some basic algorithms. This graph can have numbers or letters as nodes and weights

## Usage
1. Prepare your input data:

* Create a CSV file representing the graph.
* The first three columns of the CSV file represents:
    - Origin node
    - Destination node
    - Weight

Like in this format: `Origin node`, `Destination node`, `Weight`

2. Execute:

Once you have your csv file type in your terminal the command on the current directory:

```bash
    python main.py <path to the csv file>
```

You can use the folder assets to save the CSV files that you want an type the command:

```bash
    python main.py ./assets/graph_example.csv
```
