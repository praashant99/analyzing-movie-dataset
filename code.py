# --------------
import pandas as pd
import numpy as np
import csv



opened_file = open(path, encoding="utf8")
read_file = csv.reader(opened_file)
movies = list(read_file)

movies_header=movies[0]
del movies[0]
del movies[4553]


def explore_data(dataset,start,end,row_columns=False):
    for c in range(start,end):
        dataset[c]
    return c 

exloredata=explore_data(movies,0,5)

def duplicate_and_unique_movies(dataset, index_):
    c=pd.DataFrame(dataset)
    f=c[c.duplicated(index_,keep=False)]
    return f


duplicate=duplicate_and_unique_movies(movies,13)

c=np.array(movies)[:,13].tolist()
d=np.array(movies)[:,12].tolist()

reviews_max=dict(zip(c,d))


movies_clean1=pd.DataFrame(movies)
movies_clean1=movies_clean1[movies_clean1.duplicated(13,keep=False)]
movies_clean1=movies_clean1.drop(movies_clean1.index[[2,3,5]])
movies_clean=movies_clean1.values.tolist()


def movies_lang(dataset, index_, lang_):
    f=pd.DataFrame(dataset)
    c=f[f[index_]==lang_]
    return c
    
movies_en=movies_lang(movies,3,'en')



def rate_bucket(dataset,rate_high,rate_low):
    z=pd.read_csv(path)
    x=z[(z['vote_average']>=rate_high)&(z['original_language']=='en')]
    return x

high_rated_movies=rate_bucket(movies,8.0,7)
print(high_rated_movies.shape)













# Read the data file and store it as a list 'movies'




# The first row is header. Extract and store it in 'movies_header'.


# Subset the movies dataset such that the header is removed from the list and store it back in movies




# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.



# Using explore_data() with appropriate parameters, view the details of the first 5 movies.




# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.




# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.



# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 




# Calling movies_lang(), extract all the english movies and store it in movies_en.




# Call the rate_bucket function to see the movies with rating higher than 8.



