"""An example of how to represent a group of acquaintances in Python."""
import pandas as pd
Jill = {"Name" : "Jill", "Age" : "26", "Job" : "Biologist", "Connections" : ("Zalika's friend", "John's partner")}
Zalika = {"Name" : "Zalika", "Age" : "28", "Job" : "Artist", "Connections" : "Jill's friend"}
John = {"Name" : "John", "Age" : "27", "Job" : "Writer"}
my_group = [Jill,Zalika,John,Nash]

df = pd.DataFrame(data = my_group)