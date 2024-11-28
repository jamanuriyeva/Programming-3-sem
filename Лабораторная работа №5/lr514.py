dict = {
      "Russia": ['Moscow', 'Yekaterinburg', "Saint-Petersburg"],
      "Azerbaijan": ['Baku', 'Ganja', 'Khachmaz'],
      "UAR": ['Dubai', 'Abu-Dhabi', 'Al Ain'],
}

cities = ['Moscow', 'Dubai', 'Baku','Saint-Petersburg']

class City_Iterator():

  def __init__(self,lst,dict):
      self.iterable = lst
      self.dict = dict
      self.idx = 0

  def __iter__(self):
      return self

  def __next__(self):
      if self.idx < len(self.iterable):
          self.idx += 1
          city = self.iterable[self.idx-1]
          for items in self.dict.items():
              if city in items[1]:
                  return items[0]
      else:
          raise StopIteration

iter = City_Iterator(cities,dict)
for city in iter:
  print(city)