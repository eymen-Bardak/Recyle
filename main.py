import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

memes = [
    "https://i.imgflip.com/9wygff.jpg",
    "https://i.imgflip.com/9wyici.jpg",
    "https://i.imgflip.com/9wyixu.jpg"  # 3. meme eklendi
]

@bot.command()
async def meme(ctx):
    random_meme = random.choice(memes)
    await ctx.send(random_meme)

ayrisma_sureleri = {
    "plastik": "450 yıl",
    "cam şişe": "400 yıl",
    "karton kutu": "350 yıl",
    "metal kutu": "500 yıl",
    "pvc kutu": "300 yıl",
    "tek kullanımlık çatal": "400 yıl",
    "tek kullanımlık tabak": "400 yıl",
    "muz kabuğu": "2 hafta",
    "elma kabuğu": "2 ay",
    "portakal kabuğu": "6 ay",
    "yumurta kabuğu": "1 yıl",
}

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} olarak giriş yaptı!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Botun kendi mesajlarını görmezden gelmesini sağlıyoruz.

    esya = message.content.lower()  # Kullanıcının yazdığı mesajı alıp küçük harfe çeviriyoruz.

    if esya in ayrisma_sureleri:
        await message.channel.send(f"♻ *{esya}* geri dönüşüm süresi: *{ayrisma_sureleri[esya]}*")
    
    await bot.process_commands(message)  # Diğer komutların çalışabilmesi için bu satırı ekliyoruz.

# Botunu başlat
bot.run("TOKEN")
