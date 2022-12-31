# import mrjob dependency
from mrjob.job import MRJob

# create class
class Bacon_count(MRJob):
   # define mapper function to assign input to k-v pairs
   def mapper(self, _, line):
       # generator
       for word in line.split():
           if word.lower() == "bacon":
               yield "bacon", 1
   # reducer function
   def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Bacon_count.run()