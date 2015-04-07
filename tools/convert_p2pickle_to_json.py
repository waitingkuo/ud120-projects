import pickle
import json

def convert(in_filename, out_filename):
    li = pickle.load(open(in_filename))
    json.dump(li, open(out_filename, 'w+'))

convert('email_authors.pkl.python2', 'email_authors.json')
convert('word_data.pkl.python2', 'word_data.json')
