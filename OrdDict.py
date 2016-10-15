class OrdDict:
    """ Dictionnaire ordonné et pouvant donc être trié. """
    def __init__(self,dictio={},**data):
        """ Constructeur. Aucun paramètre OU construit depuis un dictionnaire.
        OU depuis des valeurs. """
        self._keys = []
        self._values = []
        for key in dictio:
            self[key] = dictio[key]
        for key in data:
            self[key] = data[key]
        
    def __repr__(self):
        """ Affichage du dictionnaire (avec appel : >>>nom_dict). """
        string = "{"
        for key,value in self.items():
            string += "{}:{},".format(repr(key),repr(value))
        if string[-1] == ",":string = string[:-1]
        return string + "}"

    def __str__(self):
        """ Affichage du dictionnaire (avec appel : >>>print(nom_dict). """
        return repr(self)

    def __len__(self):
        """ Taille du dictionnaire. """
        return len(self._keys)

    def __contains__(self,key):
        """ Clef contenue dans le dictionnaire. """
        return key in self._keys

    def __getitem__(self,key):
        """ Valeur correspondant à la clef dans le dictionnaire. """
        return self._values[self._keys.index(key)]

    def __setitem__(self,key,value):
        """ Ajout ou modification de la valeur d'une clef. """
        if key in self._keys:
            self._values[self._keys.index(key)]
        else:
            self._keys.append(key)
            self._values.append(value)

    def __delitem__(self,key):
        """ Suppression d'une clef. """
        del self._values[self._keys.index(key)]
        del self._keys[self._keys.index(key)]

    def __iter__(self):
        """ Parcours du dictionnaire. """
        return iter(self._keys)

    def __add__(self,dictio):
        """ Concatène deux dictionnaires. """
        temp_dictio = OrdDict()
        for key,value in self.items():
            temp_dictio[key] = value
        for key,value in dictio.items():
            temp_dictio[key] = value
        return temp_dictio

    def items(self):
        """ Renvoie les couples clefs valeurs. """
        for i, key in enumerate(self._keys):
            yield (key,self._values[i])

    def keys(self):
        """ Renvoie la liste des clefs. """
        return list(self._keys)

    def values(self):
        """ Renvoie la liste des valeurs. """
        return list(self._values)

    def reverse(self):
        """ Inverse le dictionnaire. """
        keys,values = [],[]
        for key,value in self.items():
            keys.insert(0,key)
            values.insert(0,value)
        self._keys = keys
        self._values = values

    def sort(self):
        """ Trie le dictionnaire en fonction des clefs. """
        sorted_keys = sorted(self._keys)
        sorted_values = [self[key] for key in sorted_keys]
        self._keys = sorted_keys
        self._values = sorted_values
        

fruits = OrdDict()
print(fruits)
fruits["pomme"] = 52
fruits["poire"] = 34
fruits["melon"] = 128
fruits["prune"] = 15
print(fruits)
fruits.sort()
print(fruits)
legumes = OrdDict(carotte = 26, haricot = 48)
print(legumes)
print(len(legumes))
legumes.reverse()
print(legumes)
print(fruits)
fruits = fruits + legumes
print(fruits)
print('haricot' in fruits)
del fruits['haricot']
print('haricot' in fruits)
print(legumes['haricot'])
for key in legumes:
    print(key)
print(legumes.keys())
print(legumes.values())
for name,qtt in legumes.items():
    print("{} ({})".format(name,qtt))















        
        
    
        
