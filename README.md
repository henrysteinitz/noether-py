
## How to install
```
pip install noether-api
```

## How to use
Let's ask Noether about the following image:
![Image](https://cdn.vox-cdn.com/thumbor/oCiqoTZlurIloHrG8O3cHqpBOiE=/241x193:2304x1644/1200x800/filters:focal(1034x301:1446x713)/cdn.vox-cdn.com/uploads/chorus_image/image/53741489/618916710.0.jpg)

```
# Import NoetherClient
from noether_api import NoetherClient

# Create Noether client
noether = NoetherClient(api_key="...")

image_url = "https://cdn.vox-cdn.com/thumbor/oCiqoTZlurIloHrG8O3cHqpBOiE=/241x193:2304x1644/1200x800/filters:focal(1034x301:1446x713)/cdn.vox-cdn.com/uploads/chorus_image/image/53741489/618916710.0.jpg"

# Ask 
result = noether.ask(
	image_url=image_url,
	question="What color are the letters on the player's shirt?"
)
print(result)
```
The script above should print the following:
```
{'data': ['white'], 'success': True}
```

Let's ask a few more questions:
```
result = noether.ask(
	image_url=image_url,
	question="What color is the player's shirt?"
)
print(result)
```
```
{'data': ['black'], 'success': True}
```
```
result = noether.ask(
	image_url=image_url,
	question="What sport are they playing?"
)
print(result)
```
```
{'data': ['basketball'], 'success': True}
```
Visit [noether.dev](https://noether.dev) for more details.