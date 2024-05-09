

def testmiddleware(get_response):
    def innerFun(request):
        print('Before request sending view')
        request.myValue = 'we are good students'
  
        resp = get_response(request)
        
        print('Before response sending to client')
        resp.otherValue = 'sometimes good students'
        return resp
    return innerFun