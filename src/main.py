from input_module import get_user_input
from scheduler import fcfs, sjf, round_robin, priority
from visualization.gantt_chart import draw_gantt_chart
from analytics.metrics import compute_metrics

def main():
    processes = get_user_input()
    # For example, run FCFS scheduling
    schedule = fcfs.schedule_processes(processes)
    metrics = compute_metrics(schedule)
    draw_gantt_chart(schedule, title="FCFS Scheduling")
    print(metrics)

if __name__ == "__main__":
    main()
