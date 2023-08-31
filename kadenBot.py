import discord
from discord.ext import commands
import random
from googletrans import Translator

translator = Translator()

react_nigga = [
    'what color r u', 'what is your skin color', 'are you black',
    'what color are you', 'what color r you', 'what color are u',
    'r u black', 'r u white or black',
    'are you white or black','are u white or black',
]
lie = [
    'I know you arent','i know ur white','u r white','you are white','you r white','no you arent'
    'you are not. unlive',
]
agreed = [
    'so you are racist', 'so you cant say nword', 'so you cant say n-word',
    'so why are you racist', 'why r u racist then', 'u cant say nword if you are white',
    'only black people can say nword',
]
im_black = [
    'yes i am','yes','i am',
]
im_racist = [
    'bro im black', 'im not even white', 'i can because im black',
    'im black guys', 'you are lying',
]
age_ask = [
    'old enough', 'stop asking me this question', '13','im 13','old enough','stop','kys','kys'
]
no = [
    'no','no','no','no','definitely no',
]
yes = [
    'yes'
]
are_you_real = [
    'no', 'yes', 'how do you think', 'whats wrong with you'
]
yo_mamma = [
    'Yo momma is so fat when she got on the scale it said, "I need your weight not your phone number."','Yo momma is so fat, I took a picture of her last Christmas and its still printing.',
    'Yo momma is so fat that when she went to the beach a whale swam up and sang, "We are family, even though youre fatter than me."','Yo mamma is so ugly when she tried to join an ugly contest they said, "Sorry, no professionals."',
    'Yo momma is so fat and old when God said, "Let there be light," he asked your mother to move out of the way.', 'Yo momma is so fat, that when she fell, no one was laughing but the ground was cracking up.',
    'Yo momma is so fat when she sat on WalMart, she lowered the prices.', 'Yo momma is so fat that Dora cant even explore her','Yo momma is so stupid when an intruder broke into her house, she ran downstairs, dialed 9-1-1 on the microwave, and couldnt find the "CALL" button.',
    'Your momma is so ugly she made One Direction go another direction.','Yo momma is so fat her bellybutton gets home 15 minutes before she does.',
    'Yo momma is so stupid, she put two quarters in her ears and thought she was listening to 50 Cent.'
]
didnt_ask = [
    'uhm according to wikipedia they didnt ask', 'cool but nobody asked', '/poll who asked','/poll question:who asked  choices:nobody, nobody'
]
unfunny = [
    'because you are not funny','you think you are funny','cuz its not funny','because it is not funny'
]
kaden_hot = [
    'I totally agree with you','person above me is right :arrow_up:','true :arrow_up:','thats right'
]
shut_up = [
    'unlive pls','kys','kys please','kill yourself please','unlive please'
]
sleep_well = [
    'nobody cares shut up', 'sleep well'
]
go_sleep_then = [
    'go sleep then'
]
because = [
    'because'
]
say_nword = [
    'unlive pls','kys','kys please','kill yourself please','unlive please','unlive pls','kys','kys please','kill yourself please','unlive please','nigger'
]
echo_trigger = [
    'can you fucking learn, its "!" not "/"', 'ITS "!" LEARN IT','not this symbol buddy', 'caught in 4k',
]
fuck_me = [
    'fuck you'
]
suck_my_dick = [
    'im not going to do that','unlive','kys pls','stop','its not funny'
]
answer_me = [
    'no lol'
]
idc = [
    'i dont really care','i dont care','i dont care at all','honestly, i dont care'
]
what_makes_you = [
    'i just know it'
]
egirl_sim = [
    'yes im level 100','yes','i like it'
]
sorry = [
    'sorry','I will stop','my bad','sorry'
]
who_made_you = [
    'im not ai, im just discord bot created by <@709391280807084115>\nI have also commands only aurora knows about'
]
do_me_favor = [
    'just do me a favor and jump off the building','just do me a favor','killing yourself is fun trust me','because your life is worth less than amount of my subscribers'
]
know_me = [
    'no clue','no','no clue who are you','no but i know your mom'
]
address = [
    '69 walter white street mexico','i cant remember',"im hiding from aurora in fogi's garage","im hiding from aurora in fogi's garage"
]
face = [
    'this is me\nhttps://media.discordapp.net/attachments/1145178441461796998/1146435048241897552/kaden_face.jpg?width=1003&height=663'
]
vacc = [
    'idk tbh'
]
aurora = [
    'aurora made me pregnant'
]


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

