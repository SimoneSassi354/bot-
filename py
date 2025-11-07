import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def consiglio_eco(tipo: str) -> str:
    if tipo.lower() == "casa":
        return "Riduci il consumo di plastica, spegni le luci quando non servono e usa lampadine LED!"
    elif tipo.lower() == "trasporti":
        return "Prova a usare la bicicletta, camminare di più o i mezzi pubblici per ridurre le emissioni."
    elif tipo.lower() == "alimentazione":
        return "Riduci il consumo di carne, preferisci prodotti locali e stagionali!"
    else:
        return "Non ho consigli per questo tipo, prova: casa, trasporti o alimentazione."

def info_inquinamento(argomento: str) -> str:
    if argomento.lower() == "aria":
        return "L'inquinamento dell'aria causa smog e problemi respiratori. Riduci emissioni veicolari e industriali!"
    elif argomento.lower() == "acqua":
        return "L'inquinamento dell'acqua avvelena fiumi, laghi e mari. Evita sostanze chimiche nocive!"
    elif argomento.lower() == "suolo":
        return "L'inquinamento del suolo degrada terreni agricoli. Ricicla e riduci pesticidi!"
    else:
        return "Non ho informazioni su questo argomento, prova: aria, acqua o suolo."

@bot.event
async def on_ready():
    print(f"Bot connesso come {bot.user}")
    await bot.change_presence(activity=discord.Game(name="!aiuto per i comandi ecologici"))

@bot.command()
async def ciao(ctx):
    await ctx.send(f"Ciao {ctx.author.mention}! Sono il tuo bot ecologico!")

@bot.command()
async def consiglio(ctx, categoria: str):
    messaggio = consiglio_eco(categoria)
    await ctx.send(messaggio)

@bot.command()
async def info(ctx, tipo: str):
    messaggio = info_inquinamento(tipo)
    await ctx.send(messaggio)

@bot.command()
async def aiuto(ctx):
    testo = (
        "**Comandi disponibili:**\n"
        "`!ciao` - Saluta il bot\n"
        "`!consiglio <categoria>` - Ricevi un consiglio ecologico (casa, trasporti, alimentazione)\n"
        "`!info <tipo>` - Informazioni sull'inquinamento (aria, acqua, suolo)\n"
        "`!aiuto` - Mostra questo messaggio"
    )
    await ctx.send(testo)

bot.run("MTQzNjEyMjY0NTcxMTI5NDQ3MQ.Gf_qcu.zlSixoziQlpivJsee55HIv3Dw_p3x02OQgCF1Q")
