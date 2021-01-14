from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class MyHelloWorldViewlet(ViewletBase):
	render = ViewPageTemplateFile('myhelloworldviewlet.pt')

	def update(self):
		self.company = 'Plone Fundation'

