import webbrowser


class Movie():
    """Has Movie Trailer details"""

    # Gets all values from Entertainment.py
    def __init__(self, mname, mstory, mimage, mtrailer):
        self.title = mname                      # Assigns Movie Name
        self.storyline = mstory                 # Assigns Movie Description
        self.poster_image_url = mimage          # Assigns Image URL to variable
        self.trailer_youtube_url = mtrailer     # Assigns Video URL to variable
