from AirlineReservation import Passenger, Employee, Ticket, Flight

# p_id,p_type,p_gender,p_name,p_phonenumber,f_id,pno,f_origin,f_destination,no_of_stops,flight_type
#f_id, f_origin, f_destination, no_of_stops, flight_type, p_id, p_type
f1 = Flight("AE1425", "PHL", "MCI", 1, "AMERICAN EAGLE", "P1", "P4")
f1.get_flight_details("AE1425")

#Instances of Passenger class
p1 = Passenger("P1", "P", "F", "NIKKI", 4258796358, "F1425", "A123", "MCI", "HYD", 3, "American Airlines")
p2 = Passenger("P2", "P", "M", "PRANOOP", 2588796358, "F1425", "A123", "MCI", "HYD", 3, "American Airlines")
p3 = Passenger("P3", "P", "F", "RELLA", 42587961558, "F1420", "A123", "MCI", "BLR", 3, "QATAR")

#Instances of Employee class
e1 = Employee("E1", "E", "M", "RESHWANTH", 142587961558, "F1425", "A123", "MCI", "HYD", 3, "American Airlines")
e2 = Employee("E2", "E", "M", "VINAY", 422587961558, "F1425", "A123", "MCI", "HYD", 3, "American Airlines")
e3 = Employee("E2", "E", "M", "ASHISH", 424587961558, "F1420", "A123", "MCI", "BLR", 3, "QATAR")

#This method prints the travel details for the passenger
p1.get_travel_details_passanger()
#This method prints the travel details for the employee
e1.get_travel_details_employee()

#This method prints the travelling passengers on that flight
p1.get_travelling_passengers()

#Prints the boarding pass
T1 = Ticket("P1", "P", "F", "CHANU", 4258796358, "F1425", "A123", "MCI", "HYD", 3, "American Airlines", "G", "E",12)
T1.get_boarding_pass("CHANU")





