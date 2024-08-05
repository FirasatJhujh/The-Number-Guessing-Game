import tkinter as tk
import customtkinter as ctk
import random

# cl["key"][0] = background , cl["key"][1] = foreground
cl = {
    # labels
    "lb1": ["#00356d", "white"],
    "lb2": ["white", "#137aa2"],
    "lb3": ["white", "black"],
    "lb4": ["white", "black"],
    "lb5": ["white", "#6f73aa"],
    # Entry
    "en1": ["white", "#631d8c"],
    # Frame
    "frm1": ["white"],
    # Button
    "btn1": ["#0945ce", "white"]
}

# mainValues:There are something that we can change like number of chances , guessing range etc
mainValues = {
    "remain": 10,
    "chances": 10,
    "guess_number_to": 15
}


class Number_Guessing_Game():
    def __init__(self) -> None:
        self.root = tk.Tk()

        # some important variables
        self.comp = random.randint(1, mainValues["guess_number_to"])
        self.user = tk.StringVar(self.root)


        self.chances = mainValues["chances"]
        self.remain = mainValues["remain"]
        self.hint = ""

        # declaring geometry(700x500) , title(Number Guessing Game) , background(white) , resizable(0,0) , icon(icon.ico)
        self.root.geometry("700x500")
        self.root.title("Number Guessing Game")
        self.root.configure(bg="#ffffff")
        self.root.resizable(False, False)
        self.root.iconbitmap("C:\\Users\\Firasat ali jhuih\\Desktop\Projects\\Guess Number\\Iamges\\icon.ico")

        # ========================== Main frame as mainfrm ======================
        self.mainfrm = ctk.CTkFrame(self.root, fg_color="white")

        # heading label (lb1)
        lb1 = ctk.CTkLabel(self.mainfrm, text="Number Guessing Game",
                           font=("Roboto", 25), fg_color=cl["lb1"][0],
                           text_color=cl["lb1"][1],
                           width=650, height=40).pack()

        # guess number between label (lb2)
        lb2 = ctk.CTkLabel(self.mainfrm, text=f"Guess a number between 1 and {mainValues['guess_number_to']}",
                           font=("Roboto", 20, "bold"), fg_color=cl["lb2"][0],
                           text_color=cl["lb2"][1],
                           width=650, height=40).pack(pady=7)

        # asking number entry (en1)
        en1 = ctk.CTkEntry(self.mainfrm, font=("Poetsen One", 30, "bold"),
                           justify="center",
                           textvariable=self.user,
                           fg_color=cl["en1"][0],
                           text_color=cl["en1"][1],
                           width=240, height=40).pack(pady=7, ipadx=10, ipady=10)

        # submit button (btn1)
        btn1 = ctk.CTkButton(self.mainfrm, text="Guess", font=("Roboto", 20, "bold"),
                             fg_color=cl["btn1"][0],
                             text_color=cl["btn1"][1],
                             command=self.guess,
                             width=200, height=40).pack(pady=10, ipadx=10, ipady=10)

        # ===================== start Summary frame ===========================
        # summery frame (frm1)
        frm1 = ctk.CTkFrame(self.mainfrm, border_width=2, border_color="lightgrey", fg_color="white")
        # total Chances label (self.lb3)
        self.lb3 = ctk.CTkLabel(frm1, text="Total Chances as : " + str(self.chances),
                                width=300,
                                font=("Roboto", 18), fg_color=cl["lb3"][0], anchor="nw")
        self.lb3.pack(padx=(5, 3), pady=(12, 0))
        # remaining Chances label (self.lb4)
        self.lb4 = ctk.CTkLabel(frm1, text="Remain Chancess are : " + str(self.remain),
                                width=300,
                                font=("Roboto", 18), fg_color=cl["lb4"][0], anchor="nw")
        self.lb4.pack(padx=(7, 3), pady=(0, 12))

        frm1.pack(pady=10)
        # ===================== end Summary frame ===========================

        # hint label (self.lb5)
        self.lb5 = ctk.CTkLabel(self.mainfrm, text="",
                                font=("Roboto", 20, "bold"), fg_color=cl["lb5"][0],
                                text_color=cl["lb5"][1],
                                width=650, height=40)

        # packing variable
        self.lb5.pack(pady=7)
        self.mainfrm.pack(fill="both", expand=True)

        self.root.mainloop()

    def guess(self):
        # Check that what user enter the valied input 
        try:

            # assigning ans as user - comp
            ans = int(self.user.get()) - self.comp
            
                # ================== start If else nest    ==============
            if (self.remain != 1):

                if (self.userValue < 0 or self.userValue > 15 ):
                    # checking number is between 0 & 15.
                    self.hint = "Please enter number between 0 and 15."
                    self.remain += 1

                elif (ans == 0):
                    # Checking answer
                    self.mainfrm.pack_forget()
                    self.flashMessage("You Win")
                    self.hint = ""

                elif (ans > 0):
                    # Come here if answer is greater.
                    if (ans <= 4):
                        self.hint = "Your Number is few digit Greater."
                    elif (ans <= 8):
                        self.hint = "Your Number is little Greater."
                    else:
                        self.hint = "Your Number is  Greater."


                else:
                    # Come here if answer is smaller.
                    if (ans >= -4):
                        self.hint = "Your Number is few digit Smaller."
                    elif (ans >= -8):
                        self.hint = "Your Number is little Smaller."
                    else:
                        self.hint = "Your Number is  Smaller."

            else:
                # when user have no chance
                self.mainfrm.pack_forget()
                self.flashMessage("You Lose")

                self.lb5.configure(text=self.hint)
                self.user.set("")

            # ================== end If else nest    ==============
        
        except:
            # Come here when user give the invalided input
            self.hint =f"Enter the number between 1 and {mainValues['guess_number_to']}"
            #Increase the value of remain by one because when user give the invalid input, Its should not consider but in the finally the value of remain is decreasing by one.so if I increse 1 so remain'll not decrease
            self.remain += 1
        
        finally:
            # Changing  variables value.
            self.remain -= 1
            self.lb4.configure(text="Remain Chances are : " + str(self.remain))
            self.lb5.configure(text=self.hint)
            self.user.set("")

    def flashMessage(self, text="", textClour="black", btnClour=["blue", "white"]):
        # flashMessage() function displays message screen when we win or loose.
        def restart_game():
            # restart_game() function is for restart game.

            frm3.pack_forget()  # applying pack_forget() on flashMessage's main frame (frm3)
            self.mainfrm.pack(fill="both", expand=True)  # pack again main frame (mainfrm)

            # reset main variables
            self.remain = mainValues["remain"]
            self.chances = mainValues["chances"]
            self.comp = random.randint(1, mainValues["guess_number_to"])
            self.lb3.configure(text="Total Chances as : " + str(self.chances))
            self.lb4.configure(text="Remain Chances are : " + str(self.remain))

        # Main frame of flashMessage (frm3)
        frm3 = ctk.CTkFrame(self.root, fg_color="white")
        # Message label "You loose" or "You Win"  (lb6)
        lb6 = ctk.CTkLabel(frm3, text=text,
                           font=("Roboto", 60, "bold"), fg_color="white",
                           text_color=textClour,
                           width=650, height=40).pack(pady=20)
        # frame for btns (frm4)
        frm4 = ctk.CTkFrame(frm3, fg_color="white")

        # btn for play again (btn2)
        btn2 = ctk.CTkButton(frm4, text="Play Again", font=("Roboto", 20, "bold"),
                             fg_color=btnClour[0],
                             text_color=btnClour[1],
                             command=restart_game,
                             width=200, height=40).pack(pady=(0, 20))
        # btn for exit (btn3)
        btn3 = ctk.CTkButton(frm4, text="Exit", font=("Roboto", 20, "bold"),
                             fg_color="lightgrey",
                             text_color="black",
                             command=self.root.destroy,
                             width=200, height=40).pack(pady=(0, 20))
        #   packing btn frame (frm4)
        frm4.pack(pady=20)
        #   packing main frame of flashMessage (frm3)
        frm3.pack(fill="both", expand=True)


if __name__ == "__main__":
    game = Number_Guessing_Game()
