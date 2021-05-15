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

## Data

|ip             |city   |region |country|latitude  |longitude|rtt   |
|---------------|-------|-------|-------|----------|---------|------|
|97.124.210.198 |Phoenix|Arizona|US     |33.4484367|-112.0741|165.79|
|203.68.253.3   |Fenjihu|Taiwan |TW     |25.0833835|121.56286|269.04|
|222.172.146.29 |Kunming|Yunnan |CN     |24.8843019|102.83242|276.51|
|...            |...    |...    |...    |...       |...      |...   |
|117.95.164.220 |Qinnan |Jiangsu|CN     |21.9434443|108.65377|247.00|
|195.162.121.138|London |England|GB     |51.5073219|-0.127647|28.724|
|95.101.144.45  |Slough |England|GB     |51.5111014|-0.594068|22.793|

