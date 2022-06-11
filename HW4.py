import os

import bz2

import pandas

from urllib.request import urlopen

url = "https://database.lichess.org/lichess_db_puzzle.csv.bz2"
bz2_filename = "puzzles.csv.bz2"
header = ["PuzzleId", "FEN", "Moves",
          "Rating", "RatingDeviation",
          "Popularity", "NbPlays",
          "Themes", "GameUrl"]

final_filename = "puzzles.csv"
if os.path.isfile(bz2_filename):
    print("File {} was already downloaded. Proceeding with decompress...".format(bz2_filename))

else:
    print("Downloading the file {}  from url {}".format(bz2_filename, url))

    with urlopen(url) as data, open(bz2_filename, "wb") as file:
        file.write(data.read())
    print("{} Download complete! Proceeding with decompress...".format(bz2_filename))

if os.path.isfile(final_filename):
    print("File was already decompressed into {}".format(final_filename))

else:
    with bz2.open(bz2_filename, "rt") as filefrom, open(final_filename, "w") as fileto:
        fileto.write(filefrom.read())
    print("{} successfully decompressed into {}!".format(bz2_filename, final_filename))
puzzles = pandas.read_csv(final_filename, names = header)
print(puzzles.head())
