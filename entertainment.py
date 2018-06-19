import media
import fresh_tomatoes


# Creating objects of class media and passing movie name,
# description, poster image URL and trailer link URL as parameters.
sanam_re = media.Movie("Sanam Re",
                       "A story of man helping a women and their love story",
                       "https://www.songsmp3.co/assets/images/1/46410-1935121_"
                       "1074463212597897_3977496040057153790_n.jpg",
                       "https://www.youtube.com/watch?v=fvQZkpnb764"
                       )

aashiqui2 = media.Movie("Aashiqui 2",
                        "Singer meets bar singer and their love story begins",
                        "http://media1.santabanta.com/full1/Bollywood%20Movies"
                        "/Aashiqui%202/aashiqui-2-4d.jpg",
                        "https://www.youtube.com/watch?v=FyXXgpPqe6w"
                        )

baagi = media.Movie("Baagi",
                    "A movie with a sweet love story and action thrillers",
                    "http://media2.intoday.in/aajtak/images/stories/"
                    "042016/film_sm_650_042916032219.jpg",
                    "https://www.youtube.com/watch?v=FV-3avN3Oxc"
                    )

dangal = media.Movie("Dangal",
                     "A story of a father who empowers her daughters",
                     "https://upload.wikimedia.org/wikipedia/"
                     "en/9/99/Dangal_Poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g"
                     )

bahubali_beginning = media.Movie("Bahubali: The Beginning",
                                 "A story of a man realising his power",
                                 "http://www.cinejosh.com/newsimg/newsmainimg/"
                                 "bahubali-maa-tv-premieres-on-october-25"
                                 "_b_2909150516.jpg",
                                 "https://www.youtube.com/watch?v=sOEg_YZQsTI"
                                 )

bahubali_conclusion = media.Movie("Bahubali: The Conclusion",
                                  "Knowing why Katappa killed bahubali",
                                  "http://songspksongspk.xyz/wp-content/"
                                  "uploads/2017/02/"
                                  "Bahubali-2-Songs-Download.jpg",
                                  "https://www.youtube.com/watch?v=6fpJaMUJLV4"
                                  )

# creating a list of all the movies
list_of_movies = [
                  sanam_re,
                  aashiqui2,
                  baagi,
                  dangal,
                  bahubali_beginning,
                  bahubali_conclusion
                  ]

# sending the list to fresh_tomatoes.py file to open web page
fresh_tomatoes.open_movies_page(list_of_movies)
