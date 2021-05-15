import sys
import pygal
import pandas as pd

class ping_map:

    def __init__(self, locations_path, map_path='ping_map'):
        self.__locations_path = locations_path
        self.__map_path = map_path
        self.__map = None
        self.__create_map()

    def __load_data(self):
        raw_data = pd.read_csv(self.__locations_path)
        data = {}
        # Set mean rtt for each country in a dictionary.
        for country in set(raw_data['country']):
            rtt_sum = 0
            n = 0
            for i in raw_data.index:
                if raw_data['country'][i] == country:
                    rtt_sum += float(raw_data['rtt'][i])
                    n += 1
            if n != 0: # sometimes a nan appears in set, short patch
                data[country.lower()] = rtt_sum / n
        return data

    def __create_map(self):
        data = self.__load_data()
        self.__map = pygal.maps.world.World()
        self.__map.title = 'Ping map'
        self.__map.add('ping', data)

    def save_as_png(self, save_path='ping_map.png'):
        self.__map.render_to_png(save_path)

    def save_as_svg(self, save_path='ping_map.svg'):
        self.__map.render_to_file(save_path)

    def show_in_browser(self):
        self.__map.render_in_browser()


def main():
    if len(sys.argv) != 2:
        print('usage: python3 create_map.py locations.csv', file=sys.stderr)
        exit(1)
    # Create map
    pm = ping_map(sys.argv[1])
    # Show map
    if input('Do you want to open the map in you browser ? yes/no: ') == 'yes':
        pm.show_in_browser()
    # Save map
    if input('Do you want to save the map as png ? yes/no: ') == 'yes':
        pm.save_as_png()
    if input('Do you want to save the map as svg ? yes/no: ') == 'yes':
        pm.save_as_svg()

if __name__ == '__main__':
    # Handle ctrl-C
    try:
       main()
    except KeyboardInterrupt:
        print('\n\n[Process completed]')
        exit(1)
