import pyverilog.vparser.ast as vast
from pyverilog.vparser.parser import parse
import random

# Function to parse Verilog files and extract signal names
def parse_verilog_files(top_level_file, testbench_file):
    ast, _ = parse([top_level_file, testbench_file])
    return ast

# Function to simulate random clock generation
def simulate_random_clock(simulation_time_ns):
    random.seed(12345)
    clk_values = []
    current_time = 0

    # Start with a rising edge at time zero
    clk_values.append((0, 1))

    while current_time < simulation_time_ns:
        delay_rising = random.randint(5, 15)
        delay_falling = random.randint(5, 15)

        current_time += delay_rising
        clk_values.append((current_time, 0))  # Rising edge

        if current_time >= simulation_time_ns:
            break

        current_time += delay_falling
        clk_values.append((current_time, 1))  # Falling edge

    return clk_values

# Function to simulate data stream based on the RTL module
def simulate_data_stream(clk_values):
    counter = 0
    data_stream = []
    for time, clk in clk_values:
        if clk == 0:  # Rising edge
            counter += 1
        data_stream.append((time, counter))  # Store the entire counter value
    return data_stream

# Function to analyze data stream
def analyze_data_stream(data_stream):
    analysis = []
    for i in range(1, len(data_stream)):
        prev_time, prev_value = data_stream[i - 1]
        curr_time, curr_value = data_stream[i]
        if curr_value > prev_value:
            behavior = "Incrementing"
        elif curr_value < prev_value:
            behavior = "Decrementing"
        else:
            behavior = "Constant"
        analysis.append((prev_time, curr_time, prev_value, curr_value, behavior))
    return analysis

# Function to write results to file
def write_results_to_file(analysis, filename):
    with open(filename, 'w') as file:
        file.write("Cycle Analysis:\n")
        file.write("Start Time (ns) - End Time (ns): Previous Value -> Current Value [Behavior]\n")
        for start_time, end_time, prev_value, curr_value, behavior in analysis:
            file.write(f"{start_time} - {end_time}: {prev_value} -> {curr_value} [{behavior}]\n")
import subprocess

# Example command execution
cmd = ["path_to_executable", "arg1", "arg2"]
print(f"Executing command: {' '.join(cmd)}")

try:
    subprocess.call(cmd)
except FileNotFoundError as e:
    print(f"Error executing command: {e}")
    # Handle the error or further investigate


# Main script
if __name__ == "__main__":
    top_level_file = "C:\\Users\Administrator\Downloads\\Qnu_Labs-codespace-cautious-robot-66w7q79p764f6xg\\counter.v"
    testbench_file = "C:\\Users\Administrator\Downloads\\Qnu_Labs-codespace-cautious-robot-66w7q79p764f6xg\\counter_tb.v"

    # Parse Verilog files
    ast = parse_verilog_files(top_level_file, testbench_file)
    print("Parsed AST:", ast)

    # Simulate random clock generation
    simulation_time_ns = 100
    clk_values = simulate_random_clock(simulation_time_ns)

    # Simulate data stream
    data_stream = simulate_data_stream(clk_values)

    # Analyze data stream
    analysis = analyze_data_stream(data_stream)

    # Write results to file
    filename = "data_stream_cycle_analysis_results.txt"
    write_results_to_file(analysis, filename)

    print(f"Data stream cycle analysis results written to '{filename}'")
