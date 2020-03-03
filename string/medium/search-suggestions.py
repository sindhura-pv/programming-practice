class Solution:
    def suggestedProducts(self, products, searchWord: str):

        def isprefix(word, prefix):
            j = 0
            if len(prefix) > len(word):
                return False

            for p in prefix:
                if word[j] != p:
                    return False
                j += 1

            return True

        products.sort()
        result = []

        for i in range(1, len(searchWord) + 1):
            matches = []
            temp_products = products

            # print(products, searchWord[:i])

            for product in products:
                if not isprefix(product, searchWord[:i]):
                    products.remove(product)
                else:
                    if len(matches) < 3:
                        matches.append(product)

            # products = temp_products
            result.append(matches)

        return result


