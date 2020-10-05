class StorefrontConfig:
    def __init__(self, data):
        self.data = data

    def modify(self, d, md):
        for key in d.keys():
            if isinstance(d.get(key), list):
                d[key] = md[key]
            elif isinstance(d.get(key), dict) and isinstance(md.get(key), dict):
                self.modify(d[key], md[key])
            else:
                if key in md.keys():
                    d[key] = md[key]
                else:
                    pass

    def update(self, modify_data):
        self.modify(self.data, modify_data)
