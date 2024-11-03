# Overview

{In this project, I developed a Music Playlist Manager as part of my learning journey in software engineering. The application allows users to create and manage playlists by adding, modifying, and deleting songs stored in a cloud database. The focus of this project was to implement CRUD functionalities (Create, Read, Update, Eliminnate) to gain experience in cloud database integration and enhance my understanding of backend interactions in web applications.}

{The Music Playlist Manager is easy to use: users can create playlists, add or remove songs, and view or edit song details. The cloud database stores each song’s information, allowing persistent data access from any device. The program also supports data retrieval for easy playlist sharing.}

{This software aims to reinforce my understanding of database integration, user interface design, and data handling in cloud environments. Developing it helped me practice implementing efficient and user-friendly data management features.}

[Software Demo Video](https://youtu.be/GGNwInU5icE)

# Cloud Database

{This project utilizes Firebase Firestore as the cloud database, chosen for its real-time capabilities and ease of integration with web applications. Firestore is structured as a NoSQL database, with each playlist stored as a collection containing documents that represent individual songs.}

{Database Structure
Playlists Collection
    * Each playlist is a document containing:
        - playlist_name: String
        - created_by: String (user ID or name)
    * Each playlist document contains a songs subcollection, where each song document includes:
        - song_id: Unique identifier for the song
        - title: Title of the song
        - artist: Artist name
        - duration: Duration in minutes/seconds
        - added_by: User ID or name of the person who added the song

This structure allows the application to retrieve and display playlists and their respective songs while maintaining an organized, relational data setup.
}

# Development Environment

{
* Code Editor: Visual Studio Code for efficient code management and debugging
* Cloud Database: Firebase Firestore for cloud-based storage and real-time data updates
* Version Control: Git and GitHub for source control and collaboration
* Programming Language: Python, utilizing the Firebase Admin SDK to manage CRUD operations, database interactions, and real-time data updates in Firestore.
}

{The software was written primarily in Python. I used the Firebase SDK to handle authentication, database operations, and real-time data updates in the application.}

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Firestore Tutorial](https://firebase.google.com/docs/firestore)
- [Firestore Console](https://firebase.google.com/docs/firestore)
- [An Introduction to Cloudd Dtabases: Chapter 1](https://www.oreilly.com/library/view/an-introduction-to/9781492044857/ch01.html)
- [Guru99](https://www.guru99.com/nosql-tutorial.html)

# Future Work

- Implement user authentication to allow personalized playlist management for each user.
- Add real-time notifications to alert users when a playlist is updated.
- Develop advanced playlist features, such as song sorting, custom playlist covers, and playlist sharing via unique links.