Development began: 2025.02.21

2025.02.22 8:30 AM current model is about 82% accurate. (123 total points out of 150) benchmarked by three different 50 point tests (Deepseek R1, Claude 3.5, ChatGPT 4o)

I will go set up a few tweaks right now and I will report back on accuracy soon.

2025.02.22 9:42 AM 

PluralizerV2 now effectively handles most english words. (294 out of 300 points total) benchmarked by three AI Models,
Deepseek R1 ChatGPT 4o and Claude 3.5 Sonnet respectively. PluralizerV2 scored 98% on all three tests.
note: some words were repeated, to make a more accurate assesment I'll make one soon.

2025.02.22 11:00

Removed unnecessary irregulars : book, door, datum

These were necessary when I had a rule that turned "oo" into "ee" in a word
However, this seemed to backfire most of the time as you can guess
ex. Moose -> Meese

The way the program pluralizes words are by set rules, depending on the end of the word then adding the appropiate suffix

However, english has a lot of exceptions, and any 'outliers' get placed inside the irregular category
For better readability, some words, such as ones that are of latin origin and go from -us to -i are also listed in a seperate category
This is due to a bug I just couldn't fix
"Bus" kept turning into "Bi"