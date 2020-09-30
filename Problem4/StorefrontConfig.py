class StorefrontConfig:
    def __init__(self, data):
        self.data = data

    def modify(self, d, md):
        for i in range(len(md.keys())):
            if isinstance(list(d.keys())[i], list):
                d[list(d.keys())[i]] = md[list(d.keys())[i]]
            elif isinstance(list(d.keys())[i], dict):
                self.modify(d[list(d.keys())[i]], md[list(d.keys())[i]])
            else:
                if list(d.keys())[i] in list(md.keys()):
                    d[list(d.keys())[i]] = md[list(d.keys())[i]]
                else:
                    pass

    def update(self, modify_data):
        self.modify(self.data, modify_data)
