import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firestore
cred = credentials.Certificate("classroom.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#CREATE PLAYLIST
# CRUD Functions
def create_playlist():
    playlist_name = input("Enter the playlist name: ")
    playlist_ref = db.collection("playlists").add({"name": playlist_name})
    print(f"Playlist '{playlist_name}' created with ID: {playlist_ref[1].id}")

#ADD SONG FUCTION
def add_song():
    get_playlists()  
    playlist_id = input("Enter the playlist ID for the song: ")
    song_name = input("Enter song name: ")
    artist_name = input("Enter artist name: ")
    duration = input("Enter duration (e.g., 3:45): ")

    # Create a new song document and associate it with a playlist by using playlist_id
    new_song_ref = db.collection("songs").document()
    new_song_ref.set({
        "playlist_id": playlist_id,
        "name": song_name,
        "artist": artist_name,
        "duration": duration,
    })
    print(f"Song '{song_name}' added with ID: {new_song_ref.id} to playlist ID: {playlist_id}")

def get_playlists():
    print("\nAvailable Playlists:")
    playlists = db.collection("playlists").get()
    for playlist in playlists:
        print(f"ID: {playlist.id}, Name: {playlist.to_dict()['name']}")

def view_songs():
    playlist_id = input("Enter the playlist ID to view songs: ")
    results = db.collection("songs").where("playlist_id", "==", playlist_id).get()
    if not results:
        print("No songs found in this playlist.")
        return
    print("\nSongs in Playlist:")
    for result in results:
        data = result.to_dict()
        print(f"ID: {result.id} - {data['name']} by {data['artist']}, Duration: {data['duration']}")

#UPDATE AND DELETE FUNCTIONS
def update_song():
    song_id = input("Enter the song ID to update: ")
    new_name = input("Enter new song name (leave blank to keep current): ")
    new_artist = input("Enter new artist name (leave blank to keep current): ")
    new_duration = input("Enter new duration (leave blank to keep current): ")
    updates = {}
    if new_name:
        updates["name"] = new_name
    if new_artist:
        updates["artist"] = new_artist
    if new_duration:
        updates["duration"] = new_duration
    db.collection("songs").document(song_id).update(updates)
    print(f"Song ID {song_id} updated.")

def delete_song():
    song_id = input("Enter the song ID to delete: ")
    db.collection("songs").document(song_id).delete()
    print(f"Song ID {song_id} deleted from playlist.")

# Main Interactive Menu
def menu():
    while True:
        print("\nMusic Playlist Manager")
        print("1. Create a new playlist")
        print("2. Add a song to a playlist")
        print("3. View all playlists")
        print("4. View songs in a playlist")
        print("5. Update a song in a playlist")
        print("6. Delete a song from a playlist")
        print("7. Exit")

        choice = input("Select an option (1-7): ")
        if choice == "1":
            create_playlist()
        elif choice == "2":
            add_song()
        elif choice == "3":
            get_playlists()
        elif choice == "4":
            view_songs()
        elif choice == "5":
            update_song()
        elif choice == "6":
            delete_song()
        elif choice == "7":
            print("Exiting the Music Playlist Manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
