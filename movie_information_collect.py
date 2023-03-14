class movies:
    def __init__(self,titel,hero,heroin):
        self.titel = titel
        self.hero = hero
        self.heroin = heroin
    
    def information(self):
        print(f"Movies Name : {self.titel}")
        print(f"Hero Name : {self.hero}")
        print(f"Heroin: {self.heroin}")

movie_list = []
while True: 
    title = input("Enter Movie name: ")
    hero = input("Enter the name of Hero: ")
    heroin = input("Enter the name of Heroin: ")
    m = movies(title,hero,heroin)
    movie_list.append(title)
    file = open("Movie  Data.txt","w")
    file.write(title)
    file.close()
    opstion = input("Do you want to add movie [Yes/No] : ")
    if opstion.lower() == "no":
        print()
        break
print("All information ......")
for movie in movie_list: 
    f"{movie}.{m.information()}"
    print()

    
    