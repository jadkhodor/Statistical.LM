import bz2
import os
import pandas
from urllib.request import urlopen
import matplotlib.pyplot as plt
import statistics as stat
from statsmodels.nonparametric.smoothers_lowess import lowess as lowess

###taken from hw4

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


#####5
plays_median = stat.median(puzzles.NbPlays)
rating_low = 1500
rating_high = stat.quantiles(data=puzzles.Rating,n=100)[98]

puzzles_filtered = puzzles[(puzzles.NbPlays > plays_median) & (puzzles.Rating > rating_low) & (puzzles.Rating < rating_high)]
gg = puzzles_filtered[["Rating","Popularity"]]

rating_mapping = {}

for (i, rating) in enumerate(gg.Rating):
    if rating in rating_mapping.keys():
        rating_mapping[rating].append(i)
    else:
        rating_mapping[rating] = [i]

ratings = gg.Rating.unique()
mean_pop = []

for rating in ratings:
    indices = rating_mapping[rating]
    popularities = gg.iloc[indices, gg.columns.get_loc("Popularity")]
    mean_pop.append(stat.mean(popularities))

l_y, l_x = lowess(ratings, mean_pop, frac=0.25, it=5, return_sorted=True).T

plt.scatter(x=ratings, y=mean_pop)
plt.plot(l_x, l_y, color="red")
plt.xlabel = "rating"
plt.ylabel = "popularity"
plt.tight_layout()
plt.show()