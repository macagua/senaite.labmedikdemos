"""Definition of the COVID-19 Cases Folder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from senaite.labmedik.interfaces import ICOVID-19CasesFolder
from senaite.labmedik.config import PROJECTNAME

COVID-19CasesFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

COVID-19CasesFolderSchema['title'].storage = atapi.AnnotationStorage()
COVID-19CasesFolderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    COVID-19CasesFolderSchema,
    folderish=True,
    moveDiscussion=False
)


class COVID-19CasesFolder(folder.ATFolder):
    """A folderish for COVID-19 Cases"""
    implements(ICOVID-19CasesFolder)

    meta_type = "COVID-19CasesFolder"
    schema = COVID-19CasesFolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(COVID-19CasesFolder, PROJECTNAME)
