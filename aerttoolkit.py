# =========================================================
# AERT TOOLKIT - Data Structures Assignment (Unit 1)
# Student Name: Navraj
# Roll No: 2501730493
# Course: Data Structures (ETCCDS202)
# =========================================================

# ------------------ PART A: STACK ADT ------------------

class StackADT:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        return "Stack Empty"

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        return "Stack Empty"

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


# ------------------ PART B: FACTORIAL ------------------

def factorial(n):
    if n < 0:
        return "Invalid Input"
    if n == 0:
        return 1
    return n * factorial(n - 1)


# ------------------ PART B: FIBONACCI ------------------

call_naive = 0
call_memo = 0

def fib_naive(n):
    global call_naive
    call_naive += 1

    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


memo = {}

def fib_memo(n):
    global call_memo
    call_memo += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


# ------------------ PART C: TOWER OF HANOI ------------------

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)


# ------------------ PART D: BINARY SEARCH ------------------

def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


# ------------------ MAIN FUNCTION ------------------

def main():

    print("=================================================")
    print("            AERT TOOLKIT OUTPUT")
    print("=================================================\n")

    # -------- STACK ADT --------
    print("----- STACK ADT -----")
    s = StackADT()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack size:", s.size())
    print("Top element:", s.peek())
    print("Pop element:", s.pop())
    print("After pop size:", s.size())

    # -------- FACTORIAL --------
    print("\n----- FACTORIAL (RECURSIVE) -----")
    test_fact = [0, 1, 5, 10]
    for n in test_fact:
        print(f"{n}! =", factorial(n))

    # -------- FIBONACCI --------
    print("\n----- FIBONACCI (NAIVE vs MEMO) -----")
    test_fib = [5, 10, 20, 30]

    for n in test_fib:
        global call_naive, call_memo, memo
        call_naive = 0
        call_memo = 0
        memo = {}

        print(f"\nN = {n}")
        print("Naive Result:", fib_naive(n), "| Calls:", call_naive)
        print("Memo Result :", fib_memo(n), "| Calls:", call_memo)

    # -------- TOWER OF HANOI --------
    print("\n----- TOWER OF HANOI (N = 3) -----")
    hanoi(3, 'A', 'B', 'C')

    # -------- BINARY SEARCH --------
    print("\n----- RECURSIVE BINARY SEARCH -----")
    arr = [1, 3, 5, 7, 9, 11, 13]
    search_keys = [7, 1, 13, 2]

    for key in search_keys:
        index = binary_search(arr, key, 0, len(arr) - 1)
        print(f"Search {key} -> Index:", index)

    # Edge case
    print("Search in empty array ->", binary_search([], 5, 0, -1))


# ------------------ RUN PROGRAM ------------------

if __name__ == "__main__":
    main()