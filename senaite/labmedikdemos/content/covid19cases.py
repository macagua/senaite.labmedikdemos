"""Definition of the COVID-19 Cases content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from senaite.labmedikdemos.interfaces import ICOVID19Cases
from senaite.labmedikdemos.config import PROJECTNAME

COVID19CasesSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

COVID19CasesSchema['title'].storage = atapi.AnnotationStorage()
COVID19CasesSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    COVID19CasesSchema,
    folderish=True,
    moveDiscussion=False
)


class COVID19Cases(folder.ATFolder):
    """A folderish for COVID-19 Cases"""
    implements(ICOVID19Cases)

    meta_type = "COVID19Cases"
    schema = COVID19CasesSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(COVID19Cases, PROJECTNAME)

