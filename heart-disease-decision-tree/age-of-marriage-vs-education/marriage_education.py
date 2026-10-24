# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util


lwd=pd.read_csv("livwell135.csv")

#number of rows and columns
print(lwd.shape)

#Filter for India
IndiaBooleanList = lwd["country_name"] == "India"
IndiaData = lwd.loc[IndiaBooleanList]

#scatter plot 1
plt.scatter( x = IndiaData["year"], y = IndiaData["ED_educ_years_mean"])
plt.title("Female average/median years of schooling change over time")
plt.xlabel("Year")
plt.ylabel("Female average/median years of schooling")
plt.show()
plt.close()

#
print("In the early 2000s, the Indian government launched initiatives such as Sarva Shiksha Abhiyan (Education for All) to expand access to free elementary education. This helped more girls stay in school, which is reflected in the increase in average years of schooling shown in the graph. In 2001, the Indian government also adopted the National Policy for the Empowerment of Women to improve women's access to education, healthcare, employment, and equal opportunities.                                                                                                                             ")

input("                                                                                 Press enter to continue...\n")

print("The scatter plot shows that average years of schooling and the female average age at marriage are positively correlated. As India's economy improved, more educational and employment opportunities became available. Many families placed greater value on higher education and professional careers, which may have contributed to women marrying later. The next scatter plot further illustrates this relationship.")



#scatter plot 2
plt.scatter(x = IndiaData["DM_age_marr_mean"],y = IndiaData["ED_educ_years_mean"], color = "red")

plt.title("Female average age at marriage vs average years of schooling in India")
plt.xlabel("Female average age at marriage")
plt.ylabel("Female average/median years of schooling")

plt.show()
plt.close()

input("                                                                                 Press enter to continue...\n")



print("The graph shows that the average age at marriage increased steadily over time. Combined with the previous graphs, this suggests that as women's education improved, the average age at marriage also increased in India.")

#scatter plot 3

plt.scatter( x = IndiaData["year"], y = IndiaData["DM_age_marr_mean"])
plt.title("Female average age at marriage change over time")
plt.xlabel("year")
plt.ylabel("Female average age at marriage")

plt.show()
plt.close()

input("                                                                                 Press enter to continue...\n")

print("My research question is: ")
print("What factors other than education can help increase the average age at marriage among women in India ?")
print("Thank you for reading my story")



