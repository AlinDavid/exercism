

def convert(number):
    # Initialisation
    check_dict = {3 :"Pling", 5 :"Plang", 7 :"Plong"}
    sound =str()

    # Scan for factor in dictionary
    for i in check_dict :
        if number % i == 0 :
            sound += check_dict[i]

    # Return resulting sound if any factor found, string of the input otherwise
    # return sound if sound else str(number)
    return sound or str(number)
