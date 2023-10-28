import os
import re
import datetime

from anki.collection import Collection 
from anki.decks import DeckDict
from anki.notes import NoteId

# Find the Anki directory 
anki_home = '/home/inter/Dev/article-painter/src/AnkiTest/User 1'
anki_collection_path = os.path.join(anki_home, "collection.anki2")

# 1. Load the anki collection 
col = Collection(anki_collection_path)

# 2. Select the deck 

# Find the model to use (Basic, Basic with reversed, ...)
modelBasic = col.models.by_name('Basic')
if modelBasic is None:
    exit(1)
# Set the deck
dicks = col.decks.all()
for d in dicks:
    print(d['name'])
deck: DeckDict | None = col.decks.by_name('xd')
if deck is None:
    print('errrrro')
    exit(1)

col.decks.select(deck['id'])
ids = col.find_notes('deck:Deutsch')
# print(ids)
for id in ids:
    # print(f'Card id: {id}')
    # print('question:')
    # print(col.get_card(id).question())
    # print('answer:')
    print(id)
    x = col.get_note(id).items()
    print(x)

col.decks.current()['mid'] = modelBasic['id']
print(col.decks.current())

# 3. Create a new card 
to_rm = col.find_notes('xd')
print('to rm ===')
print(to_rm)
print('========')
n = col.get_note(to_rm[0])
n.fields[0] += 'xd'
n.flush()
print(n.fields)

note = col.new_note(modelBasic)
note.fields[0] = f'generated on {datetime.datetime.now()}' # The Front input field in the UI
note.fields[1] = "mom"   # The Back input field in the UI
col.add_note(note, deck['id'])

# 4. Save changes 
col.save()
