import argparse 

parse = argparse.ArgumentParser(description="ForTest!")
parse.add_argument('integers', type=int)

print(parse.parse_args())