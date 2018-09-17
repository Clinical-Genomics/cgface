import requests
import json
from config import url


class CgFace(object):

    def __init__(self):
        self.url = url

    def apptag(self, tag_name, key=None, entry_point='/applications'):
        res = requests.get(self.url + entry_point + '/' + tag_name)

        if key:
            return json.loads(res.text)[key]
        else:
            return json.loads(res.text)

    def family(self, family_name, key=None, entry_point='/families'):
        res = requests.get(self.url + entry_point + '/' + family_name)

        if key:
            return json.loads(res.text)[key]
        else:
            return json.loads(res.text)

    def sample(self, sample_name, key=None, entry_point='/samples'):
        res = requests.get(self.url + entry_point + '/' + sample_name)

        if key:
            return json.loads(res.text)[key]
        else:
            return json.loads(res.text)

    def pool(self, pool_name, key=None, entry_point='/pools'):
        res = requests.get(self.url + entry_point + '/' + pool_name)

        if key:
            return json.loads(res.text)[key]
        else:
            return json.loads(res.text)

    def flowcell(self, flowcell_id, key=None, entry_point='/flowcells'):
        res = requests.get(self.url + entry_point + '/' + flowcell_id)
        if key:
            return json.loads(res.text)[key]
        else:
            return json.loads(res.text)

    def trends(self, level, year , key=None, entry_point='/trends'):
        res = requests.get(self.url + entry_point + '/' + level  + '/' + year)
        if key:
            return json.loads(res.text)[key]
        else:
            return json.loads(res.text)


    def get_applications(self):
        res = requests.get(self.url + '/applications')
        return res.json()['applications']

    def get_customers(self):
        res = requests.get(self.url + '/customers')
        return res.json()['customers']

    def get_families(self):
        res = requests.get(self.url + '/families')
        return res.json()['families']

    def get_panels(self):
        res = requests.get(self.url + '/panels')
        return res.json()['panels']

    def get_samples(self):
        res = requests.get(self.url + '/samples')
        return res.json()['samples']

    def get_pools(self):
        res = requests.get(self.url + '/pools')
        return res.json()['pools']

    def get_flowcells(self):
        res = requests.get(self.url + '/flowcells')
        return res.json()['flowcells']

    def get_analyses(self):
        res = requests.get(self.url + '/analyses')
        return res.json()['analyses']
    
        
        


