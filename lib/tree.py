class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        return self._traverse(self.root, id)

    def _traverse(self, node, id):
        if node['id'] == id:
            return node

        for child in node['children']:
            result = self._traverse(child, id)
            if result:
                return result

        return None

