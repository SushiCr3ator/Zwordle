import nextcord

def generate_blanks():
    return "\N{WHITE MEDIUM SQUARE}" * 5

def generate_puzzle_embed():
    embed = nextcord.Embed(title="Zwordle")
    embed.description="\n".join([generate_blanks()] *6)
    embed.set_footer(text=
        "To play, use command /play! \n" 
        "To guess, reply to this message with a word."
    )
    return embed