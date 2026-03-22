from random import randint

words = [
    "apple", "banana", "cat", "dog", "elephant", "fox", "grape", "house", "ice", "jungle",
    "kite", "lemon", "monkey", "nest", "ocean", "panda", "queen", "river", "sun", "tree",
    "umbrella", "violet", "wolf", "xray", "yellow", "zebra", "bird", "cloud", "door", "egg",
    "fish", "goat", "hat", "island", "jar", "king", "lamp", "moon", "night", "orange",
    "pen", "quilt", "rain", "star", "table", "user", "voice", "water", "xenon", "yarn",
    "ant", "book", "cake", "dove", "eagle", "flame", "ghost", "honey", "ink", "jelly",
    "key", "lion", "mango", "note", "owl", "pear", "quiz", "rose", "song", "tiger",
    "unicorn", "vase", "wand", "yarn", "zinc", "bridge", "chair", "dance", "earth", "fire",
    "glass", "heart", "image", "joy", "knife"
]

def life():
    """Guess the word"""
    random_number = randint(0, 99)
    word = words[random_number]
    print("Here's the hint!")
    print("_"*len(word))


print("Welcome to my game!")

life()