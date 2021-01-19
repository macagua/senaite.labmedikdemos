from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from senaite.labmedikdemos import labmedikdemosMessageFactory as _

class MyHelloWorldViewlet(ViewletBase):
	render = ViewPageTemplateFile('myhelloworldviewlet.pt')

	def update(self):
		self.company = _(u'Plone Foundation!!!')
