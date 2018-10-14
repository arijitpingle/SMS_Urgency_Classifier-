from bayes import Bayes, URGENCIES
from sys import argv
import json

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)



f = open(argv[1], 'r')
json_str = f.read()
message_list = json.loads(json_str)
bae = Bayes(message_list)
bae.train()

test_data = open(argv[2], 'r')
test_data = test_data.read()
test_data = json.loads(test_data)

    
def prob_class(string, clazz):
    S = set( string.split() )
    fv = bae.gen_feature_vector(S)
    return bae.prob_class(fv, clazz)

def main():
    tests = test_data

    out = {}
    for test in tests:
        o = {}
        for u in URGENCIES.keys():
            o[u] = prob_class(test, u)
        out[test] = o

    s = json.dumps(out)

    

    o = {}
    for test in tests:
        S = set( test )
        fv = bae.gen_feature_vector(S)
        o[test] = bae.classify(fv)

    ss = json.dumps(o)

#   print(s)
#   print("\n\n\n")
    print(ss)


if __name__ == '__main__':
    main()
