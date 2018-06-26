import json
import gensim
from django.http import HttpResponse
from myblog.settings import BASE_DIR

model = gensim.models.KeyedVectors.load_word2vec_format(BASE_DIR + '/api/StaticData/out2', binary=False)


def similar_word(request):
    word = request.GET.get('word', '一般')
    topn = request.GET.get('topn', '10')
    return HttpResponse(json.dumps(model.most_similar(word, topn=int(topn))))
