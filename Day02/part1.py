from termcolor import colored

maxes = {
  'red': 12,
  'blue': 14,
  'green': 13,
}

def decode_lines_to_games(lines):
  games = []
  for i in range(len(lines)):
    game_id = lines[i].split(':')[0].split(' ')[1]
    game_data = {
      'id': game_id,
      "red": [],
      "blue": [],
      "green": []
    }
    
    scores = lines[i].split(":")[1].split(';')
    for score in scores:
      cubes = score.split(',')
      for cube in cubes:
        cube_str = cube.strip()
        s, c = cube_str.split(' ')[0], cube_str.split(' ')[1]
        game_data[c].append(s)
    games.append(game_data)
  return games

with open("input.txt") as file:
  lines = file.readlines()
  games = []

  games = decode_lines_to_games(lines)
  
  winning_games = []
  score = 0
  
  successful_games = [game for game in games]
  
  for i in range(len(games)):
    game = games[i]
    game_id = game['id']
    #print(colored(f'game: {game}', 'cyan'))
    good_games = {
      'id': f'{game_id}',
    }
    gi = []
    for key, value in maxes.items():
      sg = [int(x) for x in game[key] if int(x) <= value ]
      good_games[key] = sg
      if len(good_games[key]) < len(game[key]):
        print(colored(f'found bad game: {game_id}, failing game: {key}. expected less than {value}, got {game[key]}', 'red'))
        break
      else:
        gi.append(game_id)
    if len(gi) == 3:
      winning_games.append(game_id)
      score += int(gi[0])
      print(colored(f'found good game: {game_id}', 'green'))
  new_winning_games = []
  [new_winning_games.append(int(x)) for x in winning_games if x not in new_winning_games]
  new_score = sum([int(x) for x in new_winning_games])
  print(colored(f'score: {new_score}', 'white', 'on_light_magenta', attrs=['blink']))