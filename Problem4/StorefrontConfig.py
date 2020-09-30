class StorefrontConfig:
    def __init__(self, data):
        self.data = data

    def update(self, modify_data):
        for i in range(len(modify_data.keys())):
            self.data[m_keys[i]] = modify_data[m_keys[i]]