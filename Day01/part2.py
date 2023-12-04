
import time
import os
os.system("")

from termcolor import colored

word_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def check_for_word(string):
  #print(f'received string {string} \n')
  result = [False, 0]
  if len(string) < 3: return result
  
  for key, value in word_dict.items():
    if key in string:
      print(colored(f'found word: {key} in {string}, returning {value}', 'green'))
      result = [True, value]
      break
  return result

with open("input.txt") as f:
    lines = f.readlines()
    #print(f'{len(lines)} \n')

    total = 0

    for line in lines:
      print('***************************************************\n', line, '\n')
      line_list = [c for c in line]
      parsed_nums = []
      window_start = 0
      window_end = 0
      while window_end < len(line_list):
        frame = line_list[window_start:window_end + 1]
        print(colored(f'window start: {window_start}, window end: {window_end}, line length: {len(line_list)}, line: {line}, frame: {frame}, found numbers: {parsed_nums}', 'yellow'))
        if len(frame) > 2: 
          is_word, value = check_for_word(''.join(line_list[window_start:window_end +1]))
          if is_word == True: 
            parsed_nums.append(value)
            window_start = window_end
        if line_list[window_end].isdigit() == True:
          print(colored(f'found natural number: {line_list[window_end]}, returning', 'yellow'))
          parsed_nums.append(line_list[window_end])
          window_start = window_end
        window_end += 1
        #time.sleep(0.5)
      first_and_last = [parsed_nums[0], parsed_nums[-1]]
      print(colored(f'initial String: {line}, parsed nums: {parsed_nums}, first and last: {"".join(first_and_last) }', 'cyan', 'on_dark_grey'))
      total += int(''.join(first_and_last))
    print(colored(f'TOTAL: {total}', 'blue', 'on_white'))