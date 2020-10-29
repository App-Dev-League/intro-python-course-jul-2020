class Radio:
    def __init__(self, cur_song, channel):
        self.cur_song = cur_song
        self.channel = channel
    
    def is_good_song(self, song):
        if song.lower() == "animals" or song.lower() == "the box":
            return True
        else:
            return False
        
        