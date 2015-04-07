import pickle
import json

def convert(in_filename, out_filename):
    li = json.load(open(in_filename))
    pickle.dump(li, open(out_filename, 'wb+'))

convert('email_authors.json', 'email_authors.pkl')
convert('word_data.json', 'word_data.pkl')
