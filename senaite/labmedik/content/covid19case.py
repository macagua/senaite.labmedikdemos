"""Definition of the COVID-19 Case content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.Archetypes.public import StringField
from Products.Archetypes.public import StringWidget

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from senaite.labmedik import labmedikMessageFactory as _

from senaite.labmedik.interfaces import ICOVID19Case
from senaite.labmedik.config import PROJECTNAME

COVID19CaseSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    StringField(
        "CaseID",
        widget=StringWidget(
            label=_("Case ID"),
            description=_("COVID 19 Case id from Person Test"),
        ),
    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

COVID19CaseSchema['title'].storage = atapi.AnnotationStorage()
COVID19CaseSchema['description'].storage = atapi.AnnotationStorage()

COVID19CaseSchema['title'].validators = ()
COVID19CaseSchema['title'].widget.description = _("If no value is entered, the Title"
                                                  " will be auto-generated.")

COVID19CaseSchema['title'].required = False
COVID19CaseSchema['title'].widget.visible = False
COVID19CaseSchema['title'].widget.description = _("If no description value is entered,"
                                                  " the COVID-19 Case ID will be used.")

COVID19CaseSchema['description'].required = False
COVID19CaseSchema["description"].widget.visible = False

schemata.finalizeATCTSchema(COVID19CaseSchema, moveDiscussion=False)


class COVID19Case(base.ATCTContent):
    """A register for a COVID-19 Case"""
    implements(ICOVID19Case)

    meta_type = "COVID19Case"
    schema = COVID19CaseSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(COVID19Case, PROJECTNAME)
