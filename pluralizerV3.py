irregular = {"child": "children",
             "bus": "buses",
             "shrimp": "shrimp",
             "fish": "fish",
             "mouse": "mice",
             "man": "men",
             "woman": "women",
             "deer": "deer",
             "species": "species",
             "person": "people",
             "knife": "knives",
             "sheep": "sheep",
             "ox": "oxen",
             "moose": "moose",
             "virus": "viruses",
             "giraffe": "giraffes",
             "chief": "chiefs",
             "roof": "roofs",
             "cuff": "cuffs",
             "photo": "photos",
             "piano": "pianos",
             "manatee": "manatees",
             "human": "humans",
             "goose": "geese",
             "tooth": "teeth",
             "mantis": "mantises",
             "reef": "reefs",
             "die": "dice",
             "index": "indeces",
             "chef": "chefs",
             "soprano": "sopranos",
             "cello": "cellos",
             "dynamo": "dynamos",
             "kilo": "kilos",
             "auto": "autos",
             "avocado": "avocados",
             "video": "videos",
             "studio": "studios",
             "concerto": "concertos",
             "radio": "radios",
             "quiz": "quizzes",
             "trout": "trout",
             "salmon": "salmon",
             "series": "series",
             "cod": "cod",
             "pro": "pros",
             "rice": "rice",
             "louse": "lice", # Offtopic who knew this?? The animal that eats your dandruff isnt a lice its a god damn louse??
             "banana": "bananas",
             "drama": "dramas",
             "umbrella": "umbrellas",
             "zebra": "zebras",
             "iron": "irons",
             "spoon": "spoons",
             "drum": "drums",
             "wagon": "wagons"}

us_to_i = {
    "alumnus",    # alumni
    "bacillus",   # bacilli
    "cactus",     # cacti
    "focus",      # foci
    "fungus",     # fungi
    "locus",      # loci
    "nucleus",    # nuclei
    "radius",     # radii
    "stimulus",   # stimuli
    "syllabus",   # syllabi
    "terminus",   # termini
    "uterus",     # uteri
    "octopus",     # octopi (octopuses is also valid but come on i dont need more special cases man)
    "apparatus"
}
vowels = {"a", "e", "i", "o", "u"}
consonants = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"}

def makepl(word):
    word = word.lower()  
    plural = word + "s"
    
    if word in irregular:  
        plural = irregular[word]
    elif word.endswith(("oo", "ff")):
        plural = word + "s"
    elif word in us_to_i:
        plural = word[:-2] + "i"
    elif word.endswith("y") and word[-2] in consonants:
        plural = word[:-1] + "ies"
    elif word.endswith("is"):
        plural = word[:-2] + "es"
    elif word.endswith(("ix", "ex")):
        plural = word[:-2] +"ices"
    elif word.endswith(("sh","o","ch", "x", "z")):
        plural = word + "es"
    elif word.endswith("fe"):
        plural = word[:-2] + "ves"
    elif word.endswith("f"):
        plural = word[:-1] + "ves"
    elif word.endswith("a"):
        plural = word + "e"
    elif word.endswith("s"):
        plural = word + "es"
    elif "woman" in word:
        plural = word.replace("woman", "women")
    elif "man" in word:
        plural = word.replace("man", "men")
    elif word.endswith(("um", "on")):
        plural = word[:-2] + "a"
    return plural
             
print("   ▄███████▄  ▄█       ███    █▄     ▄████████    ▄████████  ▄█        ▄█   ▄███████▄     ▄████████    ▄████████ ")
print("  ███    ███ ███       ███    ███   ███    ███   ███    ███ ███       ███  ██▀     ▄██   ███    ███   ███    ███ ")
print("  ███    ███ ███       ███    ███   ███    ███   ███    ███ ███       ███▌       ▄███▀   ███    █▀    ███    ███ ")
print("  ███    ███ ███       ███    ███  ▄███▄▄▄▄██▀   ███    ███ ███       ███▌  ▀█▀▄███▀▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀ ")
print("▀█████████▀  ███       ███    ███ ▀▀███▀▀▀▀▀   ▀███████████ ███       ███▌   ▄███▀   ▀ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ")
print("  ███        ███       ███    ███ ▀███████████   ███    ███ ███       ███  ▄███▀         ███    █▄  ▀███████████ ")
print("  ███        ███▌    ▄ ███    ███   ███    ███   ███    ███ ███▌    ▄ ███  ███▄     ▄█   ███    ███   ███    ███ ")
print(" ▄████▀      █████▄▄██ ████████▀    ███    ███   ███    █▀  █████▄▄██ █▀    ▀████████▀   ██████████   ███    ███ ")
print("             ▀                      ███    ███              ▀                                         ███    ███ ")
print(" ")

while True:
    print("Use singular form..")
    wish = input("Please enter the word(s) you wish to pluralize: ").split()
    
    if wish and wish[0].lower() == "quit":
        break
    
    plural_form = [makepl(word) for word in wish]
    print("Pluralized word(s):", " ".join(plural_form))
    print(" ")