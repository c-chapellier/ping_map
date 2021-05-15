# ping_map
Pinging random addresses to create a map

## Dependencies

```bash
# python3 --version
# Python 3.9.5

pip3 install    pandas \
                pygal \
                pygal_maps_world \
                cairosvg \
                geoip2
```

## Usage

```bash
# Gather data by pinging random IP adresses.
python3 ping_the_world.py

# Gather data by pinging specified IP adresses.
python3 ping_the_world.py ip1 ip2 ..

# Create a map with the data.
python3 create_map.py locations.csv
```

## Output

![alt text](https://github.com/c-chapellier/ping_map/blob/master/data/binks_ping_map.png)

![alt text](https://github.com/c-chapellier/ping_map/blob/master/data/binks_data.csv)
