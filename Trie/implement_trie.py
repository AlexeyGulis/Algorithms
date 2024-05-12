class Trie:

    my_dict = None
    def __init__(self):
        self.my_dict = {}

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            if word[0:i + 1] not in self.my_dict:
                self.my_dict[word[0:i + 1]] = 0
        self.my_dict[word] = 1

    def search(self, word: str) -> bool:
        if word not in self.my_dict:
            return False
        return True if self.my_dict[word] == 1 else False

    def startsWith(self, prefix: str) -> bool:
        return True if prefix in self.my_dict else False


commands_list = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
input_list = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
my_object = None
answer = []
for i in range(len(commands_list)):
    if commands_list[i] == 'Trie':
        my_object = Trie()
        answer.append(None)
    if commands_list[i] == 'insert':
        my_object.insert(input_list[i][0])
        answer.append(None)
    if commands_list[i] == 'search':
        answer.append(my_object.search(input_list[i][0]))
    if commands_list[i] == 'startsWith':
        answer.append(my_object.startsWith(input_list[i][0]))

print(commands_list)
print(input_list)
print(answer)
