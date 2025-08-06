import os

input_dir = 'data_input'
output_dir = 'data_output'

if not os.path.exists(input_dir):
    os.makedirs(input_dir)
    print(f"'{input_dir}' folder created. Please add .txt files to it.")
    exit()

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

summary = []

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        line_count = 0
        word_count = 0
        modified_lines = []

        with open(input_path, 'r') as file:
            for line in file:
                if line.strip().startswith('#'):
                    continue
                line_count += 1
                word_count += len(line.split())
                modified_line = line.replace("temp", "permanent")
                modified_lines.append(modified_line)

        with open(output_path, 'w') as out_file:
            out_file.writelines(modified_lines)

        summary.append(f"{filename}\nLines: {line_count}\nWords: {word_count}\n")

summary_path = os.path.join(output_dir, 'summary.txt')
with open(summary_path, 'w') as summary_file:
    summary_file.write('\n'.join(summary))

print(" Check the 'data_output' folder.")