from tabulate import tabulate

def gantt_chart(processes):
    start_times = []
    waiting_time = 0
    for i in range(len(processes)):
        start_times.append(waiting_time)
        waiting_time += processes[i][2]
    
    process_names = [f"P{i+1}" for i in range(len(processes))]

    header = "____________________"
    process_row = "|" + "|".join([f" {name} " for name in process_names]) + "|"
    line_row = "|" + "|".join(["‾" * 4 for _ in range(len(processes))]) + "|"

    gantt_row = ""
    for time in start_times:
        gantt_row += f"{time:^5}"
    gantt_row += str(start_times[-1] + processes[-1][2])

    print(header)
    print(process_row)
    print(line_row)
    print(gantt_row)

def fcfs(processes):
    start_times = []
    waiting_time = 0
    for i in range(len(processes)):
        start_times.append(waiting_time)
        waiting_time += processes[i][2]
    total_waiting_time = 0
    total_completion_time = 0
    result_processes = []
    for i in range(len(start_times)):
        waiting_time = start_times[i] - processes[i][1]
        completion_time = start_times[i] + processes[i][2]
        result_processes.append([i+1, waiting_time, completion_time])
        total_waiting_time += waiting_time
        total_completion_time += completion_time
    headers = ["Process ID", "Waiting Time(ms)", "Completion Time(ms)"]
    table = tabulate(result_processes, headers)
    print(table)
    return total_waiting_time / len(processes), total_completion_time / len(processes)

if __name__ == "__main__":
    processes = [[1, 0, 3], [2, 2, 5], [3, 4, 2], [4, 6, 4]]
    # processes = []
    # process_number = int(input("Enter of number processes: "))
    # for i in range(process_number):
    #     process_id = i+1
    #     arrival_time, brust_time = input(f"Enter arrival time, brust time of P{process_id}: ").split()
    #     processes.append([process_id, float(arrival_time), float(brust_time)])
    
    sort_processes = sorted(processes, key=lambda x: x[0])
    gantt_chart(sort_processes)
    headers = ["Process ID", "Arrival Time(ms)", "Burst Time(ms)"]
    print(tabulate(sort_processes, headers))
    waiting_time, running_time = fcfs(sort_processes)
    print(f"Average waiting time: {waiting_time}ms")
    print(f"Average completion time: {running_time}ms")