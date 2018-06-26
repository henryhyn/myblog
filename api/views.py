import json
import gensim
from django.http import HttpResponse
from myblog.settings import BASE_DIR

model = gensim.models.KeyedVectors.load_word2vec_format(BASE_DIR + '/api/StaticData/out2', binary=False)


def __build_response(rs):
    response = HttpResponse(json.dumps(rs))
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response


def similar_word(request):
    word = request.GET.get('word', '一般')
    topn = request.GET.get('topn', '10')
    rs = model.most_similar(word, topn=int(topn))
    return __build_response(rs)
