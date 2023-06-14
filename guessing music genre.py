import random
print("Lets play, Name That Tune!!!")

# list of genres
genres = ["pop", "rock", "hip hop", "country", "jazz"]

score = 0

# randomly choose a genre from the list
genre_choice = random.choice(genres)

# loop
while True:
    # input from user to guess the genre
    guess = input("Guess the music genre (pop, rock, hip hop, country, jazz): ")

    # check if guess is correct
    if guess == genre_choice:
        print("You guessed it! The genre was", genre_choice)
        print("SCORE: ", score + 1)
        break
    else:
        print("Wrong guess! Here's a hint: ")
        # give a different hint for each genre
        if genre_choice == "pop":
            print("HINT: Most peoples favourite type of music.")
        
        elif genre_choice == "rock":
            print("HINT: May be considered loud or noisy to some people.")
            
        elif genre_choice == "hip hop":
            print("HINT: Includes rap.")
            
        elif genre_choice == "country":
            print("HINT: Sweet Home Alabama.")
            
        elif genre_choice == "jazz":
            print("HINT: Timeless and classy.")
           