import customtkinter


def plot():

    def button_callback():
        video_url = entry1.get()
        audio_path = entry2.get()
        return video_url, audio_path

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("500*350")


    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Welcome to ClipDigest") #, text_font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(
        master=frame,
        placeholder_text="video url"
    )
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(
        master=frame,
        placeholder_text="load your local audio"
    )
    entry2.pack(pady=12, padx=10)

    button_1 = customtkinter.CTkButton(master=frame, text="Go", command=button_callback)
    button_1.pack(pady=10, padx=10)

    root.mainloop()


## Reference: https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/complex_example.py