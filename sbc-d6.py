user, empty_ = input("Enter a word: "),""
for i in range(len(user)-1, -1, -1):empty_ += user[i]
print(f" {empty_} - is palendrom " if user.replace(" ","") == empty_.replace(" ","") else f"{user} - is not palendrom")
