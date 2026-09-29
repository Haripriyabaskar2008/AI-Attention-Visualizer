import numpy as np


def softmax(scores):
    scores = np.array(scores)
    exp_scores = np.exp(scores - np.max(scores))
    return exp_scores / np.sum(exp_scores)


def calculate_attention(query, keys):
    scores = np.dot(keys, query)

    attention_weights = softmax(scores)

    return attention_weights


def visualize_attention(tokens, attention_weights):

    print("\nAttention Visualization")
    print("=" * 40)

    for token, weight in zip(tokens, attention_weights):
        print(f"{token:15} {weight:.4f}")


# Example input
tokens = [
    "I",
    "love",
    "learning",
    "Artificial",
    "Intelligence"
]

# Query vector
query = np.array([0.5, 0.8, 0.3])

# Example key vectors
keys = np.array([
    [0.1, 0.2, 0.1],
    [0.2, 0.7, 0.3],
    [0.4, 0.6, 0.2],
    [0.8, 0.9, 0.7],
    [0.3, 0.4, 0.2]
])

attention_weights = calculate_attention(
    query,
    keys
)

visualize_attention(
    tokens,
    attention_weights
)