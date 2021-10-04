from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url"
    helptxt = f"**What's the song you want?**\nUsage`/song <song name>`"
    await message.reply_text(helptxt)
    
    
