class NationalPark:
    national_parks_list = {}

    def __init__(self, name):
        self.name = name
        self.current_visitations = {}
        self.trips = []
        self.visitors = []

        self.national_parks_list_increment(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str:
            if not hasattr(self ,"name"):
                self._name = name
            else:
                raise ValueError ("Cannot reassign value")
        else:
            raise AttributeError ("Name must be a string")
    
    @name.deleter
    def name(self):
        del self.name

        
    def access_current_trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self.trips.append(new_trip)
            self.national_parks_list_newvisit(self)
        return self.trips
    
    def access_current_visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor) and new_visitor not in  self.visitors:
            self.visitors.append(new_visitor)
        if isinstance(new_visitor, Visitor):
            if new_visitor not in self.current_visitations:
                self.current_visitations[new_visitor] = 1
            else:
                self.current_visitations[new_visitor] += 1
        return  self.visitors

    
    def calculate_all_trips(self):
        return len(self.trips)
    
    def check_most_frequent_visitor(self):
        return max(self.current_visitations, key = self.current_visitations.get)
    
    @classmethod
    def national_parks_list_increment(cls, new_trip):
        cls.national_parks_list[new_trip.name] = 1

    @classmethod
    def national_parks_list_newvisit(cls, new_trip):
        cls.national_parks_list[new_trip.name] += 1
        cls.national_parks_list = dict(sorted(cls.national_parks_list.items(), key = lambda x:x[1]))
        print(cls.national_parks_list) 
