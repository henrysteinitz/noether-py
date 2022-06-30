import requests

noether_url = "https://www.noetherapi.com"


def parse_data_input(text: str = None, image_url: str = None, audio_url: str = None, video_url: str = None): 
	if sum([x is not None for x in [text, image_url, audio_url, video_url]]) != 1:
		raise("Exactly one of {text, image_url, audio_url, video_url} must be defined.")
	result = ""
	if text: 
		result += "text={}".format(text)
	elif image_url:
		result += "image_url={}".format(image_url)
	elif audio_url:
		result += "audio_url={}".format(audio_url)
	elif video_url:
		result += "video_url={}".format(video_url)
	return result


class Noether:
	def __init__(self, api_key: str):
		self._api_key = api_key


	def ask(self, question: str, text: str = None, image_url: str = None, audio_url: str = None, video_url: str = None):
		data_input = parse_data_input(text, image_url, audio_url, video_url)
		return requests.get("{}/ask?{}&question={}&api_key={}".format(noether_url, data_input, question, self._api_key)).json()


	def color(self, obj: str = None, image_url: str = None):
		if obj is None:
			return self.ask(image_url=image_url, question="What color is the image")
		else:
			return self.ask(image_url=image_url, question="What color is the {} in the image".format(obj))


	def embed(self, text: str = None, image_url: str = None, audio_url: str = None, video_url: str = None):
		data_input = parse_data_input(text, image_url, audio_url, video_url)
		return requests.get("{}/embed?{}&api_key={}".format(noether_url, data_input, self._api_key)).json()


	def save(self, text: str = None, image_url: str = None, audio_url: str = None, video_url: str = None):
		data_input = parse_data_input(text, image_url, audio_url, video_url)
		return requests.get("{}/save?{}&api_key={}".format(noether_url, data_input, self._api_key)).json()


	def search(self, query: str):
		return requests.get("{}/search?query={}&api_key={}".format(noether_url, query, self._api_key)).json()


	def summary(self, text: str = None, image_url: str = None, audio_url: str = None, video_url: str = None):
		data_input = parse_data_input(text, image_url, audio_url, video_url)
		return requests.get("{}/summary?{}&api_key={}".format(noether_url, data_input, self._api_key)).json()
