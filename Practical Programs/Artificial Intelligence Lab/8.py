from pgmpy.models import DiscreteBayesianNetwork  # Changed from BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
# A -> B, A -> C, B -> D, C -> D
model = DiscreteBayesianNetwork([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])  # Changed from BayesianNetwork

# Define the Conditional Probability Distributions (CPDs)

# P(A)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])

# P(B|A)
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7, 0.2], [0.3, 0.8]],
                   evidence=['A'], evidence_card=[2])

# P(C|A)
cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.8, 0.5], [0.2, 0.5]],
                   evidence=['A'], evidence_card=[2])

# P(D|B,C)
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.9, 0.6, 0.7, 0.1], [0.1, 0.4, 0.3, 0.9]],
                   evidence=['B', 'C'], evidence_card=[2, 2])

# Add CPDs to the model
model.add_cpds(cpd_a, cpd_b, cpd_c, cpd_d)

# Check if the model is valid (CPDs sum to 1, etc.)
assert model.check_model()

# Create an inference object using the Variable Elimination algorithm
inference = VariableElimination(model)

# Perform various queries on the network
result = inference.query(variables=['D'], evidence={'A': 1})
result1 = inference.query(variables=['D'], evidence={'B': 1, 'C': 1})
result2 = inference.query(variables=['D'], evidence={'B': 1, 'C': 0}, show_progress=False)
result3 = inference.query(variables=['D'], evidence={'B': 0, 'C': 1}, show_progress=False)
result4 = inference.query(variables=['D'], evidence={'B': 0, 'C': 0})
result5 = inference.query(variables=['C'], evidence={'A': 1}, show_progress=False)
result6 = inference.query(variables=['C'], evidence={'A': 0}, show_progress=False)
result7 = inference.query(variables=['B'], evidence={'A': 0}, show_progress=False)

# Print the results of the queries
print("P(D | A=1)")
print(result)
print("\nP(D | B=1, C=1)")
print(result1)
print("\nP(D | B=1, C=0)")
print(result2)
print("\nP(D | B=0, C=1)")
print(result3)
print("\nP(D | B=0, C=0)")
print(result4)
print("\nP(C | A=1)")
print(result5)
print("\nP(C | A=0)")
print(result6)
print("\nP(B | A=0)")
print(result7)