# LoL Draft Screen Tool
 Broadcast tool to help show teams during spectate delay because according to riot games that's not a thing people actually want grumble grumble
 
 Also fair warning that I only spent a couple hours on this for personal gratification; it's very much function over form, and even then it might not function.
 
# Installation

You'll need Python 3, with the wxpython, glob and shutil libraries. I made and ran this with Python 3.8; earlier versions _should_ work, but your mileage may vary. Download the entire thing and run main.py and hope for the best.

# Usage

![Image](https://imgur.com/o2hPiGj.png)

As you would expect, the team and player names are just text boxes, and the dropdown menus are just a big list of champ names. Pressing UPDATE will then update the files in /output, which you can then put into your favourite copy of OBS Studio. Players are numbered in descending order (e.g. b3champ.png is the image for the third player down's champion).

For bo3/bo5 sets, CLEAR CHAMPS sets all champs and bans to the first value which, by default, is !BLANK. SWAP SIDES will swap the team and player names (not champions) between red and blue. CLEAR ALL resets all champions and also wipes all text boxes. Remember, you will need to press UPDATE after doing any of these in order to push the changes.

# Modification

I heartlessly ripped a bunch of images from one of Riot's websites, but if you have more appropriately sized ones for your broadcast (or, more likely, an update comes out and I haven't updated this tool), the tool will happily accept any .png file in /input. Make sure the file name is the same as the champ name for your own sake. Also, make sure you have one image named !BLANK or equivalent, else the tool will reset to the first champion alphabetically.