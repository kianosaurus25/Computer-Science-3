# These are the variables used
year = int(input("Enter your birth year: "))
sign = ""
#This code checks if the year is valid
if year < 1900:
    print("Invalid year. The year of birth must be 1900 or later.")
    #ends code if the year is invalid
    (exit())
#This code checks for the zodiac sign based on the remainder of the year when divided by 12
else:
    zodiac_signs = {
        0: "Monkey (猴 / Hóu)",
        1: "Rooster (鸡 / Jī)",
        2: "Dog (狗 / Gǒu)",
        3: "Pig (猪 / Zhū)",
        4: "Rat (鼠 / Shǔ)",
        5: "Ox (牛 / Niú)",
        6: "Tiger (虎 / Hǔ)",
        7: "Rabbit (兔 / Tù)",
        8: "Dragon (龙 / Lóng)",
        9: "Snake (蛇 / Shé)",
        10: "Horse (马 / Mǎ)",
        11: "Sheep (羊 / Yáng)"
    }
#This part calculates the zodiac sign based on the year of birth and prints it
    sign = zodiac_signs[(year - 4) % 12]

print(f"Your Chinese zodiac sign is: {sign}")