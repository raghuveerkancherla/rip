class Request(object):
    """
    All actions objects when called create a request object before passing the call to a handler.
    A request object has a requesting_user, params of the call and the caller. Caller is the name of the
    action object making the call
    """

    def __init__(self, user, request_params, data=None, context_params=None,
                 request_headers=None, request_body=None,
                 request_get_params=None, url_kwargs=None):

        self.user = user or None
        self.request_params = request_params or {}
        # request_params = request_get_params + url_kwargs
        self.request_get_params = request_get_params or {}
        self.url_kwargs = url_kwargs or {}
        self.data = data or {}
        self.request_headers = request_headers or {}
        self.request_body = request_body

        # computed data or contextual information like api name etc.
        self.context_params = context_params or {}

    def __eq__(self, val):
        return self.user == val.user and \
               self.request_params == val.request_params and \
               self.data == self.data and \
               self.context_params == val.context_params
