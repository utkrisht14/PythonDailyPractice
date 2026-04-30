class Song:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"Song: {self.name} Name: {self.artist} Artist: {self.duration}"

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song:Song):
        for current_song in self.songs:
            if current_song.name.lower() == song.name.lower():
                print("Song already exists in the playlist.")
                return
        self.songs.append(song)
        print("Song added to the playlist.")
        return

    def view_playlist(self):
        if not self.songs:
            print("Playlist is empty.")
            return

        for playlist_data in self.songs:
            print(playlist_data)
        return

    def remove_song(self, title):
        for song in self.songs:
            if title.lower() == song.name.lower():
                self.songs.remove(song)
                print("Song removed successfully.")
                return
        else:
            print("Song not found in the playlist.")

    def calculate_playlist_duration(self):
        total_duration = 0
        for song in self.songs:
            total_duration += song.duration
        print(f"Total duration of the playlist: {total_duration} minutes")



if __name__ == "__main__":
    my_song_1 = Song("Song 1", "Artist 1", 300)
    my_song_2 = Song("Song 2", "Artist 2", 450)
    my_song_3 = Song("Song 3", "Artist 3", 240)

    my_playlist = Playlist()
    my_playlist.add_song(my_song_1)
    my_playlist.add_song(my_song_2)
    my_playlist.add_song(my_song_3)
    my_playlist.view_playlist()
    my_playlist.remove_song("Song 2")
    my_playlist.view_playlist()
    my_playlist.calculate_playlist_duration()