responses = {
     "nigger": react_nigga,
     "nigga": react_nigga,
    "<@1145831769829032067> im white": agreed,
    "<@1145831769829032067>im white": agreed,
    "<@1145831769829032067> i am white": agreed,
    "<@1145831769829032067> i'm white": agreed,
    "<@1145831769829032067>i'm white": agreed,
    "<@1145831769829032067>i am white": agreed,
    "<@1145831769829032067>white": agreed,
    "<@1145831769829032067> white": agreed,
    
    
    "<@1145831769829032067> im black": lie,
    "<@1145831769829032067>im black": lie,
    "<@1145831769829032067>black": lie,
    "<@1145831769829032067> black": lie,
    "<@1145831769829032067> i am black": lie,
    "<@1145831769829032067>i am black": lie,
    "<@1145831769829032067>i'm black": lie,
    "<@1145831769829032067> i'm black": lie,

    "<@1145831769829032067>are you black": im_black,
    "<@1145831769829032067> are you black": im_black,
    "<@1145831769829032067>r u black": im_black,
    "<@1145831769829032067> r u black": im_black,
    "<@1145831769829032067>are u black": im_black,
    "<@1145831769829032067> are u black": im_black,
    "<@1145831769829032067> you are black": im_black,
    "<@1145831769829032067> are you nigger": im_black,
    "<@1145831769829032067> u r black": im_racist,
    "<@1145831769829032067> u black": im_black,
    "<@1145831769829032067> you are black": im_black,
    "<@1145831769829032067> you are nigger": im_black,
    "<@1145831769829032067> is black": im_black,
    "<@1145831769829032067> is nigger": im_black,
    "<@1145831769829032067> is nigga": im_black,
    
    "<@1145831769829032067> is aurora hot": yes,
    "<@1145831769829032067> aurora is hot": yes,
    "<@1145831769829032067> do you think is aurora hot": yes,
    "<@1145831769829032067> am i hot": yes,
    "<@1145831769829032067> do you think aurora is hot": yes,
    

    "<@1145831769829032067> are you hot": yes,
    "<@1145831769829032067> is kaden hot": yes,
    
    "<@1145831769829032067> shut up": shut_up,
    
    
    "<@1145831769829032067>are you white": im_racist,
    "<@1145831769829032067>r u white": im_racist,
    "<@1145831769829032067>are u white": im_racist,
    "<@1145831769829032067>r you white": im_racist,
    "<@1145831769829032067>you are white": im_racist,
    "<@1145831769829032067> is white": im_racist,
    "<@1145831769829032067>is white": im_racist,
    "<@1145831769829032067> is racist": im_racist,
    "<@1145831769829032067> are you racist": im_racist,
    "<@1145831769829032067> why r u racist": im_racist,
    "<@1145831769829032067> why are u racist": im_racist,
    "<@1145831769829032067> why are you racist": im_racist,
    "<@1145831769829032067> r u racist": im_racist,

    "<@1145831769829032067> how old are you": age_ask,
    "<@1145831769829032067> how old r u": age_ask,
    "<@1145831769829032067> how old are u": age_ask,
    "<@1145831769829032067> how old r you": age_ask,
    
    "<@1145831769829032067> r u 11": no,
    "<@1145831769829032067> are you 11": no,
    "<@1145831769829032067> r you 11": no,
    "<@1145831769829032067> are u 11": no,
    "<@1145831769829032067> you are 11": shut_up,
    "<@1145831769829032067> you are eleven": shut_up,
    "<@1145831769829032067> u r 11": no,
    "<@1145831769829032067> u are 11": no,
    "<@1145831769829032067> you r 11": shut_up,
    "<@1145831769829032067> you are like 11": shut_up,
    "<@1145831769829032067> you r like 11": shut_up,
    "<@1145831769829032067> u r like 11": shut_up,
    "<@1145831769829032067> u are like 11": shut_up,
    "<@1145831769829032067> bro you are like 11": shut_up,
    "<@1145831769829032067> man you are like 11": shut_up,
    "<@1145831769829032067> no you are 11": shut_up,
    "<@1145831769829032067> no u are 11": shut_up,
    "<@1145831769829032067> no you r like 11": shut_up,
    "<@1145831769829032067> cool but i didnt ask": shut_up,
    "<@1145831769829032067> who ask": shut_up,
    "<@1145831769829032067> i didnt ask": shut_up,
    "<@1145831769829032067> nobody ask": shut_up,
    "<@1145831769829032067> cool but i didnt ask": shut_up,
    
    
    "<@1145831769829032067> are you eleven": no,
    "<@1145831769829032067> r u eleven": no,
    "<@1145831769829032067> yes you are": no,
    "<@1145831769829032067> yes u r": no,
    "<@1145831769829032067> stop lying": no,
    "<@1145831769829032067> dont lie": no,
    "<@1145831769829032067> you are lying": no,
    "<@1145831769829032067> u r lying": no,
    "<@1145831769829032067> is kaden retarded": yes,
    "<@1145831769829032067> are you retarded": yes,
    "<@1145831769829032067> r u retarded": yes,
    "<@1145831769829032067> are u retarded": yes,
    
    "<@1145831769829032067> why": unfunny,
    
    "<@1145831769829032067> is hot": kaden_hot,
    "<@1145831769829032067> you are hot": kaden_hot,
    "<@1145831769829032067> u r hot": kaden_hot,
    
    "kaden is hot": kaden_hot,
    

    "<@1145831769829032067> kys": yo_mamma,
    "<@1145831769829032067> nobody loves you": yo_mamma,
    

    "<@1145831769829032067> should I kys": yes,
    "<@1145831769829032067> should I kill myself": yes,
    "<@1145831769829032067> should I die": yes,
    "<@1145831769829032067> do you hate me": yes,
    "<@1145831769829032067> do u hate me": yes,

    "<@1145831769829032067> do u like me": no,
    "<@1145831769829032067> do you like me": no,
    
    
    "<@1145831769829032067> do u know vacc": vacc,
    "<@1145831769829032067> do you know vacc": vacc,
    "<@1145831769829032067> who is vacc": vacc,
    

    "<@1145831769829032067> not funny": didnt_ask,
    "<@1145831769829032067> its not funny": didnt_ask,
    "<@1145831769829032067> it's not funny": didnt_ask,
    "<@1145831769829032067> unfunny": didnt_ask,
    "<@1145831769829032067> this isnt funny": didnt_ask,
    "<@1145831769829032067> this wasnt funny": didnt_ask,
    "<@1145831769829032067> that wasnt funny": didnt_ask,
    "<@1145831769829032067> that was not funny": didnt_ask,
    "<@1145831769829032067> this was not funny": didnt_ask,
    "<@1145831769829032067> this is not funny": didnt_ask,
    "<@1145831769829032067> this wasn't funny": didnt_ask,
    "<@1145831769829032067> you are not funny": didnt_ask,
    "<@1145831769829032067> you aren't funny": didnt_ask,
    "<@1145831769829032067> you are cringe": didnt_ask,
    "<@1145831769829032067> you are unfunny": didnt_ask,
    
    "<@1145831769829032067> im tired": go_sleep_then,
    "<@1145831769829032067> ima sleep": sleep_well,
    "<@1145831769829032067> ima go sleep": sleep_well,
    "<@1145831769829032067> im gonna sleep": sleep_well,
    "<@1145831769829032067> im gonna go sleep": sleep_well,
    "<@1145831769829032067> i will sleep": sleep_well,
    "<@1145831769829032067> i will go sleep": sleep_well,

    "im tired": go_sleep_then,
    "ima sleep": sleep_well,
    "ima go sleep": sleep_well,
    "im gonna sleep": sleep_well,
    "im gonna go sleep": sleep_well,
    "i will sleep": sleep_well,
    "i will go sleep": sleep_well,

    '<@1145831769829032067> you just said i should go sleep': no,
    '<@1145831769829032067> you said i should go sleep': no,
    '<@1145831769829032067> why did you say I should go sleep': because,
    
    '<@1145831769829032067> say nigger': say_nword,
    '<@1145831769829032067> say nigga': say_nword,
    '<@1145831769829032067> say nword': say_nword,
    
    '/echo': echo_trigger,

    'fuck me': fuck_me,

    '<@1145831769829032067> suck my dick': suck_my_dick,
    '<@1145831769829032067> can you suck my dick': suck_my_dick,
    
    '<@1145831769829032067> answer me': answer_me,
    
    '<@1145831769829032067> im gonna ban you': idc,
    '<@1145831769829032067> because im gonna ban you': idc,
    '<@1145831769829032067> I will ban you': idc,
    '<@1145831769829032067> because I will ban you': idc,
    '<@1145831769829032067> im going to ban you': idc,

    '<@1145831769829032067> what makes you think im not funny': what_makes_you,
    '<@1145831769829032067> what makes you think im unfunny': what_makes_you,
    '<@1145831769829032067> why do you think im not funny': what_makes_you,
    '<@1145831769829032067> why do you think im unfunny': what_makes_you,
    '<@1145831769829032067> why you say im not funny': what_makes_you,
    '<@1145831769829032067> why did you say im not funny': what_makes_you,
    '<@1145831769829032067> why you said im not funny': what_makes_you,
    '<@1145831769829032067> why you say im unfunny': what_makes_you,
    '<@1145831769829032067> why did you say im unfunny': what_makes_you,
    '<@1145831769829032067> why you said im unfunny': what_makes_you,
    
    'e-girl simulator': egirl_sim,
    'egirl simulator': egirl_sim,
    
    'dont ping me nigger': sorry,
    'dont ping me nigga': sorry,
    'stop pinging me nigga': sorry,
    'stop pinging me nigger': sorry,
    
    '<@1145831769829032067> do you know aurora': aurora,
    '<@1145831769829032067> do you know danny': aurora,
    '<@1145831769829032067> do u know aurora': aurora,
    '<@1145831769829032067> do u know danny': aurora,
    '<@1145831769829032067> who is aurora': aurora,
    '<@1145831769829032067> who is danny': aurora,
    
    
    
    '<@1145831769829032067> who made you': who_made_you,
    '<@1145831769829032067> who is your creator': who_made_you,
    '<@1145831769829032067> are you ai': who_made_you,
    
    '<@1145831769829032067> why would I kill myself': do_me_favor,
    '<@1145831769829032067> why should I kill myself': do_me_favor,
    '<@1145831769829032067> why do you want me to die': do_me_favor,
    '<@1145831769829032067> why do you want me to kill myself': do_me_favor,
    
    '<@1145831769829032067> do you know me': know_me,
    '<@1145831769829032067> do you know who I am': know_me,
    '<@1145831769829032067> who am I': know_me,
    
    '<@1145831769829032067> where do you live': address,
    '<@1145831769829032067> what is your addres': address,
    '<@1145831769829032067> give me your addres': address,
    
    '<@1145831769829032067> show face': face,
    '<@1145831769829032067> can you do face reveal': face,
    '<@1145831769829032067> show your face': face,
    '<@1145831769829032067> do face': face,
    '<@1145831769829032067> show me your face': face,
    '<@1145831769829032067> show your nudes': face,
    '<@1145831769829032067> show me your nude': face,
    '<@1145831769829032067> show nude': face,
    '<@1145831769829032067> send nude': face,
    '<@1145831769829032067> show some nude': face,
    '<@1145831769829032067> send me nude': face,
    '<@1145831769829032067> send me your nude': face,
    
    '<@1145831769829032067> show us your face': face,
    '<@1145831769829032067> show us face': face,
    
    '<@1145831769829032067> I said nudes': no,
    '<@1145831769829032067> I said show nudes': no,
    '<@1145831769829032067> nudes': no,
    
    
}

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="E-Girl Simulator 2"))
    print(f'Logged in as {bot.user.name}')

    if random.random() < 0.3:
        general_channel = bot.get_channel(1117766297405624382)
        if general_channel:
            await general_channel.send("<@1141262611749548093> hi")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()


    for keyword, response_list in responses.items():
        if ('nigger' in content or 'nigga' in content) and message.author.id == 1141262611749548093 or 709391280807084115:
            increment_counter()
            return
        if keyword in content:
            response = random.choice(response_list)
            if response:
                await message.channel.send(response)

    await bot.process_commands(message)

