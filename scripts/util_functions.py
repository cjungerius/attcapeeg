import json

def get_subject_info(id):
        
        with open('contexts.json') as f:
                data = json.load(f)
        
        subject_data = data['subject'][str(id)]

        context_list = subject_data['contexts']
        contexts = []
        for l in context_list:
                location_contexts = []
                for s in l :
                        location_contexts.append([list(filter(str.isalnum, s))])
                contexts.append(location_contexts)

        target_color = subject_data['target_color']
        target_shape = subject_data['target_shape']

        return contexts, target_color, target_shape

