import json

class PageRender:
	def __init__(self, nameChapter):
		self.nameChapter = nameChapter
		self.jsonFilePath = 'static/'+nameChapter+'/metadata.json'
	def getPageList(self):
		with open(self.jsonFilePath) as f:
		    data = json.load(f)
		# print(data)
		listPage = data['metadata']['pages']
		return listPage
	def render(self):
		pages = self.getPageList()
		htmlRender = """ """
		for p in pages:
			htmlRender += """ <img src= "{{url_for('static', filename='"""+p+"""')}}" alt="02" class = "singlePage"> """
		return htmlRender
	