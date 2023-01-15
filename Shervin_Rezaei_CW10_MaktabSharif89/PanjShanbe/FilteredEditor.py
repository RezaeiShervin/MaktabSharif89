class filtered_editor:
    bad_words={"gun": "gum", "war": "car", "maktab_sharif" : "out of range", "karshenas-amuzesh" : None}

    def __init__(self, text):
        self.text = text

    def __enter__(self):
        for key in filtered_editor.bad_words:
            if filtered_editor.bad_words[key]:
                replace_word = filtered_editor.bad_words[key]

            else:
                replace_word = len(key) * "*"
                print(f"warning:{key} is not have suitable equivalent.")

            self.text = self.text.replace(key, replace_word)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.text)


text = "i kill karshenas-amuzesh with gun in war with maktab_sharif , group 6"
with filtered_editor(text):
    pass
