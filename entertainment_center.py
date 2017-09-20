import fresh_tomatoes
import media

#Avatar instance
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
#Print(avatar.storyline)
#Harry Potter instance
harry_potter = media.Movie("Harry Potter",
                         "On his 11th birthday, Harry Potter learns that he's a powerful wizard with a place waiting for him at the Hogwarts School of Witchcraft and Wizardry.",
                         "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone_(film)#/media/File:Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG",
                         "https://www.youtube.com/watch?v=PbdM1db3JbY")
#Get Out instance
get_out = media.Movie("Get Out",
                      "Get Out is a 2017 horror/racial satire film",
                      "https://en.wikipedia.org/wiki/Get_Out_(film)#/media/File:Teaser_poster_for_2017_film_Get_Out.png",
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")

#Salt instance
salt = media.Movie("salt",
                   "A CIA agent goes on the run after a defector accuses her of being a Russian spy",
                   "https://en.wikipedia.org/wiki/Salt_(2010_film)#/media/File:Salt_film_theatrical_poster.jpg",
                   "https://www.youtube.com/watch?v=QZ40WlshNwU")


movies = [avatar, harry_potter, get_out, salt]
fresh_tomatoes.open_movies_page(movies)


