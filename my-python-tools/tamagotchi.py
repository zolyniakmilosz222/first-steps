import tkinter as  tk
from tkinter import colorchooser
gra = False
x = 100
y = 100
z = 100
i = 99
j= 99
k= 99
szerokość_okna_startowego = 500
wysokość_okna_startowego = 500
#def animacja_okna_głównego():

def animacja():
    global i, j, k, x
    if x == 100:
        i -= 1 
        j -= 1
        k -= 1
        okno_startowe.after(299, animacja)

def poziom_zadowolenia_stworka():
    global x, y, z
    if gra:
        x -= 1 
        y -= 1
        z -= 1
        okno_startowe.after(10, poziom_zadowolenia_stworka)

def start_gry():
    global gra, nowe_okno
    gra = True
    nowe_okno = tk.Toplevel(okno_startowe)
    nowe_okno.title("Nowe okno")
    nowe_okno.geometry("600x600")
    napis = tk.Label(nowe_okno, text="GRA",)
    napis.place(relx=0.5, rely=0.5, anchor="center")
    uzupełnij_pragnienie = tk.Button(
    nowe_okno,
    fg="green",
    bg="gray",
    text="pragnienie",
    font=("Arial", 20),
    command=start_gry
    
    )

    uzupełnij_zdrowie = tk.Button(
    nowe_okno,
    fg="green",
    bg="gray",
    text="zdrowie",
    font=("Arial", 20),
    command=start_gry
    
    )

    uzupełnij_zabawe = tk.Button(
    nowe_okno,
    fg="green",
    bg="gray",
    text="zabawa",
    font=("Arial", 20),
    command=start_gry
    )
    uzupełnij_pragnienie.place(
    relx=0.2,
    rely=0.9,
    anchor="center"
    )
    uzupełnij_zdrowie.place(
    
    relx=0.5,
    rely=0.9,
    anchor="center"
    )
    uzupełnij_zabawe.place(
    
    relx=0.8,
    rely=0.9,
    anchor="center"
    )
    poziom_zadowolenia_stworka()
    check()

def check():
    global x, y, z
    if gra:
        print (x, y, z)
        nowe_okno.after(200, check)
def cos():
    global i, j, k
    if x == 100:
        print (i, j, k)
        okno_startowe.after(200, cos)

okno_startowe = tk.Tk()

img = tk.PhotoImage(width=szerokość_okna_startowego, height=wysokość_okna_startowego)
canvas = tk.Canvas(okno_startowe, width=szerokość_okna_startowego, height=wysokość_okna_startowego)
canvas.pack()
canvas.create_image((0, 0), image=img, anchor= "nw")
okno_startowe.geometry(f'{szerokość_okna_startowego}x{wysokość_okna_startowego}')
img.put("red", (10, 10))
img.put(f'#EE{j}{k}', to=(10, 0, szerokość_okna_startowego,wysokość_okna_startowego))
#img.put("#FF0000", to=(10, 0, szerokość_okna_startowego,wysokość_okna_startowego))
#img.put("#EE9999", to=(10, 0, szerokość_okna_startowego,wysokość_okna_startowego))


przycisk = tk.Button(
    okno_startowe,
    fg="green",
    bg="gray",
    text="Graj!",
    font=("Arial", 20),
    command=start_gry
    
)
przycisk.place(
    relx=0.5,
    rely=0.5, 
    anchor="center"
)
tytuł = tk.Label(
    okno_startowe,
    fg="black",
    text="MAGICZNY STWOREK",
    font=("Verdana", 12, "bold")
)
tytuł.place(
    
    relx=0.5,
    rely=0.1,
    anchor="center"
)
cos()
animacja()
okno_startowe.mainloop()
