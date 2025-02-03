def get_user_input():
    # Simple CLI-based input collection, can be extended to a GUI later
    num_processes = int(input("Enter number of processes: "))
    processes = []
    for i in range(num_processes):
        arrival = float(input(f"Process {i+1} arrival time: "))
        burst = float(input(f"Process {i+1} burst time: "))
        priority = int(input(f"Process {i+1} priority: "))
        processes.append({'id': i+1, 'arrival': arrival, 'burst': burst, 'priority': priority})
    return processes
