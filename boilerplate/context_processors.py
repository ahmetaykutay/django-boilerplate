import os 

def export_vars(request):
    data = {}
    data['NODE_ENV'] = os.getenv('NODE_ENV', 'production')
    return data