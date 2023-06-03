from pyspark.sql import SparkSession

# Create a Sparksession
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Read a text file into an RDD
lines = spark.sparkContext.textFile("input.txt")

#perform the word count
#lines is an RDD (Resilient Distributed Dataset) that represents a collection of lines, typically obtained from reading a text file using textFile() or a similar method.
word_counts = lines.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b)

#flatMap(lambda line: line.split(" ")) is a transformation applied to each line in the lines RDD. 
#It splits each line into words using the space character as the delimiter and flattens the resulting list of words into a single RDD. 
#This operation transforms the RDD from a collection of lines into a collection of words.

#map(lambda word: (word, 1)) is another transformation applied to each word in the RDD obtained from the previous step. It transforms each word into a key-value pair, where the word becomes the key, and the value is set to 1. This step associates each word with an initial count of 1.

# reduceByKey(lambda a, b: a + b) is a transformation that groups the key-value pairs by key and performs a reduction operation on the values associated with each key. In this case, it sums the values (counts) for each word. The result is an RDD with unique words as keys and their respective counts as values.


# repeating words

repeating_words = word_counts.filter(lambda x: x[1]>1)

#Print the word counts
for word, count in word_counts.collect():
    print(f"{word}: {count}")

for word, count in repeating_words.collect():
    print(f"{word}: {count}")    

# Stop the SparkSession
