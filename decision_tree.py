import csv
import math

# Function to load data from a CSV file
def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Function to calculate entropy
def entropy(data):
    total = len(data)
    if total == 0:
        return 0
    class_labels = [row["class_buys_computer"] for row in data]
    count_yes = class_labels.count("yes")
    count_no = total - count_yes
    p_yes = count_yes / total
    p_no = count_no / total
    entropy_yes = -p_yes * math.log2(p_yes) if p_yes > 0 else 0
    entropy_no = -p_no * math.log2(p_no) if p_no > 0 else 0
    return entropy_yes + entropy_no

# Function to calculate information gain
def information_gain(data, attribute):
    total_entropy = entropy(data)
    attribute_values = [row[attribute] for row in data]
    values = set(attribute_values)
    weighted_entropy = 0
    for value in values:
        subset = [row for row in data if row[attribute] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)
    gain = total_entropy - weighted_entropy
    print(f"Information Gain for {attribute}: {gain:.4f}")
    return gain

# Function to split data based on an attribute value
def split_data(data, attribute, value):
    return [row for row in data if row[attribute] == value]

# Function to build the decision tree
def build_tree(data, attributes):
    # If all examples are positive, return "yes"
    if all(row['class_buys_computer'] == 'yes' for row in data):
        return "yes"
    # If all examples are negative, return "no"
    if all(row['class_buys_computer'] == "no" for row in data):
        return "no"
    # If no more attributes to split, return the majority class
    if not attributes:
        count_yes = sum(1 for row in data if row["class_buys_computer"] == "yes")
        count_no = len(data) - count_yes
        return "yes" if count_yes >= count_no else "no"

    # Find the best attribute to split on
    best_attribute = max(attributes, key=lambda attr: information_gain(data, attr))
    tree = {best_attribute: {}}

    # Split the data and build subtrees
    for value in set(row[best_attribute] for row in data):
        subset = split_data(data, best_attribute, value)
        subtree = build_tree(subset, [attr for attr in attributes if attr != best_attribute])
        tree[best_attribute][value] = subtree

    return tree

# Function to display the decision tree
def display_tree(tree, indent=""):
    if isinstance(tree, dict):
        for key, value in tree.items():
            print(f"{indent}{key}")
            display_tree(value, indent + "  ")
    else:
        print(f"{indent}--> {tree}")

# Function to get user input for prediction
def get_user_input():
    age = input("Enter Age: 1 - Youth, 2 - Middle-aged, 3 - Senior: ")
    age_map = {"1": "youth", "2": "middle_aged", "3": "senior"}
    income = input("Enter Income: 1 - High, 2 - Medium, 3 - Low: ")
    income_map = {"1": "low", "2": "medium", "3": "high"}
    student = input("Are you a Student: 1 - Yes, 2 - No: ")
    student_map = {"1": "yes", "2": "no"}
    credit_rating = input("Enter Credit Rating: 1 - Fair, 2 - Excellent: ")
    credit_rating_map = {"1": "fair", "2": "excellent"}
    
    return {
        'age': age_map.get(age, "youth"), 
        'income': income_map.get(income, "medium"), 
        'student': student_map.get(student, "no"), 
        'credit_rating': credit_rating_map.get(credit_rating, "fair")
    }

# Function to predict the class for a given instance
def predict(tree, instance):
    if not isinstance(tree, dict):
        return tree
    attribute = next(iter(tree))
    value = instance[attribute]
    subtree = tree[attribute].get(value, "no")
    return predict(subtree, instance)

# Main function
def main():
    filename = "decision_tree.csv"
    data = load_data(filename)
    attributes = ['age', 'income', 'student', 'credit_rating']
    tree = build_tree(data, attributes)
    print("\nDecision Tree:")
    display_tree(tree)
    print("\nPrediction Process:")
    instance = get_user_input()
    prediction = predict(tree, instance)
    print(f"\nFinal Prediction for class_buys_computer: {prediction}")

if __name__ == "__main__":
    main()