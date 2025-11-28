# Task 1: AI-Powered Code Completion
# Comparing Manual vs AI-Suggested Implementations

"""
Task: Write a Python function to sort a list of dictionaries by a specific key.
"""

# ============================================
# MANUAL IMPLEMENTATION
# ============================================

def sort_dict_list_manual(dict_list, key, reverse=False):
    """
    Manually implemented function to sort a list of dictionaries by a specific key.
    
    Args:
        dict_list (list): List of dictionaries to sort
        key (str): The key to sort by
        reverse (bool): If True, sort in descending order
    
    Returns:
        list: Sorted list of dictionaries
    
    Time Complexity: O(n log n)
    Space Complexity: O(n) due to sorted() creating a new list
    """
    # Validate input
    if not dict_list:
        return []
    
    # Check if key exists in all dictionaries
    for item in dict_list:
        if key not in item:
            raise KeyError(f"Key '{key}' not found in all dictionaries")
    
    # Sort using sorted() with lambda function
    return sorted(dict_list, key=lambda x: x[key], reverse=reverse)


# ============================================
# AI-SUGGESTED IMPLEMENTATION (GitHub Copilot style)
# ============================================

def sort_dict_list_ai(dict_list, key, reverse=False):
    """
    AI-suggested function to sort a list of dictionaries by a specific key.
    
    This version uses operator.itemgetter for better performance.
    """
    from operator import itemgetter
    
    # Using itemgetter is more efficient than lambda for simple key access
    return sorted(dict_list, key=itemgetter(key), reverse=reverse)


# ============================================
# TEST CASES
# ============================================

if __name__ == "__main__":
    # Sample data
    employees = [
        {"name": "Alice", "age": 30, "salary": 70000},
        {"name": "Bob", "age": 25, "salary": 50000},
        {"name": "Charlie", "age": 35, "salary": 90000},
        {"name": "Diana", "age": 28, "salary": 60000}
    ]
    
    print("Original list:")
    for emp in employees:
        print(emp)
    
    print("\n" + "="*50)
    print("MANUAL IMPLEMENTATION - Sort by age:")
    print("="*50)
    sorted_manual = sort_dict_list_manual(employees, "age")
    for emp in sorted_manual:
        print(emp)
    
    print("\n" + "="*50)
    print("AI-SUGGESTED IMPLEMENTATION - Sort by age:")
    print("="*50)
    sorted_ai = sort_dict_list_ai(employees, "age")
    for emp in sorted_ai:
        print(emp)
    
    print("\n" + "="*50)
    print("Sort by salary (descending):")
    print("="*50)
    sorted_salary = sort_dict_list_ai(employees, "salary", reverse=True)
    for emp in sorted_salary:
        print(emp)
    
    # Performance comparison
    import timeit
    
    large_dataset = [{"id": i, "value": i % 100} for i in range(10000)]
    
    manual_time = timeit.timeit(
        lambda: sort_dict_list_manual(large_dataset, "value"),
        number=1000
    )
    
    ai_time = timeit.timeit(
        lambda: sort_dict_list_ai(large_dataset, "value"),
        number=1000
    )
    
    print("\n" + "="*50)
    print("PERFORMANCE COMPARISON (10,000 items, 1000 iterations):")
    print("="*50)
    print(f"Manual implementation: {manual_time:.4f} seconds")
    print(f"AI-suggested implementation: {ai_time:.4f} seconds")
    print(f"Speed improvement: {((manual_time - ai_time) / manual_time * 100):.2f}%")
