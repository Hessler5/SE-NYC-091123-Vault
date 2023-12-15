from classes.visitor import Visitor

class Trip:
    counter, catalog = 0, []
    def __init__(self, visitor, national_park, start_date=None, end_date=None):
        # DO NOT EDIT – Datetime Initialization Script –––––––––––– #
        NO_START_DATE_PROVIDED = (start_date is None)               #
        NO_END_DATE_PROVIDED = (end_date is None)                   #
        if NO_START_DATE_PROVIDED or NO_END_DATE_PROVIDED:          #
            from datetime import date, timedelta                    #
            if NO_START_DATE_PROVIDED:                              #
                self.start_date = date.today()                      #
            if NO_END_DATE_PROVIDED:                                #
                self.end_date = date.today() + timedelta(days=1)    #
        else:                                                       #
            self.start_date, self.end_date = start_date, end_date   #
        # DO NOT EDIT – Datetime Initialization Script –––––––––––– #
        
        self.visitor = visitor
        self.national_park = national_park

        Trip.counter += 1
        Trip.catalog.append(self)

        self.visitor.access_current_trips(self)
        self.visitor.access_current_parks(national_park)
        self.national_park.access_current_trips(self)
        self.national_park.access_current_visitors(visitor)

    @property
    def start_date(self):
        return self._start_date() 
    
    @start_date.setter
    def start_date(self, new_start_date):
        new_start_date_check = (str(new_start_date).split("-"))
        if len(new_start_date_check[0]) == 4 and len(new_start_date_check[1]) == 2 and len(new_start_date_check[2]) == 2:
            self._start_date = new_start_date

    @property
    def end_date(self):
        return self._start_date() 
    
    @end_date.setter
    def end_date(self, new_end_date):
        new_end_date_check = (str(new_end_date).split("-"))
        if len(new_end_date_check[0]) == 4 and len(new_end_date_check[1]) == 2 and len(new_end_date_check[2]) == 2:
            self._start_date = new_end_date

    @property
    def visitor(self):
        return self._visitor 
    
    @visitor.setter
    def visitor(self, visitor):
        if type(visitor) == Visitor:
            self._visitor = visitor
        else:
            raise AttributeError("Visitor must be a Visitor type")
        
    @visitor.deleter
    def name(self):
        del self.name

    def __repr__(self):
        from datetime import datetime
        return f"{self.visitor.name} is going on a trip to {self.national_park.name} from {datetime.strftime(self.start_date, '%m/%d/%Y')} to {datetime.strftime(self.end_date, '%m/%d/%Y')}."


