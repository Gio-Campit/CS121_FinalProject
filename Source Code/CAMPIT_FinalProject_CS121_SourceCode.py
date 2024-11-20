import random

# Define all the regions and provinces with their capitals
regions = {
    "Ilocos Region": {
        "Ilocos Norte": "Laoag",
        "Ilocos Sur": "Vigan",
        "La Union": "San Fernando",
        "Pangasinan": "Lingayen"
    },
    "Cagayan Valley": {
        "Batanes": "Basco",
        "Cagayan": "Tuguegarao",
        "Isabela": "Ilagan",
        "Nueva Vizcaya": "Bayombong",
        "Quirino": "Cabarroguis"
    },
    "Central Luzon": {
        "Aurora": "Baler",
        "Bataan": "Balanga",
        "Bulacan": "Malolos",
        "Nueva Ecija": "Palayan",
        "Pampanga": "San Fernando",
        "Tarlac": "Tarlac City",
        "Zambales": "Iba"
    },
    "CALABARZON": {
        "Batangas": "Batangas City",
        "Cavite": "Trece Martires",
        "Laguna": "Santa Cruz",
        "Quezon": "Lucena",
        "Rizal": "Antipolo"
    },
    "Mimaropa": {
        "Occidental Mindoro": "Mamburao",
        "Oriental Mindoro": "Calapan",
        "Marinduque": "Boac",
        "Romblon": "Romblon",
        "Palawan": "Puerto Princesa"
    },
    "Bicol Region": {
        "Albay": "Legazpi",
        "Camarines Norte": "Daet",
        "Camarines Sur": "Naga",
        "Catanduanes": "Virac",
        "Masbate": "Masbate City",
        "Sorsogon": "Sorsogon City"
    },
    "Western Visayas": {
        "Aklan": "Kalibo",
        "Antique": "San Jose",
        "Capiz": "Roxas City",
        "Guimaras": "Jordan",
        "Iloilo": "Iloilo City",
        "Negros Occidental": "Bacolod"
    },
    "Central Visayas": {
        "Bohol": "Tagbilaran",
        "Cebu": "Cebu City",
        "Negros Oriental": "Dumaguete",
        "Siquijor": "Siquijor"
    },
    "Eastern Visayas": {
        "Biliran": "Naval",
        "Eastern Samar": "Borongan",
        "Leyte": "Tacloban",
        "Northern Samar": "Catarman",
        "Samar": "Catbalogan",
        "Southern Leyte": "Maasin"
    },
    "Zamboanga Peninsula": {
        "Zamboanga del Norte": "Dipolog",
        "Zamboanga del Sur": "Pagadian",
        "Zamboanga Sibugay": "Ipil"
    },
    "Northern Mindanao": {
        "Bukidnon": "Malaybalay",
        "Camiguin": "Mambajao",
        "Lanao del Norte": "Tubod",
        "Misamis Occidental": "Ozamiz",
        "Misamis Oriental": "Cagayan de Oro"
    },
    "Davao Region": {
        "Davao del Norte": "Tagum",
        "Davao del Sur": "Digos",
        "Davao Oriental": "Mati",
        "Davao Occidental": "Malita",
        "Davao de Oro": "Nabunturan"
    },
    "Soccsksargen": {
        "Cotabato": "Kidapawan",
        "Sarangani": "Alabel",
        "South Cotabato": "Koronadal",
        "Sultan Kudarat": "Isulan"
    },
    "Caraga": {
        "Agusan del Norte": "Butuan",
        "Agusan del Sur": "Prosperidad",
        "Surigao del Norte": "Surigao City",
        "Surigao del Sur": "Tandag",
        "Dinagat Islands": "San Jose"
    },
    "BARMM": {
        "Basilan": "Isabela",
        "Lanao del Sur": "Marawi",
        "Maguindanao": "Cotabato City",
        "Sulu": "Jolo",
        "Tawi-Tawi": "Bongao"
    },
    "NCR": {
        "Metro Manila": "Manila"
    },
    "CAR": {
        "Abra": "Bangued",
        "Apayao": "Conner",
        "Benguet": "La Trinidad",
        "Ifugao": "Nayon",
        "Kalinga": "Tabuk",
        "Mountain Province": "Bontoc"
    }
} 

#funtion of converting points into coins
def calculate_coins(points):
    if points < 10:
        return 0
    base_pesos = (points // 5)
    extra_points = points % 5

    extra_pesos = extra_points*0.20
    return base_pesos + extra_pesos


#function for gcash transfer
def Gcash(coins):
   
   while True:
        Gcash_number = input ("Please enter your Gcash Number to receive your coins: ")
    
        if len(Gcash_number) == 11 and Gcash_number.isdigit():
            print (f"Sending {coins:.2f} pesos to Gcash Number {Gcash_number}...")
            print(f"{coins:.2f} pesos has been succesfully sent to your Gcash Account! Thank you for playing the Game!")
            break
        else:
            print("Invalid Gcash Number, Please enter the correct number!")


#donation drive function
def donation(coins):
    donate = input("Coins  has been credited to your account! Would you  like to donate this to Angat Buhay Foundation? (yes/no)").lower()
    if donate == "yes":
        donation_link = ("https://www.angatbuhay.ph/donation-details/")
        print(f"Thank you for your generosity! You can donate your coins here: {donation_link}")
    else:
        print("Thank you for playing the Game! Your coins are yours to keep!")


# Welcome message
def play_game():
    print("Welcome! Are you ready to explore the Philippines?")
    total_points = 0  #initialize the total points
    while True:
        print("Choose a region to start the game (Case Sensitive and should be correct spelling)")
        print("\n".join(regions.keys()))

        # Ask user to choose a region
        chosen_region = input("\nEnter the name of the region you want to play: ")

        # Check if the chosen region is valid
        if chosen_region in regions:
            # Pick a random province from the chosen region
            for province, capital in regions[chosen_region].items():
    
                attempts = 3  # Set the number of attempts

                # Allow the user up to 3 attempts
                while attempts > 0:
                    # Ask the user for the capital of the chosen province
                    answer = input(f"\nWhat is the capital of {province}? ")
        
                    # Check the answer
                    if answer.lower() == capital.lower():
                        if attempts ==3:
                            points = 5
                        elif attempts ==2:
                            points = 3
                        else:
                            points = 1
                        
                        total_points += points
                        print(f"Correct! You got {points} points. Well done!")
                        print(f"You have now a total points of: {total_points}")
                        break
                    else:
                        attempts -= 1
                        if attempts > 0:
                            print(f"Incorrect. You have {attempts} attempt(s) left. Try again.")
                        else:
                            print(f"Incorrect! The correct answer is {capital}.")
            
            play_again = input ("\nContinue Playing? (yes/no):").lower()
            if play_again !="yes":
                print (f"Thank you for playing! Your total points is: {total_points}")
                
                #ask the user whether they want to convert their points into coins
                convertToCoins = input ("would you like to convert your points into coins? (yes/no) ").lower()
                if convertToCoins == "yes":
                    if total_points >=10:
                        coins = calculate_coins(total_points)
                        print(f"Congratulations on getting {coins:.2f} pesos!")

                        Gcash(coins)
                        
                        donation(coins)

                    else:
                        print("You need at least 10 points to convert it into a coin!")
                else:
                    print(f"Congratulations on getting {total_points} points!")
                break
        else:
            try_again = input ("Region not valid! Would you like to try again? ")
            if try_again != "yes":
                print("Thank you for playing the Game!")
                break

play_game()

