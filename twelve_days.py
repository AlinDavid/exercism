def recite(start_verse, end_verse):
    days = ["null", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
            "ninth", "tenth", "eleventh", "twelfth"]

    verse_dict = {1: "a Partridge in a Pear Tree.",
                  2: "two Turtle Doves, ",
                  3: "three French Hens, ",
                  4: "four Calling Birds, ",
                  5: "five Gold Rings, ",
                  6: "six Geese-a-Laying, ",
                  7: "seven Swans-a-Swimming, ",
                  8: "eight Maids-a-Milking, ",
                  9: "nine Ladies Dancing, ",
                  10: "ten Lords-a-Leaping, ",
                  11: "eleven Pipers Piping, ",
                  12: "twelve Drummers Drumming, "}

    final, poetry = "", ""
    for i in range(start_verse, end_verse + 1):
        final = verse_dict[i] + final
        poetry += "On the {} day of Christmas my true love gave to me: {}. \n\n".format(days[i], final)

    return poetry
