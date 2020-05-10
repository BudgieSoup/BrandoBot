import discord
import numpy as np
import random
import os

client = discord.Client()

this_folder = os.path.dirname(os.path.abspath(__file__))
brando_txt = os.path.join(this_folder, 'brando.txt')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!jeff'):
        await message.channel.send('my nama jeff')

    elif message.content.startswith('!brando'):
        e = random.randint(1, 101)
        if e <= 20:
            await message.channel.send(brando_chain())
        elif e <= 50:
            await message.channel.send(brando_chain() + brando_chain() + brando_chain() + brando_chain() + brando_chain() + '\n\n' + brando_chain() + brando_chain() + brando_chain() + brando_chain() + brando_chain() + brando_chain())
        elif e <= 70:
            await message.channel.send(brando_chain() + '\n\n' + brando_chain() + brando_chain() + '\n\n' + brando_chain() + brando_chain() + brando_chain() + '\n\n' + brando_chain() + '\n\n' + brando_chain())
        else:
            await message.channel.send(brando_chain() + brando_chain() + brando_chain() + '\n\n' + brando_chain() + '\n\n' + brando_chain() + brando_chain() + brando_chain() + brando_chain() + brando_chain() + brando_chain())

    elif message.content.startswith('!wheel'):
        await message.channel.send('The TLI subject of the hour is: ' + wheel())

    elif message.content.startswith('!clown'):
        await message.channel.send('https://www.youtube.com/watch?v=zjedLeVGcfE')

    else:
         return

def wheel():
    subjects = ['twitter retards', 'Morrowind', 'transgenderism', 'covid-19', 'inceldom', 'gachashit', 'MOBAs', 'anime', 'mango', 'hating women', 'hating blacks', 'hating jews', 'drumpf', 'e-drama', 'the latest krappost', 'vidya', 'balkan music', 'an epic BPD_GOD tweet', 'hornyposting', 'cooking', 'some nerd shit involving history or politics or something', 'sissy hypno', 'bullying kaasci', 'paradox games', 'funny and epic balkan countries', 'blogposting']

    num_items = len(subjects)

    rand_num = random.randint(0, num_items -1)

    return subjects[rand_num]

def brando_chain():
    brando = open(brando_txt).read()

    corpus = brando.split()

    def make_pairs(corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])

    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(corpus)

    chain = [first_word]

    n_words = random.randint(10, 20)

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    s = ' '

    s = s.join(chain)

    return s

client.run('')