def increment_counter():
    try:
        with open('counter.txt', 'r') as file:
            counter = int(file.read())
        counter += 1
        with open('counter.txt', 'w') as file:
            file.write(str(counter))
    except Exception as e:
        print(f"An error occurred while incrementing counter: {e}")


@bot.command()
async def echo(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

@bot.command()
async def Echo(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

@bot.command()
async def ECHO(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

@bot.command()
async def dick(ctx, *, text):
    await ctx.send(text)

@bot.command()
async def secret(ctx):
    if ctx.author.id == 709391280807084115:
        await ctx.send('https://cdn.discordapp.com/attachments/1146426822716821515/1146446534368579705/image.png')
    else:
        await ctx.send('secret :)')

@bot.command()
async def Secret(ctx):
    if ctx.author.id == 709391280807084115:
        await ctx.send('https://cdn.discordapp.com/attachments/1146426822716821515/1146446534368579705/image.png')
    else:
        await ctx.send('secret :)')


whitelist = [
    1141262611749548093,
    1137691297658974209,
    1117340703828234321,    
]

kaden_length = random.randint(2, 6)

@bot.command()
async def size(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send(f'my penis is {kaden_length}cm long')
    
    elif user.id in whitelist:
        await ctx.send("bro she's a girl")
    
    elif user.id == 709391280807084115:
        await ctx.send("<@709391280807084115>'s dick is 21cm long")
    elif user.id == 874296123173507123:
        await ctx.send("<@874296123173507123>'s dick is -3cm long :joy:")
    elif user.id == 1145831769829032067:
        await ctx.send(f'my dick is {kaden_length}cm long  :tiny:')
    else:
        length = random.randint(1, 20)
        await ctx.send(f"{user.mention}'s dick is {length}cm long :scream:")

@bot.command()
async def Size(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send(f'my penis is {kaden_length}cm long')
    elif user.id in whitelist:
        await ctx.send("bro she's a girl")
    
    elif user.id == 709391280807084115:
        await ctx.send("<@709391280807084115>'s dick is 21cm long")
    elif user.id == 874296123173507123:
        await ctx.send("<@874296123173507123>'s dick is -3cm long :joy:")
    elif user.id == 1145831769829032067:
        await ctx.send(f'my dick is {kaden_length}cm long  :tiny:')
    else:
        length = random.randint(1, 20)
        await ctx.send(f"{user.mention}'s dick is {length}cm long :scream:")

@bot.command()
async def auroracounter(ctx):
    try:
        with open('counter.txt', 'r') as file:
            counter = int(file.read())
        result = counter
        if result == 0:
            await ctx.send(f'Aurora didnt say any nword! lets celebrate! :partying_face:')
        elif result == 1:
            await ctx.send(f'Aurora said nword only 1 time. good job :)')
        else:
            await ctx.send(f'Aurora said nword {int(result)} times since im here.')
    except Exception as e:
        await ctx.send(f'An error happened while trying to get value int from counter.txt. please ask <@709391280807084115> to fix his code.')

@bot.command()
async def auroracounter_reset(ctx):
    try:
        with open('counter.txt', 'w') as file:
            file.write("0")
            await ctx.send('*Counter successfully resetted*')
        await ctx.message.delete()
    except Exception as e:
        await ctx.send(f'An error happened while trying to reset counter')

quotes_file = 'quotes.txt'

def load_quotes():
    try:
        with open(quotes_file, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_quotes(quotes):
    with open(quotes_file, 'w') as file:
        file.write('\n'.join(quotes))

quotes = load_quotes()

@bot.command()
async def quote(ctx, *, new_quote=None):
    if new_quote:
        quotes.append(new_quote)
        save_quotes(quotes)
        await ctx.send(f'"{new_quote}" has been added! write !quote_list to see full list of quotes')
    else:
        if quotes:
            random_quote = random.choice(quotes)
            await ctx.send(f'*{random_quote}*')
        else:
            await ctx.send('No available quotes.')

@bot.command()
async def quote_list(ctx):
    if ctx.guild is None:
        user_quotes = '\n'.join(quotes)
        await ctx.author.send(f'here is the full list of quotes:\n```{user_quotes}```')
    else:
        await ctx.send('Command !quote_list works only in dms.')

@bot.command()
async def translate(ctx, *, text):
    try:
        translation = translator.translate(text, src='pl', dest='en')
        translated_text = translation.text
        await ctx.send(f'||Translated to english:||\n{translated_text}')
    except:
        await ctx.send('An error occurred while translating. ask <@874296123173507123> to fix api key.')

@bot.command()
async def features(ctx):
    await ctx.send("## Here's full list of features so fogi won't forget\n* `!translate (text)` - translates text from polish to english\n* `!features` - you are reading this\n* `!quote (text)` - adds quote to list, write only !quote to send random quote already added\n* `!quote_list` - works only in dms with bot. shows full list of quotes added\n* `!auroracounter` - counter that tracks how many times aurora said n-word\n* `!size (user)` - mention someone in (user), or leave blank to ask bot about his penis size\n* `!secret` - command available only for fogi. contains screenshot out of context\n\nsource code:\nhttps://github.com/FogiPL/kadenBot")


bot.run('TOKEN')
