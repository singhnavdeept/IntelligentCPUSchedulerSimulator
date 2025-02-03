def schedule_processes(processes):
    # Sort by arrival time
    processes.sort(key=lambda x: x['arrival'])
    current_time = 0
    schedule = []
    for process in processes:
        if current_time < process['arrival']:
            current_time = process['arrival']
        start = current_time
        finish = start + process['burst']
        schedule.append({**process, 'start': start, 'finish': finish})
        current_time = finish
    return schedule
