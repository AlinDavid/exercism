class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.planets = {"Earth": 31557600,
                        "Mercury": 7600543,
                        "Venus": 19414149,
                        "Mars": 59354032,
                        "Jupiter": 374355659,
                        "Saturn": 929292362,
                        "Uranus": 2651370019,
                        "Neptune": 5200418560}

    def convert_sec_to_years(self, planet):
        if planet not in self.planets.keys():
            raise ValueError("This planet is not on the list")
        age_converted = round(self.seconds / self.planets[planet], 2)
        return "Your age is {} {}-years old".format(age_converted, planet)
