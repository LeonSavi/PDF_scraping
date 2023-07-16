from pathlib import Path
import os
from PyPDF2 import PdfReader

# =====================================================================================

# get directories of PDFs and output folder
def directories():

    main_folder = Path(__file__).parent
    pdf_folder = main_folder / "PDFs"
    output_folder = main_folder / "outputs"

    return pdf_folder, output_folder

# Get dictionary of the books/pdf: {name_of_the_book.pdf:Path_of_the_book}
def pdf_dict_path(pdf_folder):

    pdf_list = [file for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

    pdf_path = [pdf_folder/pdf for pdf in pdf_list ]

    return {x:y for x,y in zip(pdf_list,pdf_path)}

# extract text on introduction,guide etc etc 
def get_intro(dict_pdf):
    pass

# create a df with the following columns: 
# index, text, events, objects to pick, dict {action:index}, connected image, 
# create a set of rules for mining the words from the book (see below)
# eg. first sentece is always removed, if the page has only one sentence -> skip
# to simplify: 
# 1- create an iterable for each page already polished from the first sentence with only 'story'
# 2- each paragraph should finish with a numer+. e.g ''turn to 16.'' 
# if not: check next page, if starts with a number you are dead
# probably more functions are needed
# 3- there exist footnotes those should be included in the text in parenthesis
# 4- 'Illustration VII' should be flagged

def read_story(book_title, book_path):

    reader = PdfReader(book_path)

    for page_idx in range(len(reader.pages)):
        pass

# =====================================================================================

def main():

    pdf_folder, output_folder = directories()
    dict_pdf = pdf_dict_path(pdf_folder)

    for ttl, pth in dict_pdf.items():
        read_story(ttl,pth)






if __name__ == "__main__":
    main()

# examples
'''
33 Joe Dever and Gary Chalk
5
After about an hour of walking, the track slowly bears round to the
east. You reach a shallow ford where a fast-ﬂowing brook runs on
a steep rocky course towards the south. Just beyond the ford is
a junction where the track meets a wider path running north to
south. Realizing that the north path will take you away from the
capital, you turn right at the junction and head south.
Turn to 111 .
6
In the distance you can hear the sound of horses galloping nearer.
You crouch behind a tree and wait as the riders come closer. They
are the cavalry of the King’s Guard wearing the white uniforms of
His Majesty’s army.
If you wish to call them, turn to 183 .
If you wish to let them pass and then continue on your way
through the forest, turn to 200 .

'''
   ######### print(reader.pages[61].extract_text())
   ######### print(reader.pages[62].extract_text())
   ######### print(reader.pages[63].extract_text())
'''
Flight from the Dark 62
62
The ‘soldiers’ lie dead at your feet. They were bandits who were
stealing from the refugees of Toran, and from the abandoned
houses and farms in the area.
Searching their bodies you ﬁnd 28 Gold Crowns and two Back-
packs containing enough food for 3 Meals. They had been armed
with a crossbow and three Swords. The crossbow has been dam-
aged in the ﬁght, but the Swords are untouched and you may
keep one if you wish.
You adjust your equipment, give a cautious glance towards the
west and continue your run towards the outer defences of the
capital.
Turn to 288 .
63
Illustration VI
The wild old man is screaming at you. He blames you for the war
and curses the Kai Lords as agents of the Darklords. He will not
listen to reason and you must ﬁght him.
Madman: C OMBAT SKILL 11 E NDURANCE 10
If you win, turn to 269 .
64
You are awoken by the cries of a Kraan circling above the caravan.
It is early morning and the sky is clear and bright. You can see a
pack of Doomwolves less than a quarter of a mile away along
the highway ahead. They are preparing to attack. You must act
quickly.
'''
'''The wild old man is screaming at you. '''
'''
Flight from the Dark 64
If you decide to gather your equipment and run for the cover
of the trees, turn to 188 .
If you decide to cut free one of the horses and try to break
through the attacking Doomwolves to the clear road be-
yond, then turn to 16 .
65
Your senses scream at you that this place is very evil. Leave as
quickly as you can.
Turn to 104 .
66
Startled, you turn around to see a burly sergeant and two soldiers
running towards you, their swords drawn as if to strike.
You prepare to defend yourself for it looks as if they are about
to attack ﬁrst and ask questions later; but suddenly the sergeant
calls his men to a halt. He has recognized your cloak. They put
away their weapons and apologize many times for their mistake.
The sergeant orders one of the men to fetch the captain of the
Guard as he leads you to the doors of the Great Hall.
You are greeted by a tall and handsome warrior who listens
intently to your story. When you have ﬁnished the account of
your perilous journey to the capital, you notice a tear in the brave
man’s eye as he bids you to follow him. You walk through the
splendid halls and corridors of the inner Palace. The richness and
grandeur are a wonder to behold. You eventually arrive at a large
carved door, guarded by two soldiers wearing silver armour.
You are about to meet the King.
Turn to 350 . '''
