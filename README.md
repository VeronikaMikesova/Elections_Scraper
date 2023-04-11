# Elections_Scraper
"""
Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí naleznete https://github.com/VeronikaMikesova/Elections_Scraper.git.

Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
 
Spouštění projektu
Spuštění souboru main.py v rámci příkazové řádky požaduje dva povinné argumenty:
python main.py <odkaz-uzemniho-celku> <vysledny-soubor>

Kontrola zadaných parametrů:
1)	Kontrola počtu parametrů
2)	Kontrola odezvy zvolené URL stránky
3)  Kontrola správné přípony výstupního souboru s daty
Pokud nejsou zadány správné parametry. Program se ukončí.

    (.venv) PS G:\Můj disk\Osobní\Python\Repisitory\Elections_Scraper> python main.py
    ['main.py']
    Není zadán dostatečný počet argumentů. Ukončuji program.
    (.venv) PS G:\Můj disk\Osobní\Python\Repisitory\Elections_Scraper> python main.py "https://seznam.com" "test.csv"
    ['main.py', 'https://seznam.com', 'test.csv']
    https://seznam.com: neodpovídá. Ukončuji program.
    (.venv) PS G:\Můj disk\Osobní\Python\Repisitory\Elections_Scraper> python main.py "https://seznam.cz" "test.txt"
    ['main.py', 'https://seznam.cz', 'test.txt']
    Zadány nesprávné argumenty. Ukončuji program.
 
Ukázka projektu:
1.	argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101
2.	argument: Jeseník.csv

Spouštění programu:
Python main.py „https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101“ „Jeseník.csv“
 
Průběh stahování:
1)	„Stahuji data z vybraného URL“: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101 
2)	„Ukládám do souboru“: Jeseník.csv
3)	„Ukončuji program“

    (.venv) PS G:\Můj disk\Osobní\Python\Repisitory\Elections_Scraper> python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101" "Jeseník.csv"
    ['main.py', 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101', 'Jeseník.csv']
    Stahuji data z vybraného URL:https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101
    Ukládám do souboru:Jeseník.csv
    Ukončuji program.
 
Částečný výstup:
    cislo,název,voliči,obálky,platné hlasy celkem,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů,-
    523917,Bělá pod Pradědem,1 546,945,938,77,1,0,47,2,53,70,8,12,10,0,1,79,1,33,331,0,3,42,0,7,0,1,158,2,-
    524891,Bernartice,703,344,343,24,0,0,25,1,6,38,1,1,1,0,0,15,0,5,149,2,1,13,1,0,1,1,58,0,-
    525227,Bílá Voda,242,140,138,17,1,0,7,1,5,14,6,2,0,0,0,13,0,9,18,1,0,16,0,0,1,1,25,1,-
    533491,Černá Voda,495,269,269,14,0,0,14,1,16,30,2,1,4,0,0,27,0,13,89,2,1,15,0,0,0,0,40,0,-
    569356,Česká Ves,1 964,1 139,1 126,62,0,0,70,4,139,92,9,8,10,0,0,64,4,61,355,0,0,52,0,2,0,1,193,0,-
    553301,Hradec-Nová Ves,312,162,161,15,0,0,12,0,13,14,3,1,2,0,0,12,0,0,46,3,0,10,0,1,0,0,29,0,-
    536148,Javorník,2 269,1 229,1 212,99,3,1,111,0,23,137,14,11,12,0,0,100,2,19,419,1,4,48,0,7,2,1,194,4,-

"""
