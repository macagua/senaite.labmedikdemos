from Products.Five import BrowserView
# from bika.lims.browser import BrowserView

class HelloWorld(BrowserView):
    '''
    Hello World browser view, as simple string
    '''

    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def __call__(self):
        return "Hello World"
