from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"1.Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url\n\n2.**What's the song you want?** Usage /song <song name>"
    
    await message.reply_text(helptxt)
    
    
