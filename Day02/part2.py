from termcolor import colored

def decode_lines_to_games(lines):
  games = []
  for i in range(len(lines)):
    game_id = lines[i].split(':')[0].split(' ')[1]
    game_data = {
      'id': game_id,
      "red": [],
      "green": [],
      "blue": []
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

  games = decode_lines_to_games(lines)

  games_min_dice = []
  total = 0

  for game in games: 
    game_id = game['id']
    gmd = {
      'id': game_id,
    }
    for key, value in game.items():
      if key != 'key': gmd[key] = max([int(x) for x in value])
    games_min_dice.append(gmd)

    d1, d2, d3 = [int(v) for k, v in gmd.items() if k != 'id']
    print(colored(f'game: {game_id}, d1: {d1}, d2: {d2}, d3: {d3}, multiplied total: {(d1 * d2 * d3)}', 'cyan'))
    total += (d1 * d2 * d3)
  print(games_min_dice)
  print(total)