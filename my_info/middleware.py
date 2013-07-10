from http_request_storage.models import HttpRequestStorage
from datetime import datetime
	
class RequestStorageMiddleware(object):
	def process_request(self, request):
		return HttpRequestStorage.objects.create(date=datetime.now(),\
		              path = request.path[:100])
		
