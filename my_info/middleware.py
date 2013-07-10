from http_request_storage.models import HttpRequestStorage
from datetime import datetime
	
class RequestStorageMiddleware(object):
	def process_request(self, request):
		cur_request = HttpRequestStorage.objects.create(date=datetime.now(),\
		              path_info = request.path_info[:100])
		
