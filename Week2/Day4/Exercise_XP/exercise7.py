import random

def get_random_temp(month):
    if month == 12 or month in range(1, 3):
        return random.uniform(-10.0, 11.0), 'winter'
    if month in range(3, 6):
        return random.uniform(17.0, 24.0), 'spring'        
    elif month in range(6, 9):
        return random.uniform(25.0, 40.0), 'summer'
    elif month in range(9, 12):    
        return random.uniform(12.0, 20.0), 'autumn'

def main():
    month = int(input("Enter number of month: "))
    temp_season = get_random_temp(month)
    temp = float('{:.2f}'.format(temp_season[0]))
    season = temp_season[1].capitalize()
    if temp < 0:
        print(f"{season}!\nThe temperature right now is {temp} degrees Celsius.\nBrrr, that's freezing! Wear some extra layers today.")
    elif temp < 16:
        print(f"{season}!\nThe temperature right now is {temp} degrees Celsius.\nQuite chilly! Don't forget your coat.") 
    elif temp < 24:
        print(f"{season}!\nThe temperature right now is {temp} degrees Celsius.\nIt's a lovely day! Wear whatever you want.")  
    elif temp < 33:   
        print(f"{season}!\nThe temperature right now is {temp} degrees Celsius.\nIt's hot! Wear something light. And don't forget to drink plenty of water.")
    else:
        print(f"{season}!\nThe temperature right now is {temp} degrees Celsius.\nIt's sweltering! Stay inside and drink plenty of water.") 

main()
          