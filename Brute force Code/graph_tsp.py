from itertools import permutations
import csv
import logging
from colorama import Fore, Back, Style
import matplotlib.pyplot as plt
class graph_tsp():
    def __init__(self, filename):
        try:
            self.logger = self.setupLogger()
            self.filename = filename
            # Open CSV file and read each row into a list of lists
            with open('data/' + self.filename + '.csv', newline='') as file:
                reader = csv.reader(file)
                points_original = list(map(list, reader))
            # Remove header column
            del points_original[0]
            # Remove city index from the points
            cities = []
            for point in points_original:
                cities.append(point.pop(0))
            # Convert string values to float
            points = []
            for item in points_original:
                point = []
                for values in item:
                    point.append(float(values))
                points.append(point)
            # Show Plot for original data provided
            title = 'The TSP Original Data Route'
            self.plotIt(points, title)
            self.logger.info('CSV file data/' + self.filename + '.csv was read...')
            # Print distance
            print("""Original Distance: {} \nRecommended Tour Route: {} \nMinimum distance: {}""".format('{0:.1f}'.format(self.total_distance(points)),tuple(points), '{0:.1f}'.format(self.total_distance(self.calculate_TSP(points)))))
        except Exception as e:
            self.logger.error(Fore.RED + 'Error reading CSV data/' + self.filename + '.csv file... %s' % str(e) + Style.RESET_ALL)
    def setupLogger(self):
        logfile = 'logs/app_log.txt'
        # Format log to add time, level and message
        logging.basicConfig(level=logging.WARNING)
        logFormatter = logging.Formatter('%(asctime)s - %(levelname)s --: %(message)s')
        logger = logging.getLogger(__name__)
        # Add handler to send logs to log file
        handler = logging.FileHandler(logfile)
        handler.setFormatter(logFormatter)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
        logger.info('Logs written in %s' % logfile)
        return logger
    def distance(self, point_one, point_two):
        complete = False
        try:
            distance = ( (point_one[0] - point_two[0]) ** 2.0 + (point_one[1] - point_two[1]) ** 2.0) ** 0.5
            complete = True
            return distance
        except Exception as e:
            self.logger.error(Fore.RED + 'Error calculating distance between points... %s' % str(e) + Style.RESET_ALL)
        finally:
            if complete:
                self.logger.info('Distance between all points has been calculated...')
    def total_distance(self, points):
        # Determine if the function has been completed
        complete = False
        try:
            total_distance = sum([self.distance(p, points[value + 1]) for value, p in enumerate(points[:-1])])
            complete = True
            return total_distance
        except Exception as e:
            self.logger.error(Fore.RED + 'Error calculating total distance between points... %s' % str(e) + Style.RESET_ALL)
        finally:
            if complete:
                self.logger.info('Total distance between all points has been calculated...')
    def calculate_TSP(self, points):
        # Determine if the function has been completed
        complete = False
        # Starting position
        start_position = points[0]
        # Places to visit
        visit_list = points
        # Set tour to starting position
        tour = [start_position]
        # Remove the starting position
        visit_list.remove(start_position)
        try:
            # Loop through places to visit to find min distance
            while visit_list:
                key_value = lambda y: self.distance(tour[-1], y)
                # Find nearest city
                nearest_city = min(visit_list, key = key_value)
                # Append nearest city to the tour and remove it from the visit list
                tour.append(nearest_city)
                visit_list.remove(nearest_city)
            complete = True
            # Show Plot for the evaluated min tour route order
            title = 'The TSP Calculated Minimum Route'
            self.plotIt(tour, title)
            return tour
        except Exception as e:
                self.logger.error(Fore.RED + 'Error calculating minimum distance between points and finding total path... %s' % str(e) + Style.RESET_ALL)
        finally:
                    if complete:
                        self.logger.info('Minimum distance between all points and path have been calculated...')
    def plotIt(self, tour_points, title):
        try:
            # Grab X and Y values of points
            x = []
            y = []
            for values in tour_points:
                x.append(values[0])
                y.append(values[1])
            # Append the first item to the end to complete the loop
            x.append(x[0])
            y.append(y[0])
            # Setup plot
            plt.plot(x, y, 'b--')
            plt.xlabel('Longitude (X)')
            plt.ylabel('Latitude (Y)')
            plt.title(title)
            plt.grid(True)
            # Plot TSP route
            plt.show()
            self.logger.info('Plot created of route... ')
        except Exception as e:
                    self.logger.error(Fore.RED + 'Error plotting route. Check data provided and/or graph settings... %s' % str(e) + Style.RESET_ALL)





                    
