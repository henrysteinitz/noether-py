
## How to install
```
pip install noether-api
```

## How to use
```
# Import NoetherClient
from noether_api import NoetherClient

# Create Noether client
noether = NoetherClient(api_key="...")

# Ask 
result = noether.ask(
	image_url="https://cdn.vox-cdn.com/thumbor/oCiqoTZlurIloHrG8O3cHqpBOiE=/241x193:2304x1644/1200x800/filters:focal(1034x301:1446x713)/cdn.vox-cdn.com/uploads/chorus_image/image/53741489/618916710.0.jpg",
	question="What color are the letters on the players shirt?"
)
print(result)
```

The script above should print the following:
```
{'data': ['white'], 'success': True}
```